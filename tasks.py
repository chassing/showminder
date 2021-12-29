from datetime import datetime as dt

from invoke import task


@task
def backup(c):
    """Create a backup of prod database."""
    # conda install postgresql
    p = c.run(
        'kubectl get secret --namespace showminder showminder-postgres-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode',
        pty=True,
    )
    print(p)
    c.run(
        f"pg_dump --host=192.168.0.64 --username=postgres -W --file=backup/showminder.{dt.now():%Y-%m-%d}.sql showminder"
    )
    c.run("ls -lrt backup")


@task
def release(c):
    c.run("docker build -t chassing/showminder:latest .", pty=True)
    c.run("docker push chassing/showminder:latest", pty=True)
    c.run("kubectl rollout restart deployment showminder")


"""
pip install db-to-sqlite
rm -f db.sqlite3 ; db-to-sqlite "postgres://$DB_USER:$DB_PASSWORD@$DB_HOST/showminder" db.sqlite3 --all
"""
