from flask import render_template
from app import blg


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
