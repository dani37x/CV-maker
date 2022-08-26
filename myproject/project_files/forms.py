from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
# from flask_uploads import UploadSet
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import Length, DataRequired, Email
import email_validator




class Informations(FlaskForm):

  first_name = StringField('first_name', validators=[DataRequired(), Length(max=30)])
  second_name = StringField('second_name', validators=[DataRequired(), Length(max=30)])
  e_mail = StringField('e_mail', validators=[Email(), DataRequired()])
  birthday= StringField('birthday', validators=[DataRequired()])
  city = StringField('city', validators=[DataRequired()])
  phone_number = StringField('phone number', validators=[DataRequired(), Length(max=19)])
  info = TextAreaField('Tell something about you in five sentences', validators=[DataRequired(), Length(max=1024)])
  file = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
  button = SubmitField('send data')


