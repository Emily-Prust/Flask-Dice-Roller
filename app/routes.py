from flask import render_template, flash, redirect
from app import app
from app.forms import RollForm
from app.roll import roll


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
    rolls = [
        {
            'note': {'note': 'Roll for hit'},
            'roll': {'amount': 2, 'dice_number': 6, 'roll_result': '1, 1'}
        },
        {
            'note': {'note': 'Roll for damage'},
            'roll': {'amount': 6, 'dice_number': 18, 'roll_result': '2, 16, 6, 6, 1, 13'}
        }
    ]
    form = RollForm()
    if form.validate_on_submit():
        note = form.note.data
        amount = form.amount.data
        dice_number = form.dice_number.data
        rolls.append({
            'note': {'note': note},
            'roll': {'amount:': amount, 'dice_number': dice_number, 'roll_result': roll(amount, dice_number)}
        })
        return redirect('/private_roll')
    return render_template('private_roll.html', title='Private Roll', rolls=rolls, form=form)
