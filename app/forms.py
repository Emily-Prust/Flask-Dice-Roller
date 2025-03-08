from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import sqlalchemy as sa
from app import db
from app.models import Roll


class RollForm(FlaskForm):
    note = StringField('Note', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[
                          DataRequired(), NumberRange(min=1, max=999,
                                                      message="Input must be between 0 and 1000.")
                          ])
    dice_number = IntegerField('Dice Number', validators=[
                               DataRequired(), NumberRange(min=1, max=999,
                                                           message="Input must be between 0 and 1000.")
                               ])
    submit = SubmitField('Roll!')
