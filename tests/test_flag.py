# -*- coding: UTF-8 -*-


import sys
import distutils.version

try:
    import flag
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    import flag
    print("Imported flag from %s" % os.path.abspath(os.path.join(include, "flag")))



import emoji
if distutils.version.StrictVersion(emoji.__version__) < distutils.version.StrictVersion('0.5.0'): # pragma: nocover
    raise ImportError("emoji module version < 0.5.0", "Module/Package `emoji` is version %s, it needs to be at least version 0.5.0" % emoji.__version__) # pragma: nocover


allcodes = {
    u"\U0001f1e6\U0001f1eb" : "af",
    u"\U0001f1e6\U0001f1f1" : "al",
    u"\U0001f1e9\U0001f1ff" : "dz",
    u"\U0001f1e6\U0001f1f8" : "as",
    u"\U0001f1e6\U0001f1e9" : "ad",
    u"\U0001f1e6\U0001f1f4" : "ao",
    u"\U0001f1e6\U0001f1ee" : "ai",
    u"\U0001f1e6\U0001f1f6" : "aq",
    u"\U0001f1e6\U0001f1ec" : "ag",
    u"\U0001f1e6\U0001f1f7" : "ar",
    u"\U0001f1e6\U0001f1f2" : "am",
    u"\U0001f1e6\U0001f1fc" : "aw",
    u"\U0001f1e6\U0001f1e8" : "ac",
    u"\U0001f1e6\U0001f1fa" : "au",
    u"\U0001f1e6\U0001f1f9" : "at",
    u"\U0001f1e6\U0001f1ff" : "az",
    u"\U0001f1e7\U0001f1f8" : "bs",
    u"\U0001f1e7\U0001f1ed" : "bh",
    u"\U0001f1e7\U0001f1e9" : "bd",
    u"\U0001f1e7\U0001f1e7" : "bb",
    u"\U0001f1e7\U0001f1fe" : "by",
    u"\U0001f1e7\U0001f1ea" : "be",
    u"\U0001f1e7\U0001f1ff" : "bz",
    u"\U0001f1e7\U0001f1ef" : "bj",
    u"\U0001f1e7\U0001f1f2" : "bm",
    u"\U0001f1e7\U0001f1f9" : "bt",
    u"\U0001f1e7\U0001f1f4" : "bo",
    u"\U0001f1e7\U0001f1e6" : "ba",
    u"\U0001f1e7\U0001f1fc" : "bw",
    u"\U0001f1e7\U0001f1fb" : "bv",
    u"\U0001f1e7\U0001f1f7" : "br",
    u"\U0001f1ee\U0001f1f4" : "io",
    u"\U0001f1fb\U0001f1ec" : "vg",
    u"\U0001f1e7\U0001f1f3" : "bn",
    u"\U0001f1e7\U0001f1ec" : "bg",
    u"\U0001f1e7\U0001f1eb" : "bf",
    u"\U0001f1e7\U0001f1ee" : "bi",
    u"\U0001f1f0\U0001f1ed" : "kh",
    u"\U0001f1e8\U0001f1f2" : "cm",
    u"\U0001f1e8\U0001f1e6" : "ca",
    u"\U0001f1ee\U0001f1e8" : "ic",
    u"\U0001f1e8\U0001f1fb" : "cv",
    u"\U0001f1e7\U0001f1f6" : "bq",
    u"\U0001f1f0\U0001f1fe" : "ky",
    u"\U0001f1e8\U0001f1eb" : "cf",
    u"\U0001f1ea\U0001f1e6" : "ea",
    u"\U0001f1f9\U0001f1e9" : "td",
    u"\U0001f1e8\U0001f1f1" : "cl",
    u"\U0001f1e8\U0001f1f3" : "cn",
    u"\U0001f1e8\U0001f1fd" : "cx",
    u"\U0001f1e8\U0001f1f5" : "cp",
    u"\U0001f1e8\U0001f1e8" : "cc",
    u"\U0001f1e8\U0001f1f4" : "co",
    u"\U0001f1f0\U0001f1f2" : "km",
    u"\U0001f1e8\U0001f1ec" : "cg",
    u"\U0001f1e8\U0001f1e9" : "cd",
    u"\U0001f1e8\U0001f1f0" : "ck",
    u"\U0001f1e8\U0001f1f7" : "cr",
    u"\U0001f1ed\U0001f1f7" : "hr",
    u"\U0001f1e8\U0001f1fa" : "cu",
    u"\U0001f1e8\U0001f1fc" : "cw",
    u"\U0001f1e8\U0001f1fe" : "cy",
    u"\U0001f1e8\U0001f1ff" : "cz",
    u"\U0001f1e8\U0001f1ee" : "ci",
    u"\U0001f1e9\U0001f1f0" : "dk",
    u"\U0001f1e9\U0001f1ec" : "dg",
    u"\U0001f1e9\U0001f1ef" : "dj",
    u"\U0001f1e9\U0001f1f2" : "dm",
    u"\U0001f1e9\U0001f1f4" : "do",
    u"\U0001f1ea\U0001f1e8" : "ec",
    u"\U0001f1ea\U0001f1ec" : "eg",
    u"\U0001f1f8\U0001f1fb" : "sv",
    u"\U0001f1ec\U0001f1f6" : "gq",
    u"\U0001f1ea\U0001f1f7" : "er",
    u"\U0001f1ea\U0001f1ea" : "ee",
    u"\U0001f1ea\U0001f1f9" : "et",
    u"\U0001f1ea\U0001f1fa" : "eu",
    u"\U0001f1eb\U0001f1f0" : "fk",
    u"\U0001f1eb\U0001f1f4" : "fo",
    u"\U0001f1eb\U0001f1ef" : "fj",
    u"\U0001f1eb\U0001f1ee" : "fi",
    u"\U0001f1eb\U0001f1f7" : "fr",
    u"\U0001f1ec\U0001f1eb" : "gf",
    u"\U0001f1f5\U0001f1eb" : "pf",
    u"\U0001f1f9\U0001f1eb" : "tf",
    u"\U0001f1ec\U0001f1e6" : "ga",
    u"\U0001f1ec\U0001f1f2" : "gm",
    u"\U0001f1ec\U0001f1ea" : "ge",
    u"\U0001f1e9\U0001f1ea" : "de",
    u"\U0001f1ec\U0001f1ed" : "gh",
    u"\U0001f1ec\U0001f1ee" : "gi",
    u"\U0001f1ec\U0001f1f7" : "gr",
    u"\U0001f1ec\U0001f1f1" : "gl",
    u"\U0001f1ec\U0001f1e9" : "gd",
    u"\U0001f1ec\U0001f1f5" : "gp",
    u"\U0001f1ec\U0001f1fa" : "gu",
    u"\U0001f1ec\U0001f1f9" : "gt",
    u"\U0001f1ec\U0001f1ec" : "gg",
    u"\U0001f1ec\U0001f1f3" : "gn",
    u"\U0001f1ec\U0001f1fc" : "gw",
    u"\U0001f1ec\U0001f1fe" : "gy",
    u"\U0001f1ed\U0001f1f9" : "ht",
    u"\U0001f1ed\U0001f1f2" : "hm",
    u"\U0001f1ed\U0001f1f3" : "hn",
    u"\U0001f1ed\U0001f1f0" : "hk",
    u"\U0001f1ed\U0001f1fa" : "hu",
    u"\U0001f1ee\U0001f1f8" : "is",
    u"\U0001f1ee\U0001f1f3" : "in",
    u"\U0001f1ee\U0001f1e9" : "id",
    u"\U0001f1ee\U0001f1f7" : "ir",
    u"\U0001f1ee\U0001f1f6" : "iq",
    u"\U0001f1ee\U0001f1ea" : "ie",
    u"\U0001f1ee\U0001f1f2" : "im",
    u"\U0001f1ee\U0001f1f1" : "il",
    u"\U0001f1ee\U0001f1f9" : "it",
    u"\U0001f1ef\U0001f1f2" : "jm",
    u"\U0001f1ef\U0001f1f5" : "jp",
    u"\U0001f1ef\U0001f1ea" : "je",
    u"\U0001f1ef\U0001f1f4" : "jo",
    u"\U0001f1f0\U0001f1ff" : "kz",
    u"\U0001f1f0\U0001f1ea" : "ke",
    u"\U0001f1f0\U0001f1ee" : "ki",
    u"\U0001f1fd\U0001f1f0" : "xk",
    u"\U0001f1f0\U0001f1fc" : "kw",
    u"\U0001f1f0\U0001f1ec" : "kg",
    u"\U0001f1f1\U0001f1e6" : "la",
    u"\U0001f1f1\U0001f1fb" : "lv",
    u"\U0001f1f1\U0001f1e7" : "lb",
    u"\U0001f1f1\U0001f1f8" : "ls",
    u"\U0001f1f1\U0001f1f7" : "lr",
    u"\U0001f1f1\U0001f1fe" : "ly",
    u"\U0001f1f1\U0001f1ee" : "li",
    u"\U0001f1f1\U0001f1f9" : "lt",
    u"\U0001f1f1\U0001f1fa" : "lu",
    u"\U0001f1f2\U0001f1f4" : "mo",
    u"\U0001f1f2\U0001f1f0" : "mk",
    u"\U0001f1f2\U0001f1ec" : "mg",
    u"\U0001f1f2\U0001f1fc" : "mw",
    u"\U0001f1f2\U0001f1fe" : "my",
    u"\U0001f1f2\U0001f1fb" : "mv",
    u"\U0001f1f2\U0001f1f1" : "ml",
    u"\U0001f1f2\U0001f1f9" : "mt",
    u"\U0001f1f2\U0001f1ed" : "mh",
    u"\U0001f1f2\U0001f1f6" : "mq",
    u"\U0001f1f2\U0001f1f7" : "mr",
    u"\U0001f1f2\U0001f1fa" : "mu",
    u"\U0001f1fe\U0001f1f9" : "yt",
    u"\U0001f1f2\U0001f1fd" : "mx",
    u"\U0001f1eb\U0001f1f2" : "fm",
    u"\U0001f1f2\U0001f1e9" : "md",
    u"\U0001f1f2\U0001f1e8" : "mc",
    u"\U0001f1f2\U0001f1f3" : "mn",
    u"\U0001f1f2\U0001f1ea" : "me",
    u"\U0001f1f2\U0001f1f8" : "ms",
    u"\U0001f1f2\U0001f1e6" : "ma",
    u"\U0001f1f2\U0001f1ff" : "mz",
    u"\U0001f1f2\U0001f1f2" : "mm",
    u"\U0001f1f3\U0001f1e6" : "na",
    u"\U0001f1f3\U0001f1f7" : "nr",
    u"\U0001f1f3\U0001f1f5" : "np",
    u"\U0001f1f3\U0001f1f1" : "nl",
    u"\U0001f1f3\U0001f1e8" : "nc",
    u"\U0001f1f3\U0001f1ff" : "nz",
    u"\U0001f1f3\U0001f1ee" : "ni",
    u"\U0001f1f3\U0001f1ea" : "ne",
    u"\U0001f1f3\U0001f1ec" : "ng",
    u"\U0001f1f3\U0001f1fa" : "nu",
    u"\U0001f1f3\U0001f1eb" : "nf",
    u"\U0001f1f0\U0001f1f5" : "kp",
    u"\U0001f1f2\U0001f1f5" : "mp",
    u"\U0001f1f3\U0001f1f4" : "no",
    u"\U0001f1f4\U0001f1f2" : "om",
    u"\U0001f1f5\U0001f1f0" : "pk",
    u"\U0001f1f5\U0001f1fc" : "pw",
    u"\U0001f1f5\U0001f1f8" : "ps",
    u"\U0001f1f5\U0001f1e6" : "pa",
    u"\U0001f1f5\U0001f1ec" : "pg",
    u"\U0001f1f5\U0001f1fe" : "py",
    u"\U0001f1f5\U0001f1ea" : "pe",
    u"\U0001f1f5\U0001f1ed" : "ph",
    u"\U0001f1f5\U0001f1f3" : "pn",
    u"\U0001f1f5\U0001f1f1" : "pl",
    u"\U0001f1f5\U0001f1f9" : "pt",
    u"\U0001f1f5\U0001f1f7" : "pr",
    u"\U0001f1f6\U0001f1e6" : "qa",
    u"\U0001f1f7\U0001f1f4" : "ro",
    u"\U0001f1f7\U0001f1fa" : "ru",
    u"\U0001f1f7\U0001f1fc" : "rw",
    u"\U0001f1f7\U0001f1ea" : "re",
    u"\U0001f1fc\U0001f1f8" : "ws",
    u"\U0001f1f8\U0001f1f2" : "sm",
    u"\U0001f1f8\U0001f1e6" : "sa",
    u"\U0001f1f8\U0001f1f3" : "sn",
    u"\U0001f1f7\U0001f1f8" : "rs",
    u"\U0001f1f8\U0001f1e8" : "sc",
    u"\U0001f1f8\U0001f1f1" : "sl",
    u"\U0001f1f8\U0001f1ec" : "sg",
    u"\U0001f1f8\U0001f1fd" : "sx",
    u"\U0001f1f8\U0001f1f0" : "sk",
    u"\U0001f1f8\U0001f1ee" : "si",
    u"\U0001f1f8\U0001f1e7" : "sb",
    u"\U0001f1f8\U0001f1f4" : "so",
    u"\U0001f1ff\U0001f1e6" : "za",
    u"\U0001f1ec\U0001f1f8" : "gs",
    u"\U0001f1f0\U0001f1f7" : "kr",
    u"\U0001f1f8\U0001f1f8" : "ss",
    u"\U0001f1ea\U0001f1f8" : "es",
    u"\U0001f1f1\U0001f1f0" : "lk",
    u"\U0001f1e7\U0001f1f1" : "bl",
    u"\U0001f1f8\U0001f1ed" : "sh",
    u"\U0001f1f0\U0001f1f3" : "kn",
    u"\U0001f1f1\U0001f1e8" : "lc",
    u"\U0001f1f2\U0001f1eb" : "mf",
    u"\U0001f1f5\U0001f1f2" : "pm",
    u"\U0001f1fb\U0001f1e8" : "vc",
    u"\U0001f1f8\U0001f1e9" : "sd",
    u"\U0001f1f8\U0001f1f7" : "sr",
    u"\U0001f1f8\U0001f1ef" : "sj",
    u"\U0001f1f8\U0001f1ff" : "sz",
    u"\U0001f1f8\U0001f1ea" : "se",
    u"\U0001f1e8\U0001f1ed" : "ch",
    u"\U0001f1f8\U0001f1fe" : "sy",
    u"\U0001f1f8\U0001f1f9" : "st",
    u"\U0001f1f9\U0001f1fc" : "tw",
    u"\U0001f1f9\U0001f1ef" : "tj",
    u"\U0001f1f9\U0001f1ff" : "tz",
    u"\U0001f1f9\U0001f1ed" : "th",
    u"\U0001f1f9\U0001f1f1" : "tl",
    u"\U0001f1f9\U0001f1ec" : "tg",
    u"\U0001f1f9\U0001f1f0" : "tk",
    u"\U0001f1f9\U0001f1f4" : "to",
    u"\U0001f1f9\U0001f1f9" : "tt",
    u"\U0001f1f9\U0001f1e6" : "ta",
    u"\U0001f1f9\U0001f1f3" : "tn",
    u"\U0001f1f9\U0001f1f7" : "tr",
    u"\U0001f1f9\U0001f1f2" : "tm",
    u"\U0001f1f9\U0001f1e8" : "tc",
    u"\U0001f1f9\U0001f1fb" : "tv",
    u"\U0001f1fa\U0001f1f2" : "um",
    u"\U0001f1fb\U0001f1ee" : "vi",
    u"\U0001f1fa\U0001f1ec" : "ug",
    u"\U0001f1fa\U0001f1e6" : "ua",
    u"\U0001f1e6\U0001f1ea" : "ae",
    u"\U0001f1ec\U0001f1e7" : "gb",
    u"\U0001f1fa\U0001f1f8" : "us",
    u"\U0001f1fa\U0001f1fe" : "uy",
    u"\U0001f1fa\U0001f1ff" : "uz",
    u"\U0001f1fb\U0001f1fa" : "vu",
    u"\U0001f1fb\U0001f1e6" : "va",
    u"\U0001f1fb\U0001f1ea" : "ve",
    u"\U0001f1fb\U0001f1f3" : "vn",
    u"\U0001f1fc\U0001f1eb" : "wf",
    u"\U0001f1ea\U0001f1ed" : "eh",
    u"\U0001f1fe\U0001f1ea" : "ye",
    u"\U0001f1ff\U0001f1f2" : "zm",
    u"\U0001f1ff\U0001f1fc" : "zw",
    u"\U0001f1e6\U0001f1fd" : "ax",
    u"\U0001f1fa\U0001f1f3" : "un"
    }

wrongcodes = [
    u"\U0001f1dd\U0001f1eb",
    u"\U0001f1de\U0001f1f1",
    u"\U0001f1df\U0001f1ff",
    u"\U0001f1e0\U0001f1f8",
    u"\U0001f1e1\U0001f1e9",
    u"\U0001f1e2\U0001f1f4",
    u"\U0001f1e3\U0001f1ee",
    u"\U0001f1e4\U0001f1f6",
    u"\U0001f1e5\U0001f1ec",

    u"\U0001f1e6\U0001f1e4",
    u"\U0001f1e6\U0001f1e5",

    u"\U0001f200\U0001f1eb",
    u"\U0001f1eb\U0001f200",
    ]


def test_example():
    assert u"🇩🇪" == flag.flagize(":DE:")

    assert ":DE:" == flag.dflagize(u"🇩🇪")

    assert u"Inline🇪🇸test" == flag.flagize("Inline:ES:test")

    assert "Inline:ES:test" == flag.dflagize(u"Inline🇪🇸test")

    assert u"Other🇳🇷unicode👍test" == flag.flagize(u"Other:NR:unicode👍test")

    assert u"Other:NR:unicode👍test" == flag.dflagize(u"Other🇳🇷unicode👍test")

    assert u"❤️🇮🇱✡️" == flag.flagize(u"❤️:IL:✡️")

    assert u"❤️:IL:✡️" == flag.dflagize(u"❤️🇮🇱✡️")

def test_all_known():
    for code in allcodes.keys():
        x = flag.dflagize(code)
        assert len(x) == 4
        assert x[0] == ":"
        assert x[-1] == ":"

def test_check_known():
    for code, value in allcodes.items():
        twoletter = ":%s:" % value.upper()

        x = flag.dflagize(code)
        y = flag.flagize(twoletter)
        z = flag.dflagize(y)

        assert x == twoletter
        assert y == code
        assert x == z

def test_compare_with_emoji_module():
    for code, value in allcodes.items():
        twoletter = ":%s:" % value.upper()

        x = flag.flagize(twoletter)

        assert not x.startswith(":")

        y = emoji.demojize(x)

        assert y.startswith(":")

def test_wrong_codes():
    for code in wrongcodes:

        x = flag.dflagize(code)

        assert code == x


def runall():
    for fname, f in list(globals().items()):
        if fname.startswith('test_'):
            print("%s()" % fname)
            f()
            print("Ok.")




if __name__ == '__main__':
    if 'idlelib' in sys.modules:
        print("Please run this file in a console!")

    runall()
