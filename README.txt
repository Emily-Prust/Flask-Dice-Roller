A simple Flask application that generates and displays random numbers, saving
them to a database.

Created as I was curious about how a web application communicates with a database.

!!! As there is no input verification on the dice amount/dice number inputs,
    inputs like negative values will require the database be cleaned, the
    easiest way to do this is with:

    $ flask db downgrade
    $ flask db upgrade

    WARNING: this will delete all previous entries.


INSTRUCTIONS:

Set up virtual environment
$ python3 -m venv venv 

Clone this repo
$ git clone https://github.com/Emily-Prust/Flask-Dice-Roller.git 

Install requirements
$ pip install -r requirements.txt

Run the app by using
$ flask run

then visit
http://127.0.0.1:5000


For a demonstration, look at:
https://emilyprust.pythonanywhere.com/index
