from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    question_subject = StringField("subject", validators=[DataRequired('Title is Required. Try it againg.')])
    question_content = TextAreaField("content", validators=[DataRequired('Content is Required.Try it again.')])
    
class AnswerForm(FlaskForm):
    answer_content = TextAreaField("content", validators=[DataRequired('Content is Requiered.')])

class UserCreateForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=5, max=12)])
    password = PasswordField("password", validators=[DataRequired(), EqualTo('password_check', 'Not Matched')])
    password_check = PasswordField("password_check", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=5, max=12)])
    password = PasswordField("password", validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField("content", validators=[DataRequired()])
