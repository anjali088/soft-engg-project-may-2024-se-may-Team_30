from .database import db
from datetime import datetime

# User Model
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    answered_questions = db.relationship('UserQuestion', backref='user')
    enrollments = db.relationship('CourseEnrollment', backref='user')

# Content Model
class Content(db.Model):
    __tablename__ = 'contents'
    content_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)
    isopen = db.Column(db.Boolean())
    lecture = db.relationship('Lecture', backref='content', lazy=True)
    assignment = db.relationship('Assignment', backref='content', lazy=True)

# Lecture Model
class Lecture(db.Model):
    __tablename__ = 'lectures'
    lec_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    week = db.Column(db.Integer)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.content_id'))
    video_url = db.Column(db.String(500), nullable=False)
    transcript = db.Column(db.Text)
    duration = db.Column(db.Integer)
    difficulty_level = db.Column(db.String(20))

# Assignment Model
class Assignment(db.Model):
    __tablename__ = 'assignments'
    assign_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    week = db.Column(db.Integer)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.content_id'))
    due_date = db.Column(db.DateTime)
    total_points = db.Column(db.Integer, default=100)
    questions = db.relationship('Question', backref='assignment')
    solved_by = db.relationship('UserQuestion', backref='assignment')

# Question Model
class Question(db.Model):
    __tablename__ = 'questions'
    que_id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assign_id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON)
    correct_answer = db.Column(db.String(200), nullable=False)
    points = db.Column(db.Integer, default=10)
    difficulty = db.Column(db.String(20))
    solved_by = db.relationship('UserQuestion', backref='question')

# UserQuestion Model
class UserQuestion(db.Model):
    __tablename__ = 'user_questions'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.que_id'), primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assign_id'), primary_key=True)
    selected_answer = db.Column(db.String(200))
    code_submission = db.Column(db.Text)
    is_correct = db.Column(db.Boolean, nullable=False)
    submission_time = db.Column(db.DateTime)
    points_earned = db.Column(db.Integer)

# Course Model
class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    instructor_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=True)
    enrollments = db.relationship('CourseEnrollment', backref='course')
    contents = db.relationship('Content', backref='course')

# CourseEnrollment Model
class CourseEnrollment(db.Model):
    __tablename__ = 'course_enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    completion_date = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean, default=False)