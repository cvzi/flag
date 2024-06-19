import flag


twoletters = {
    "\U0001f1e6\U0001f1eb": "af",
    "\U0001f1e6\U0001f1f1": "al",
    "\U0001f1e9\U0001f1ff": "dz",
    "\U0001f1e6\U0001f1f8": "as",
    "\U0001f1e6\U0001f1e9": "ad",
    "\U0001f1e6\U0001f1f4": "ao",
    "\U0001f1e6\U0001f1ee": "ai",
    "\U0001f1e6\U0001f1f6": "aq",
    "\U0001f1e6\U0001f1ec": "ag",
    "\U0001f1e6\U0001f1f7": "ar",
    "\U0001f1e6\U0001f1f2": "am",
    "\U0001f1e6\U0001f1fc": "aw",
    "\U0001f1e6\U0001f1e8": "ac",
    "\U0001f1e6\U0001f1fa": "au",
    "\U0001f1e6\U0001f1f9": "at",
    "\U0001f1e6\U0001f1ff": "az",
    "\U0001f1e7\U0001f1f8": "bs",
    "\U0001f1e7\U0001f1ed": "bh",
    "\U0001f1e7\U0001f1e9": "bd",
    "\U0001f1e7\U0001f1e7": "bb",
    "\U0001f1e7\U0001f1fe": "by",
    "\U0001f1e7\U0001f1ea": "be",
    "\U0001f1e7\U0001f1ff": "bz",
    "\U0001f1e7\U0001f1ef": "bj",
    "\U0001f1e7\U0001f1f2": "bm",
    "\U0001f1e7\U0001f1f9": "bt",
    "\U0001f1e7\U0001f1f4": "bo",
    "\U0001f1e7\U0001f1e6": "ba",
    "\U0001f1e7\U0001f1fc": "bw",
    "\U0001f1e7\U0001f1fb": "bv",
    "\U0001f1e7\U0001f1f7": "br",
    "\U0001f1ee\U0001f1f4": "io",
    "\U0001f1fb\U0001f1ec": "vg",
    "\U0001f1e7\U0001f1f3": "bn",
    "\U0001f1e7\U0001f1ec": "bg",
    "\U0001f1e7\U0001f1eb": "bf",
    "\U0001f1e7\U0001f1ee": "bi",
    "\U0001f1f0\U0001f1ed": "kh",
    "\U0001f1e8\U0001f1f2": "cm",
    "\U0001f1e8\U0001f1e6": "ca",
    "\U0001f1ee\U0001f1e8": "ic",
    "\U0001f1e8\U0001f1fb": "cv",
    "\U0001f1e7\U0001f1f6": "bq",
    "\U0001f1f0\U0001f1fe": "ky",
    "\U0001f1e8\U0001f1eb": "cf",
    "\U0001f1ea\U0001f1e6": "ea",
    "\U0001f1f9\U0001f1e9": "td",
    "\U0001f1e8\U0001f1f1": "cl",
    "\U0001f1e8\U0001f1f3": "cn",
    "\U0001f1e8\U0001f1fd": "cx",
    "\U0001f1e8\U0001f1f5": "cp",
    "\U0001f1e8\U0001f1e8": "cc",
    "\U0001f1e8\U0001f1f4": "co",
    "\U0001f1f0\U0001f1f2": "km",
    "\U0001f1e8\U0001f1ec": "cg",
    "\U0001f1e8\U0001f1e9": "cd",
    "\U0001f1e8\U0001f1f0": "ck",
    "\U0001f1e8\U0001f1f7": "cr",
    "\U0001f1ed\U0001f1f7": "hr",
    "\U0001f1e8\U0001f1fa": "cu",
    "\U0001f1e8\U0001f1fc": "cw",
    "\U0001f1e8\U0001f1fe": "cy",
    "\U0001f1e8\U0001f1ff": "cz",
    "\U0001f1e8\U0001f1ee": "ci",
    "\U0001f1e9\U0001f1f0": "dk",
    "\U0001f1e9\U0001f1ec": "dg",
    "\U0001f1e9\U0001f1ef": "dj",
    "\U0001f1e9\U0001f1f2": "dm",
    "\U0001f1e9\U0001f1f4": "do",
    "\U0001f1ea\U0001f1e8": "ec",
    "\U0001f1ea\U0001f1ec": "eg",
    "\U0001f1f8\U0001f1fb": "sv",
    "\U0001f1ec\U0001f1f6": "gq",
    "\U0001f1ea\U0001f1f7": "er",
    "\U0001f1ea\U0001f1ea": "ee",
    "\U0001f1ea\U0001f1f9": "et",
    "\U0001f1ea\U0001f1fa": "eu",
    "\U0001f1eb\U0001f1f0": "fk",
    "\U0001f1eb\U0001f1f4": "fo",
    "\U0001f1eb\U0001f1ef": "fj",
    "\U0001f1eb\U0001f1ee": "fi",
    "\U0001f1eb\U0001f1f7": "fr",
    "\U0001f1ec\U0001f1eb": "gf",
    "\U0001f1f5\U0001f1eb": "pf",
    "\U0001f1f9\U0001f1eb": "tf",
    "\U0001f1ec\U0001f1e6": "ga",
    "\U0001f1ec\U0001f1f2": "gm",
    "\U0001f1ec\U0001f1ea": "ge",
    "\U0001f1e9\U0001f1ea": "de",
    "\U0001f1ec\U0001f1ed": "gh",
    "\U0001f1ec\U0001f1ee": "gi",
    "\U0001f1ec\U0001f1f7": "gr",
    "\U0001f1ec\U0001f1f1": "gl",
    "\U0001f1ec\U0001f1e9": "gd",
    "\U0001f1ec\U0001f1f5": "gp",
    "\U0001f1ec\U0001f1fa": "gu",
    "\U0001f1ec\U0001f1f9": "gt",
    "\U0001f1ec\U0001f1ec": "gg",
    "\U0001f1ec\U0001f1f3": "gn",
    "\U0001f1ec\U0001f1fc": "gw",
    "\U0001f1ec\U0001f1fe": "gy",
    "\U0001f1ed\U0001f1f9": "ht",
    "\U0001f1ed\U0001f1f2": "hm",
    "\U0001f1ed\U0001f1f3": "hn",
    "\U0001f1ed\U0001f1f0": "hk",
    "\U0001f1ed\U0001f1fa": "hu",
    "\U0001f1ee\U0001f1f8": "is",
    "\U0001f1ee\U0001f1f3": "in",
    "\U0001f1ee\U0001f1e9": "id",
    "\U0001f1ee\U0001f1f7": "ir",
    "\U0001f1ee\U0001f1f6": "iq",
    "\U0001f1ee\U0001f1ea": "ie",
    "\U0001f1ee\U0001f1f2": "im",
    "\U0001f1ee\U0001f1f1": "il",
    "\U0001f1ee\U0001f1f9": "it",
    "\U0001f1ef\U0001f1f2": "jm",
    "\U0001f1ef\U0001f1f5": "jp",
    "\U0001f1ef\U0001f1ea": "je",
    "\U0001f1ef\U0001f1f4": "jo",
    "\U0001f1f0\U0001f1ff": "kz",
    "\U0001f1f0\U0001f1ea": "ke",
    "\U0001f1f0\U0001f1ee": "ki",
    "\U0001f1fd\U0001f1f0": "xk",
    "\U0001f1f0\U0001f1fc": "kw",
    "\U0001f1f0\U0001f1ec": "kg",
    "\U0001f1f1\U0001f1e6": "la",
    "\U0001f1f1\U0001f1fb": "lv",
    "\U0001f1f1\U0001f1e7": "lb",
    "\U0001f1f1\U0001f1f8": "ls",
    "\U0001f1f1\U0001f1f7": "lr",
    "\U0001f1f1\U0001f1fe": "ly",
    "\U0001f1f1\U0001f1ee": "li",
    "\U0001f1f1\U0001f1f9": "lt",
    "\U0001f1f1\U0001f1fa": "lu",
    "\U0001f1f2\U0001f1f4": "mo",
    "\U0001f1f2\U0001f1f0": "mk",
    "\U0001f1f2\U0001f1ec": "mg",
    "\U0001f1f2\U0001f1fc": "mw",
    "\U0001f1f2\U0001f1fe": "my",
    "\U0001f1f2\U0001f1fb": "mv",
    "\U0001f1f2\U0001f1f1": "ml",
    "\U0001f1f2\U0001f1f9": "mt",
    "\U0001f1f2\U0001f1ed": "mh",
    "\U0001f1f2\U0001f1f6": "mq",
    "\U0001f1f2\U0001f1f7": "mr",
    "\U0001f1f2\U0001f1fa": "mu",
    "\U0001f1fe\U0001f1f9": "yt",
    "\U0001f1f2\U0001f1fd": "mx",
    "\U0001f1eb\U0001f1f2": "fm",
    "\U0001f1f2\U0001f1e9": "md",
    "\U0001f1f2\U0001f1e8": "mc",
    "\U0001f1f2\U0001f1f3": "mn",
    "\U0001f1f2\U0001f1ea": "me",
    "\U0001f1f2\U0001f1f8": "ms",
    "\U0001f1f2\U0001f1e6": "ma",
    "\U0001f1f2\U0001f1ff": "mz",
    "\U0001f1f2\U0001f1f2": "mm",
    "\U0001f1f3\U0001f1e6": "na",
    "\U0001f1f3\U0001f1f7": "nr",
    "\U0001f1f3\U0001f1f5": "np",
    "\U0001f1f3\U0001f1f1": "nl",
    "\U0001f1f3\U0001f1e8": "nc",
    "\U0001f1f3\U0001f1ff": "nz",
    "\U0001f1f3\U0001f1ee": "ni",
    "\U0001f1f3\U0001f1ea": "ne",
    "\U0001f1f3\U0001f1ec": "ng",
    "\U0001f1f3\U0001f1fa": "nu",
    "\U0001f1f3\U0001f1eb": "nf",
    "\U0001f1f0\U0001f1f5": "kp",
    "\U0001f1f2\U0001f1f5": "mp",
    "\U0001f1f3\U0001f1f4": "no",
    "\U0001f1f4\U0001f1f2": "om",
    "\U0001f1f5\U0001f1f0": "pk",
    "\U0001f1f5\U0001f1fc": "pw",
    "\U0001f1f5\U0001f1f8": "ps",
    "\U0001f1f5\U0001f1e6": "pa",
    "\U0001f1f5\U0001f1ec": "pg",
    "\U0001f1f5\U0001f1fe": "py",
    "\U0001f1f5\U0001f1ea": "pe",
    "\U0001f1f5\U0001f1ed": "ph",
    "\U0001f1f5\U0001f1f3": "pn",
    "\U0001f1f5\U0001f1f1": "pl",
    "\U0001f1f5\U0001f1f9": "pt",
    "\U0001f1f5\U0001f1f7": "pr",
    "\U0001f1f6\U0001f1e6": "qa",
    "\U0001f1f7\U0001f1f4": "ro",
    "\U0001f1f7\U0001f1fa": "ru",
    "\U0001f1f7\U0001f1fc": "rw",
    "\U0001f1f7\U0001f1ea": "re",
    "\U0001f1fc\U0001f1f8": "ws",
    "\U0001f1f8\U0001f1f2": "sm",
    "\U0001f1f8\U0001f1e6": "sa",
    "\U0001f1f8\U0001f1f3": "sn",
    "\U0001f1f7\U0001f1f8": "rs",
    "\U0001f1f8\U0001f1e8": "sc",
    "\U0001f1f8\U0001f1f1": "sl",
    "\U0001f1f8\U0001f1ec": "sg",
    "\U0001f1f8\U0001f1fd": "sx",
    "\U0001f1f8\U0001f1f0": "sk",
    "\U0001f1f8\U0001f1ee": "si",
    "\U0001f1f8\U0001f1e7": "sb",
    "\U0001f1f8\U0001f1f4": "so",
    "\U0001f1ff\U0001f1e6": "za",
    "\U0001f1ec\U0001f1f8": "gs",
    "\U0001f1f0\U0001f1f7": "kr",
    "\U0001f1f8\U0001f1f8": "ss",
    "\U0001f1ea\U0001f1f8": "es",
    "\U0001f1f1\U0001f1f0": "lk",
    "\U0001f1e7\U0001f1f1": "bl",
    "\U0001f1f8\U0001f1ed": "sh",
    "\U0001f1f0\U0001f1f3": "kn",
    "\U0001f1f1\U0001f1e8": "lc",
    "\U0001f1f2\U0001f1eb": "mf",
    "\U0001f1f5\U0001f1f2": "pm",
    "\U0001f1fb\U0001f1e8": "vc",
    "\U0001f1f8\U0001f1e9": "sd",
    "\U0001f1f8\U0001f1f7": "sr",
    "\U0001f1f8\U0001f1ef": "sj",
    "\U0001f1f8\U0001f1ff": "sz",
    "\U0001f1f8\U0001f1ea": "se",
    "\U0001f1e8\U0001f1ed": "ch",
    "\U0001f1f8\U0001f1fe": "sy",
    "\U0001f1f8\U0001f1f9": "st",
    "\U0001f1f9\U0001f1fc": "tw",
    "\U0001f1f9\U0001f1ef": "tj",
    "\U0001f1f9\U0001f1ff": "tz",
    "\U0001f1f9\U0001f1ed": "th",
    "\U0001f1f9\U0001f1f1": "tl",
    "\U0001f1f9\U0001f1ec": "tg",
    "\U0001f1f9\U0001f1f0": "tk",
    "\U0001f1f9\U0001f1f4": "to",
    "\U0001f1f9\U0001f1f9": "tt",
    "\U0001f1f9\U0001f1e6": "ta",
    "\U0001f1f9\U0001f1f3": "tn",
    "\U0001f1f9\U0001f1f7": "tr",
    "\U0001f1f9\U0001f1f2": "tm",
    "\U0001f1f9\U0001f1e8": "tc",
    "\U0001f1f9\U0001f1fb": "tv",
    "\U0001f1fa\U0001f1f2": "um",
    "\U0001f1fb\U0001f1ee": "vi",
    "\U0001f1fa\U0001f1ec": "ug",
    "\U0001f1fa\U0001f1e6": "ua",
    "\U0001f1e6\U0001f1ea": "ae",
    "\U0001f1ec\U0001f1e7": "gb",
    "\U0001f1fa\U0001f1f8": "us",
    "\U0001f1fa\U0001f1fe": "uy",
    "\U0001f1fa\U0001f1ff": "uz",
    "\U0001f1fb\U0001f1fa": "vu",
    "\U0001f1fb\U0001f1e6": "va",
    "\U0001f1fb\U0001f1ea": "ve",
    "\U0001f1fb\U0001f1f3": "vn",
    "\U0001f1fc\U0001f1eb": "wf",
    "\U0001f1ea\U0001f1ed": "eh",
    "\U0001f1fe\U0001f1ea": "ye",
    "\U0001f1ff\U0001f1f2": "zm",
    "\U0001f1ff\U0001f1fc": "zw",
    "\U0001f1e6\U0001f1fd": "ax",
    "\U0001f1fa\U0001f1f3": "un",
}

moreletters = {
    "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": "gbeng",
    "\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f": "gbwls",
    "\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f": "gbsct",
}


def test_example():
    assert (
        "🇩🇪"
        == flag.flag(":DE:")
        == flag.flag("DE")
        == flag.flag("de")
        == flag.flag(":de:")
    )
    assert (
        "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f"
        == flag.flag(":GBENG:")
        == flag.flag("GBENG")
        == flag.flag("gbeng")
        == flag.flag(":gbeng:")
    )
    assert (
        "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f"
        == flag.flag(":GB-ENG:")
        == flag.flag("GB-ENG")
        == flag.flag("gb-eng")
        == flag.flag(":gb-eng:")
    )


def raisesException(func, ExceptionClass):
    try:
        func()
    except ExceptionClass as e:
        print(e)
        return True
    return False


def test_exception():
    assert raisesException(lambda: flag.flag(""), ValueError)
    assert raisesException(lambda: flag.flag(":-:"), ValueError)
    assert raisesException(lambda: flag.flag(":a:"), ValueError)
    assert raisesException(lambda: flag.flag("abcdefg"), ValueError)


def test_twoletter():
    for code, value in twoletters.items():
        x = flag.flag(value)
        assert code == x

        y = flag.flag(":%s:" % value)
        assert code == y

        z = flag.flag(value.upper())
        assert code == z


def test_moreletters():
    for code, value in moreletters.items():
        a = flag.flag(value)
        assert code == a

        b = flag.flag(":%s:" % value)
        assert code == b

        c = flag.flag(":%s%s-%s:" % (value[0], value[1], value[2:]))
        assert code == c

        d = flag.flag(value.upper())
        assert code == d
