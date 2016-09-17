from flask import render_template, flash, redirect
from app import blg
from .forms import LoginForm


@blg.route('/')
@blg.route('/index')
def index():
    user = {'nickname': 'Kelb'}  # fake user... or is he?
    posts = [  # fake array of posts
            {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
                },
            {
                'author': {'nickname': 'Susan'},
                'body': 'The Avengers movie was so cool!'
                }
            ]
    return render_template(
        'index.html', title=user['nickname'], user=user, posts=posts)


@blg.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash function is a quick way to show a message on the next page
        # presented to the user [ see 'base' template ].
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template(
        'login.html', title='Sign In',
        form=form,
        providers=blg.config['OPENID_PROVIDERS'])
