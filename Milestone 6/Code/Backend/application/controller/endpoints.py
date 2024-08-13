from app import db, api, app
from application.data.models import User, Content, Lecture, Assignment, Question, UserQuestion, Course, CourseEnrollment
# from sqlalchemy import JSON
from flask import jsonify, render_template, request
import ollama

#To display list of weeks
@app.route('/contents', methods=['GET'])
def get_weeks():
    weeks = {}
    contents = Content.query.all()
    for content in contents:
        weeks[content.week] = f'Week {content.week}'
    return jsonify(weeks)

#To display contents inside weeks
@app.route('/contents/<int:week>', methods=['GET'])
def get_content_titles(week):
    lectures = Lecture.query.filter_by(week=week).all()
    assignments = Assignment.query.filter_by(week=week).all()

    lecture_list = [{"lec_id": lec.lec_id, "title": lec.title} for lec in lectures]
    assignment_list = [{"assign_id": assign.assign_id, "title": assign.title} for assign in assignments]

    return jsonify({
        "lectures": lecture_list,
        "assignments": assignment_list
    }), 200

#To view assignments.
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


#To get feedback
@app.route('/feedback/<int:assign_id>', methods=['GET'])
def get_user_feedback(assign_id):
    #user_id = 1
    answered_questions = UserQuestion.query.filter_by(user_id=user_id,is_correct=False,assignment_id=assign_id).all()
    result = []
    for answer in answered_questions:
        if not answer.code_submission: # to check if it is a mcq type
            question = Question.query.get(answer.question_id)
            feedback = ollama.generate(model='llama3',prompt=f' Give me a feedback why my ans is wrong. This is the option i selected: {answer.selected_answer}. This is the question: {question.question_text} This is the option: {question.options}')
            result.append({
                'question_text': question.question_text,
                'selected_answer': answer.selected_answer,
                'is_correct': answer.is_correct,
                'correct_answer': question.correct_answer,
                'feedback': feedback['response']
            })
        else: # for coding type
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

#To get summary
@app.route('/get_summary/<int:lec_id>', methods=['GET'])
def get_lec_summary(lec_id):
    lecture = Lecture.query.get(lec_id)
    summary = ollama.generate(model='phi3', prompt=f'Give me a summary of this lecture: {lecture.transcript}')
    return jsonify({'summary': summary['response']})