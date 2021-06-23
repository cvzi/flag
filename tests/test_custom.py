# -*- coding: UTF-8 -*-


import sys
import warnings

try:
    import flag
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    import flag
    print("Imported flag from %s" % os.path.abspath(os.path.join(include, "flag")))


def test_custom_simple():
    for a, b in [("🇧", "🇧"), ("🇩🇪", "🇩🇪"), ("DE", "DE"), ("A", "B"), ("1", "2"), ("#", "#"), (".", "."), ("-", "z"), ("0", "123"), ("\U0001F3F4", "\U0001F3F4")]:
        f = flag.Flag(a, b, warn=False)

        assert f.flag(":il-") == "🇮🇱"

        assert "🇩🇪" == f.flagize("%sDE%s" % (a, b))

        assert "%sDE%s" % (a, b) == f.dflagize("🇩🇪")

        assert "🇩🇪🇧" == f.flagize("%sDE%s🇧" % (a, b))
        assert "%sDE%s🇧" % (a, b) == f.dflagize("🇩🇪🇧")

        assert "Inline🇪🇸test" == f.flagize("Inline%sES%stest" % (a, b))

        assert "Inline%sES%stest" % (a, b) == f.dflagize("Inline🇪🇸test")

        assert "Other🇳🇷unicode👍test" == f.flagize("Other%sNR%sunicode👍test" % (a, b))

        assert "Other%sNR%sunicode👍test" % (a, b) == f.dflagize("Other🇳🇷unicode👍test")

        assert "❤️🇮🇱✡️" == f.flagize("❤️%sIL%s✡️" % (a, b))

        assert "❤️%sIL%s✡️" % (a, b) == f.dflagize("❤️🇮🇱✡️")

        assert "❤️🇮🇱🇩🇪✡️" == f.flagize("❤️%sIL%s%sDE%s✡️" % (a, b, a, b))

        assert "❤️%sIL%s%sDE%s✡️" % (a, b, a, b) == f.dflagize("❤️🇮🇱🇩🇪✡️")

        assert "❤️\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️" == f.flagize("❤️%sgb-eng%s✡️" % (a, b), subregions=True)

        assert "❤️%sgb-eng%s✡️" % (a, b) == f.dflagize("❤️\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️", subregions=True)

        assert "❤️A\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️" == f.flagize("❤️A%sgb-eng%s✡️" % (a, b), subregions=True)

        assert "❤️A%sgb-eng%s✡️" % (a, b) == f.dflagize("❤️A\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️", subregions=True)
        
        assert "❤️0\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f1✡️" == f.flagize("❤️0%sgb-eng%s1✡️" % (a, b), subregions=True)

        assert "❤️0%sgb-eng%s1✡️" % (a, b) == f.dflagize("❤️0\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f1✡️", subregions=True)
        
        assert "❤️a\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️" == f.flagize("❤️a%sgb-eng%s✡️" % (a, b), subregions=True)

        assert "❤️a%sgb-eng%s✡️" % (a, b) == f.dflagize("❤️a\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️", subregions=True)

def test_warnings():
    for args in [("-", "-"), ("a", "b"), ("abc", "012"), ("345", "AbC"), ("", )]:
        f = flag.Flag(*args)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.flagize("️🇮🇱", subregions=True)

        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)
        assert "subregional" in str(w[-1].message)

        f = flag.Flag(*args)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.flagize_subregional("️🇮🇱")

        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)
        assert "subregional" in str(w[-1].message)

    for args in [("", "-"), ("", "b"), ("", "012"), ("", "AbC")]:
        f = flag.Flag(*args)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.flagize("️🇮🇱", subregions=True)
            f.flagize("️🇮🇱", subregions=True)
            f.flagize("️🇮🇱", subregions=True)
            f.flagize_subregional("️🇮🇱")
            f.flagize_subregional("️🇮🇱")

        assert len(w) == 2
        assert issubclass(w[-1].category, UserWarning)
        assert "subregional" in str(w[-1].message)

    for args in [("-", "-"), ("a", "b"), ("abc", "012"), ("345", "AbC"), ("abc", ), ("987", ), ("abc", )]:
        f = flag.Flag(*args)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.dflagize("️🇮🇱", subregions=True)

        assert len(w) == 0

    for b in ["abcd", "9871"]:
        f = flag.Flag(suffix_str=b)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.dflagize("️🇮🇱", subregions=True)

        assert len(w) == 0


valid_codes = {
    "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": "gb-eng",
    "\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f": "gb-sct",
    "\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f": "gb-wls",
}

def test_custom_subregions():
    for a, b in [("🇧", "🇧"), ("DE", "DE"), ("-", "b-"), ("-", "auto"), ("ab", "0123"), ("#", "#"), (".", "."), ("0", "123"), ("\U0001F3F4", "\U0001F3F4")]:
        f = flag.Flag(a, b, warn=False)

        for emoji, ascii in valid_codes.items():

            assert emoji == f.flagize("%s%s%s" % (a, ascii, b), subregions=True)

            assert "%s%s%s" % (a, ascii, b) == f.dflagize(emoji, subregions=True)

            assert a + emoji + b == f.flagize("%s%s%s%s%s" % (a, a, ascii, b, b), subregions=True)

            assert "%s%s%s%s%s" % (a, a, ascii, b, b) == f.dflagize(a + emoji + b, subregions=True)

            assert b + emoji + a == f.flagize("%s%s%s%s%s" % (b, a, ascii, b, a), subregions=True)

            assert "%s%s%s%s%s" % (b, a, ascii, b, a) == f.dflagize(b + emoji + a, subregions=True)


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
