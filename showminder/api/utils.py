
import PTN

from os.path import basename


def parse_filename(filename):
    ptn = PTN.parse(basename(filename))
    return ptn['title'], ptn['season'], ptn['episode']
