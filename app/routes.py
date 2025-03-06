from flask import render_template, flash, redirect
from app import app, db
import sqlalchemy as sa
from app.forms import RollForm
from app.models import Roll


@app.route('/')
@app.route('/index')
def index():
    # Mock data
    user = {'username': 'John'}
    rolls = [
        {
            'author': {'username': 'Snake Eyes Bert'},
            'roll': {'amount': 2, 'dice_number': 6, 'roll_result': '1, 1'}
        },
        {
            'author': {'username': 'Phil the Librarian'},
            'roll': {'amount': 6, 'dice_number': 18, 'roll_result': '2, 16, 6, 6, 1, 13'}
        }
    ]

    return render_template('index.html', title='Home', user=user, rolls=rolls)


@app.route('/private_roll', methods=['GET', 'POST'])
def private_roll():
    form = RollForm()
    if form.validate_on_submit():
        new_roll = Roll(note=form.note.data, amount=form.amount.data,
                        dice_number=form.dice_number.data)
        new_roll.generate_roll(form.amount.data,
                               form.dice_number.data)
        db.session.add(new_roll)
        db.session.commit()
        return redirect('/private_roll')
    return render_template('private_roll.html', title='Private Roll', form=form)
