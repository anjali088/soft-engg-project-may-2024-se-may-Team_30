from app import db, api, app
from application.data.models import User, Content, Lecture, Assignment, Question, UserQuestion, Course, CourseEnrollment
# from sqlalchemy import JSON
from flask import jsonify, render_template, request
import ollama


@app.route('/get_summary/<int:lec_id>', methods=['GET'])
def get_lec_summary(lec_id):
    lecture = Lecture.query.get(lec_id)
    summary = ollama.generate(model='phi3', prompt=f'Give me a summary of this lecture: {lecture.transcript}')
    return jsonify({'summary': summary['response']})

@app.route('/feedback/<int:assign_id>', methods=['GET'])
def get_user_feedback(assign_id):
    user_id = 1
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
    return render_template('answer.html', answered_questions=result), 200
