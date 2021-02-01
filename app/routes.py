from app.forms import LoginForm
from app import app
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jay'}#Dictionary with my name
    posts = [ #List of dictionaries
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) #Call the template for this weburl and pass in data
@app.route('/login', methods=['GET', 'POST']) #GET AND POST let user get and submit back
def login():
    form=LoginForm()# call form function froms form.py
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title='Sign In', form=form)#Call the template for this weburl if failed attempt