from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/login', methods=["GET", "POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me{}".format(form.username.data, remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title= 'Sign In', form = form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html')