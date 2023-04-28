# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    username = StringField('Username')
    image = FileField("Image") 
    submit = SubmitField('Post')
    #Add a SelectField (drop down list) to the ProfileForm in forms.py
    role = SelectField('Role',choices=[("Rizzler","Rizzler"), ("Rizziple", "Rizziple")])
    #role = SelectField('Role',choices=[("Rizzler","Rizzler"),("Rizziple", "Rizziple"), ("Grand Rizzard","Grand Rizzard")])
    purpose = SelectField('Purpose',choices=[("Get Some Rizz","Get Some Rizz"),("Help Others Get Rizz","Help Others Get Rizz"),("Other","Other")])

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class GrandQuestionForm(FlaskForm):
    gQuestion = TextAreaField('GrandQuestion', validators=[DataRequired()])
    submit = SubmitField('GrandQuestion')

#!bruh