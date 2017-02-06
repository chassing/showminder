# -*- coding: utf-8 -*-
from datetime import date
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import task

env.hosts = ['brain']
env.user = "core"

VERSION = '0.10'


@task
def build():
    # build
    local(f"docker build -t showminder/showminder:{VERSION} -t showminder/showminder:latest .")
    run(f'docker service update --image showminder/showminder:{VERSION} showminder')


@task
def backup():
    """Create a prod database backup."""
    today = date.today().strftime("%Y-%m-%d")
    local(f"pg_dump --host=brain.local --username=showminder --file=showminder_{today}.sql showminder")

