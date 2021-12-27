from datetime import datetime as dt

import environ
from invoke import task

env = environ.Env(DEBUG=(bool, False))
env.read_env()
DB = f"postgres://{env('DB_USER', default='user')}:{env('DB_PASSWORD', default='password')}@{env('DB_HOST', default='postgres')}/showminder"


@task
def backup(c):
    """Create a backup of prod database."""
    c.run(
        f"pg_dump --host={env('DB_HOST')} --username={env('DB_USER')} --no-password --file=backup/showminder.{dt.now():%Y-%m-%d}.sql showminder"
    )
    c.run(f"ls -lrt backup")


"""
pip install db-to-sqlite

db-to-sqlite "postgres://$DB_USER:$DB_PASSWORD@$DB_HOST/showminder" showminder.db --all
"""
