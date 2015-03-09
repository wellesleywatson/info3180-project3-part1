from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, FileField, PasswordField
from wtforms.validators import Required

class ProfileForm(Form):
      first_name = TextField('First Name', validators=[Required()])
      last_name = TextField('Last Name', validators=[Required()])
      user_name = TextField('User Name', validators=[Required()])
      age = IntegerField('Age', validators=[Required()])
      sex = SelectField('Sex', choices=[('Male','Male'),('Female','Female')] , validators=[Required()])
      email = TextField('Email Address', [validators.Length(min=6, max=35)])
      password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
      confirm = PasswordField('Confirm Password')
      image  = FileField('Image', validators=[Required()])
      
      
      