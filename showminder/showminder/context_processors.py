import os


def version(args):
    return {"VERSION": os.environ.get("SHOWMINDER_VERSION", "Dev")}
