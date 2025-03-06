from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class RollForm(FlaskForm):
    note = StringField('Note')
    amount = IntegerField('Amount', validators=[DataRequired()])
    dice_number = IntegerField('Dice Number', validators=[DataRequired()])
    submit = SubmitField('Roll!')
