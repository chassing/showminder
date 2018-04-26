
import PTN

from django.conf import settings
from pathlib import Path


def parse_filename(filename):
    for item in Path(filename).parts:
        ptn = PTN.parse(str(item).lower())
        try:
            return settings.MAP_TITLES.get(ptn['title'], ptn['title']), ptn['season'], ptn['episode']
        except KeyError:
            pass
    raise Exception('Cannot parse filename')
