from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bamboon'}
    posts = [
        {
            'author': {'username': 'Bob'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Alice'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Bootlicker3000'},
            'body': 'I LICK BOOTS!'
        }
    ]
    return render_template('index.html', title='Mine', user=user, posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me = {}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title="login form", form=form)
