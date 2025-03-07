from flask import render_template, flash, redirect
from app import app, db
import sqlalchemy as sa
from app.forms import RollForm
from app.models import Roll


@app.route('/')
@app.route('/index')
def index():
    query = sa.select(Roll)
    rolls = db.session.scalars(query).all()

    return render_template('index.html', title='Home', rolls=rolls)


@app.route('/roll', methods=['GET', 'POST'])
def roll():
    query = sa.select(Roll)
    rolls = db.session.scalars(query).all()
    form = RollForm()
    if form.validate_on_submit():
        new_roll = Roll(note=form.note.data, amount=form.amount.data,
                        dice_number=form.dice_number.data)
        new_roll.generate_roll(form.amount.data,
                               form.dice_number.data)
        db.session.add(new_roll)
        db.session.commit()
        return redirect('/roll')
    return render_template('roll.html', title='Roll', form=form, rolls=rolls)
