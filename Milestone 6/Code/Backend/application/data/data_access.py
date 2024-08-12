from application.data.models import User, Content, Lecture, Assignment, Question, UserQuestion, Course, CourseEnrollment
from application.data.database import db
from flask import session
from app import cache

def getContent(course):
    course_content = Content.query.filter_by(content_id = course).all()

    return course_content
