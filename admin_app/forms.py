from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, TimeField, PasswordField
from wtforms.validators import DataRequired, Length

class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=100)])
    author = StringField("Author", validators=[DataRequired()], default="Liam Callahan")
    excerpt = TextAreaField("Excerpt", validators=[DataRequired(), Length(max=300)])
    content = TextAreaField("Content", validators=[DataRequired()])
    # timestamp = DateTimeField("Timestamp", format="%Y-%m-%d %H:%M:%S")
    date = DateField("Timestamp", format="%Y-%m-%d", default=datetime.now())
    time = TimeField("Timestamp", format="%H:%M:%S", default=datetime.now())
    submit = SubmitField("Create Post")

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=3, max=100)])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=100)])
  submit = SubmitField("Log In")