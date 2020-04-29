#oners view in the owners folder
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Parent:')
    pup_id = IntegerField("Id of Student: ")
    submit = SubmitField('Add Parent')
