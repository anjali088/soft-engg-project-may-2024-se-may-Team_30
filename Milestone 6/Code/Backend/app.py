from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import JSON
import ollama
import os
from datetime import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
SQLITE_DB_DIR = os.path.join(basedir, "db_directory")
print(SQLITE_DB_DIR)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, 'database.sqlite3')
SECRET_KEY = 'thisisasecretkey'
app.secret_key = SECRET_KEY
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

CORS(app, resources={r'/*': {'origins': '*'}})


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    answered_questions = db.relationship('UserQuestion', backref='user')


class Content(db.Model):
    __tablename__ = 'contents'
    content_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)  # To know if the given content is Lec or Assign
    lecture = db.relationship('Lecture', backref='content')
    assignment = db.relationship('Assignment', backref='content')


class Lecture(db.Model):
    __tablename__ = 'lectures'
    lec_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    week = db.Column(db.Integer)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.content_id'), nullable=False)
    video_url = db.Column(db.String(500), nullable=False)
    transcript = db.Column(db.Text)


class Assignment(db.Model):
    __tablename__ = 'assignments'
    assign_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    week = db.Column(db.Integer)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.content_id'), nullable=False)
    questions = db.relationship('Question', backref='assignment')
    solved_by = db.relationship('UserQuestion',
                                backref='assignment')  # Relationship to UserQuestion model, indicating which users have solved the assignment.


class Question(db.Model):
    __tablename__ = 'questions'
    que_id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assign_id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON)  # JSON field to store options
    correct_answer = db.Column(db.String(200), nullable=False)
    solved_by = db.relationship('UserQuestion',
                                backref='question')  # Relationship to UserQuestion model, indicating which users have answered the question.


class UserQuestion(db.Model):
    __tablename__ = 'user_questions'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.que_id'), primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assign_id'), primary_key=True)
    selected_answer = db.Column(db.String(200))
    code_submission = db.Column(db.Text)
    is_correct = db.Column(db.Boolean, nullable=False)


# db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.json
    username = 'sanket'  # data.get('username')
    password = 'password'  # data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or user.password == password:
        return jsonify({'error': 'Invalid username or password'}), 401

    session['user_id'] = user.user_id
    return jsonify({'message': 'Login successful', 'user_id': user.user_id})


@app.route('/logout', methods=['GET'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')
        return jsonify({'message': 'Logout successful'})
    else:
        return jsonify({'message': 'Login First'})

@app.route('/contents', methods=['GET'])
# To display list of weeks
def get_weeks():
    weeks = {}
    contents = Content.query.all()
    for content in contents:
        weeks[content.week] = f'Week {content.week}'
    return jsonify(weeks)


@app.route('/contents/<int:week>', methods=['GET'])
# To display contents inside weeks
def get_content_titles(week):
    lectures = Lecture.query.filter_by(week=week).all()
    assignments = Assignment.query.filter_by(week=week).all()

    lecture_list = [{"lec_id": lec.lec_id, "title": lec.title} for lec in lectures]
    assignment_list = [{"assign_id": assign.assign_id, "title": assign.title} for assign in assignments]

    return jsonify({
        "lectures": lecture_list,
        "assignments": assignment_list
    }), 200

@app.route('/lec/<int:lec_id>/<int:week>', methods=['GET'])
def get_lecture(lec_id, week):
    lecture = Lecture.query.filter_by(lec_id=lec_id, week=week).first_or_404()
    return jsonify({
        "lec_id": lecture.lec_id,
        "week": lecture.week,
        "title": lecture.title,
        "video_url": lecture.video_url,
        "transcript": lecture.transcript
    }), 200


@app.route('/assignment/<int:assign_id>/<int:week>', methods=['GET'])
def get_assignment(assign_id, week):
    assignment = Assignment.query.filter_by(assign_id=assign_id, week=week).first_or_404()
    questions = [
        {"que_id": q.que_id, "question_text": q.question_text, "options": q.options, "correct_answer": q.correct_answer}
        for q in assignment.questions]

    return jsonify({
        "assign_id": assignment.assign_id,
        "week": assignment.week,
        "title": assignment.title,
        "questions": questions
    }), 200


@app.route('/feedback/<int:assign_id>', methods=['GET'])
def get_user_feedback(assign_id):
    user_id = 1
    answered_questions = UserQuestion.query.filter_by(user_id=user_id, is_correct=False, assignment_id=assign_id).all()
    result = []
    for answer in answered_questions:
        if not answer.code_submission:  # to check if it is a mcq type
            question = Question.query.get(answer.question_id)
            feedback = ollama.generate(model='llama3',
                                       prompt=f' Give me a feedback why my ans is wrong. This is the option i selected: {answer.selected_answer}. This is the question: {question.question_text} This is the option: {question.options}')
            result.append({
                'question_text': question.question_text,
                'selected_answer': answer.selected_answer,
                'is_correct': answer.is_correct,
                'correct_answer': question.correct_answer,
                'feedback': feedback['response']
            })
        else:  # for coding type
            question = Question.query.get(answer.question_id)
            feedback = ollama.generate(model='llama3',
                                       prompt=f' Give me a feedback on why my ans is wrong. This is the code i have written: {answer.code_submission}. This is the question: {question.question_text}')
            result.append({
                'question_text': question.question_text,
                'selected_answer': answer.selected_answer,
                'is_correct': answer.is_correct,
                'correct_answer': question.correct_answer,
                'feedback': feedback['response']
            })
    return jsonify(result), 200


@app.route('/get_summary/<int:lec_id>', methods=['GET'])
def get_lec_summary(lec_id):
    lecture = Lecture.query.get(lec_id)
    summary = ollama.generate(model='phi3', prompt=f'Give me a summary of this lecture: {lecture.transcript}')
    return jsonify({'summary': summary['response']})

@app.route('/get_links/<int:lec_id>', methods=['GET'])
def get_lec_links(lec_id):
    lecture = Lecture.query.get(lec_id)
    links = ollama.generate(model='llama3', prompt=f'f Give me links to study more about this topic: {lecture.title}')
    return jsonify({'links': links['response']})


@app.route('/submit_assignment/<int:assignment_id>', methods=['POST'])
def submit_assignment(assignment_id):
    data = request.get_json()

    user_id = data.get('user_id')
    submitted_answers = data.get('answers', [])

    if not user_id or not submitted_answers:
        return jsonify({'error': 'User ID and answers are required'}), 400

    # Fetch the assignment to ensure it exists
    assignment = Assignment.query.filter_by(assign_id=assignment_id).first_or_404()

    total_points_earned = 0

    for answer in submitted_answers:
        question_id = answer.get('question_id')
        selected_answer = answer.get('selected_answer')
        code_submission = answer.get('code_submission')  # Optional, if applicable

        # Fetch the question
        question = Question.query.filter_by(que_id=question_id, assignment_id=assignment_id).first_or_404()

        # Check if the selected answer is correct
        is_correct = (question.correct_answer == selected_answer)
        points_earned = question.points if is_correct else 0
        total_points_earned += points_earned

        # Record the submission in the UserQuestion table
        user_question = UserQuestion(
            user_id=user_id,
            question_id=question_id,
            assignment_id=assignment_id,
            selected_answer=selected_answer,
            code_submission=code_submission,
            is_correct=is_correct,
            submission_time=datetime.utcnow(),
            points_earned=points_earned
        )

        db.session.add(user_question)

    # Commit all changes to the database
    db.session.commit()

    response_data = {
        'assignment_id': assignment_id,
        'user_id': user_id,
        'total_points_earned': total_points_earned,
        'status': 'Submission successful'
    }
    return jsonify(response_data), 201



if __name__ == '__main__':
    app.run(debug=True)