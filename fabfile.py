
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import task

env.hosts = ['brain']
env.user = "core"

VERSION = '0.20'


@task
def build():
    # build
    local(f"docker build -t showminder/showminder:{VERSION} -t showminder/showminder:latest .")
    run(f'docker service update --image showminder/showminder:{VERSION} showminder')


@task
def backup():
    """Create a backup of prod database."""
    local("pg_dump --host=brain.local --username=showminder --file=showminder.sql showminder")
