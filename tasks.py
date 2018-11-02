

from datetime import datetime as dt
from invoke import task

VERSION = "0.25"

SRV = "core@brain"


@task
def build(c):
    """Build and deploy new version."""

    c.run(f"docker build -t showminder/showminder:{VERSION} -t showminder/showminder:latest .")
    c.run(
        f"ssh {SRV} docker service update --image showminder/showminder:{VERSION} --env-add SHOWMINDER_VERSION={VERSION} showminder"
    )


@task
def backup(c):
    """Create a backup of prod database."""
    c.run(
        f"pg_dump --host=brain.local --username=showminder --file=backup/showminder.{dt.now():%Y-%m-%d}.sql showminder"
    )
    c.run(f"ls -lrt backup")
