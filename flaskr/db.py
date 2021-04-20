import os
# import sqlite3
import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            f"dbname={os.environ['POSTGRES_DB']} user={os.environ['POSTGRES_USER']} password={os.environ['POSTGRES_PASSWORD']} host=db"
        )

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.commit()
        db.close()

def init_db():
    db = get_db().cursor()

    with current_app.open_resource('schema.sql') as f:
        db.execute(f.read().decode('utf8'))

    
@click.command('init_db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)