import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = get_db().cursor()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            cur.execute(
            'SELECT id FROM auth_user WHERE username = %s', (username,)
            )
            if cur.fetchone() is not None:
                error = f'User {username} is already registered.'

        if error is None:
            cur.execute(
                'INSERT INTO auth_user (username, password) VALUES (%s, %s )',
                (username, generate_password_hash(password))
            )
            return redirect(url_for('auth.login'))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cur = db.cursor()
        error = None
        cur.execute("SELECT id, password FROM auth_user WHERE username = %s", (username,))
        res = cur.fetchone()
        
        if res:
            user_id, user_pass = res
            if not check_password_hash(user_pass, password):
                error = 'Incorrect password.'
        else:
            error = 'Incorrect username.'

        if error is None:
            session.clear()
            session['user_id'] = user_id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        cur = get_db().cursor()
        cur.execute('SELECT * FROM auth_user WHERE id = %s', (user_id,))
        g.user = cur.fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)

    return wrapped_view