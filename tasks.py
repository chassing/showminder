from datetime import datetime as dt

from invoke import task


@task
def backup(c):
    """Create a backup of prod database."""
    # conda install postgresql
    postgres_password = c.run(
        'kubectl get secret --namespace showminder showminder-postgres-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode',
        pty=True,
    )
    c.run(
        f"pg_dump --dbname='postgres://postgres:{postgres_password.stdout}@192.168.0.64:5432/showminder' --file=backup/showminder.{dt.now():%Y-%m-%d}.sql",
    )
    c.run("ls -lrt backup")


@task
def release(c):
    c.run("docker build -t chassing/showminder:latest .", pty=True)
    c.run("docker push chassing/showminder:latest", pty=True)
    c.run("kubectl rollout restart deployment showminder")


@task
def nativefier(c):
    # brew install nativefier
    c.run(
        "nativefier http://showminder.ca-net.org . --name ShowMinder --inject window.js --inject site.css --title-bar-style 'hiddenInset' --hide-window-frame --tray --darwin-dark-mode-support",
        pty=True,
    )
    c.run("rm -rf /Users/cassing/bin/ShowMinder.app")
    c.run("mv ShowMinder-darwin-x64/ShowMinder.app /Users/cassing/bin/")


"""

scp rancher@192.168.0.64:/etc/rancher/k3s/k3s.yaml $HOME/.kube/config_k3s
vim $HOME/.kube/config_k3s
192.168.0.64

pip install db-to-sqlite
rm -f db.sqlite3 ; db-to-sqlite "postgres://$DB_USER:$DB_PASSWORD@$DB_HOST/showminder" db.sqlite3 --all
"""
