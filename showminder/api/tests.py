
import pytest

from .utils import parse_filename


@pytest.mark.parametrize(
    "filename, title, season, episode",
    [
        (
            "smb:///path/to/movie/Sneaky.Pete/Sneaky.Pete.S02E10.German.DL.DUBBED.720p.WebHD.x264-AIDA.mkv",
            "sneaky pete",
            2,
            10,
        ),
        ("smb:///path/to/movie/Room 104/Room.104-s01e12.mkv", "room 104", 1, 12),
        (
            "smb:///path/to/movie/Santa.Clarita/santa.clarita.diet.s02e05.german.dubbed.dl.1080p.web.x264-bigint.mkv",
            "santa clarita diet",
            2,
            5,
        ),
        (
            "smb:///path/to/movie/Frequency/Frequency.S01E13.Signalverlust.German.Dubbed.DL.1080p.AmazonHD.x264-GDR.mkv",
            "frequency",
            1,
            13,
        ),
        (
            "smb:///path/to/movie/Frequency/Frequency.S01E11.Eine.Tat.loescht.die.andere.German.Dubbed.DL.1080p.AmazonHD.x264-GDR.mkv",
            "frequency",
            1,
            11,
        ),
        (
            "smb:///path/to/movie/Lost.in.Space/lost.in.space.2018.s01e07.german.dubbed.dl.1080p.web.x264.internal-bigint.mkv",
            "lost in space",
            1,
            7,
        ),
        (
            "smb:///path/to/movie/Black.Lightning.S01E03.LaWanda.Das.Buch.des.Todes.German.DD51.DL.1080p.NetflixHD.x264-TVS/Black.Lightning.S01E03-bl-dd51-dl-18p-nfhd-x264-103.mkv",
            "black lightning",
            1,
            3,
        ),
        (
            "smb:///path/to/movie/The.Last.Man.On.Earth/The.Last.Man.On.Earth.S03E06.Ich.habe.eine.Nachricht.hinterlassen.German.DL.Dubbed.720p.Web-DL.h264-GDR.mkv",
            "the last man on earth",
            3,
            6,
        ),
        (
            "smb:///path/to/movie/Shades.of.Blue.S02E04.Toechter.des.Boesen.German.DD51.Dubbed.DL.1080p.AmazonHD.x264-TVS/Shades.of.blue.S02E04.ded-dl-18p-azhd-x264-204.mkv",
            "shades of blue",
            2,
            4,
        ),
        (
            "smb:///path/to/movie/Black.Lightning.S01E06.German.Dubbed.DL.720p.WEB.x264-BiGiNT/black.lightning.s01e06.german.dubbed.dl.720p.web.x264-bigint.mkv",
            "black lightning",
            1,
            6,
        ),
        (
            "smb:///path/to/movie/Atlanta.S02E05.Fastnacht.German.DD51.Dubbed.DL.1080p.AmazonHD.h264-GDR.mkv",
            "atlanta",
            2,
            5,
        ),
        ("smb:///path/to/movie/StartUp/startup.s02e08.dd51-dl-7p-azhd-x264-208.mkv", "startup", 2, 8),
        # 1080 vs 720
        ("smb:///path/to/movie/blacklist/the.blacklist.s05e04-1080p.mkv", "the blacklist", 5, 4),
        ("smb:///path/to/movie/blacklist/the.blacklist.s05e09-720p.mkv", "the blacklist", 5, 9),
        # season dir
        (
            "smb:///path/to/movie/Damnation.S01.Complete.German.DD51.DL.1080p.NetflixHD.x264-TVS/damnation.s1e09.dd51-dl-18p-nfhd-x264-109.mkv",
            "damnation",
            1,
            9,
        ),
        (
            "smb:///path/to/movie/The.Alienist.S01.Complete.German.DD51.DL.1080p.NetflixHD.x264-TVS/the.alienist.s01e03.dd51.dl.18p.nfhd.x264.103.mkv",
            "the alienist",
            1,
            3,
        ),
        # info in dirname
        (
            "smb:///path/to/movie/Shameless.S08E08.Franks.Northern.Southern.Express.GERMAN.DUBBED.DL.1080p.WebHD.x264-TVP/tvp-shameless-s08e08-1080p.mkv",
            "shameless",
            8,
            8,
        ),
        (
            "smb:///path/to/movie/Imposters.S01E01.Sie.ist.weg.German.1080p.HDTV.x264-ATAX/atax-imposters.s01e01-1080p.mkv",
            "imposters",
            1,
            1,
        ),
        (
            "smb:///path/to/movie/Black.Lightning.S01E06.German.Dubbed.DL.720p.WEB.x264-BiGiNT/fff.mkv",
            "black lightning",
            1,
            6,
        ),
        # special mapping
        ("smb:///path/to/movie/S.W.A.T.s05e09-720p.mkv", "swat", 5, 9),
        (
            "smb:///path/to/movie/S.W.A.T.S01E01.Sie.ist.weg.German.1080p.HDTV.x264-ATAX/atax-s.w.a.t-s01e01-1080p.mkv",
            "swat",
            1,
            1,
        ),
        pytest.param(
            "smb:///path/to/movie/Die.Verlegerin.2017.German.AC3MD.DL.1080p.BluRay.x264-iND/verlegerin-1080.mkv",
            "Die Verlegerin",
            1,
            1,
            marks=pytest.mark.xfail,
        ),
    ],
)
def test_parse_filename(filename, title, season, episode):
    assert parse_filename(filename) == (title, season, episode)
