# -*- coding: UTF-8 -*-


import sys

try:
    import flag
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    import flag
    print("Imported flag from %s" % os.path.abspath(os.path.join(include, "flag")))


import emoji


basic = {

    u"\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": ":gb-eng:",
    # Black flag+Flag of England:
    u"\U0001f3f4\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": u"\U0001f3f4:gb-eng:",
    # Flag of England+Black flag:
    u"\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U0001f3f4": u":gb-eng:\U0001f3f4",
    # Black flag+Flag of England+Black flag:
    u"\U0001f3f4\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U0001f3f4": u"\U0001f3f4:gb-eng:\U0001f3f4",
    # White flag+Flag of England:
    u"\U0001f3f3\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": u"\U0001f3f3:gb-eng:",
    # Inline tests:
    u"Test inline \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": "Test inline :gb-eng:",
    u"\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f Test inline": ":gb-eng: Test inline",
    u"before \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f after": "before :gb-eng: after",
    u"before \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f after": "before :gb-eng::gb-eng: after",
    u"before \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f after": "before :gb-eng: :gb-eng: after",
    u"before \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\n\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f after": "before :gb-eng:\n:gb-eng: after",
}

basic_mixed = {
    u"\U0001f1e8\U0001f1eb\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": ":CF::gb-eng:",
    u"\U0001f1e8\U0001f1eb \U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": ":CF: :gb-eng:",
    u"\U0001f1e8\U0001f1eb\n\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": ":CF:\n:gb-eng:",
    u"👍\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f": u"👍:gb-sct:",
    u"👍\n\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f👍": u"👍\n:gb-wls:👍",
    u"\U0001f3f4\U000e0066\U000e0072\U000e006e\U000e006f\U000e0072\U000e007f👍👍": u":fr-nor:👍👍",
    u"\U0001f6a8\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f": u"\U0001f6a8:gb-sct:",
    u"Inline Iceland \U0001f3f4\U000e0069\U000e0073\U000e0034\U000e007f with ümlaut": u"Inline Iceland :is-4: with ümlaut",
    u"🏎\U0001f3f4\U000e0030\U000e0031\U000e0039\U000e007f🏎": u"🏎:01-9:🏎",
    u"❤️🇮🇱✡️\U0001f3f4\U000e0069\U000e006c\U000e006a\U000e006d\U000e007f": u"❤️:IL:✡️:il-jm:",
}

valid_codes = {
    u"\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": "gb-eng",  # RGI
    u"\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f": "gb-sct",  # RGI
    u"\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f": "gb-wls",  # RGI

    # Ontario:
    u"\U0001f3f4\U000e0063\U000e0061\U000e006f\U000e006e\U000e007f": "ca-on",
    # Normandy:
    u"\U0001f3f4\U000e0066\U000e0072\U000e006e\U000e006f\U000e0072\U000e007f": "fr-nor",
    # Saint George Parish, Antigua and Barbuda:
    u"\U0001f3f4\U000e0061\U000e0067\U000e0030\U000e0033\U000e007f": "ag-03",
    # Benguela in Angola:
    u"\U0001f3f4\U000e0061\U000e006f\U000e0062\U000e0067\U000e0075\U000e007f": "ao-bgu",

    # Ardennes:
    u"\U0001f3f4\U000e0066\U000e0072\U000e0030\U000e0038\U000e007f": "fr-08",
    # Limón, Costa Rica:
    u"\U0001f3f4\U000e0063\U000e0072\U000e006c\U000e007f": "cr-l",
    # Zambezia, Mozambique:
    u"\U0001f3f4\U000e006d\U000e007a\U000e0071\U000e007f": "mz-q",
    # Westfjords, Iceland:
    u"\U0001f3f4\U000e0069\U000e0073\U000e0034\U000e007f": "is-4",

    # 3-digit unicode_region_subtag for World
    u"\U0001f3f4\U000e0030\U000e0030\U000e0031\U000e007f": "00-1",
    # 3-digit unicode_region_subtag for Africa
    u"\U0001f3f4\U000e0030\U000e0030\U000e0032\U000e007f": "00-2",
    # 3-digit unicode_region_subtag for Americas
    u"\U0001f3f4\U000e0030\U000e0031\U000e0039\U000e007f": "01-9",
    # 3-digit unicode_region_subtag for US
    u"\U0001f3f4\U000e0038\U000e0034\U000e0030\U000e007f": "84-0",

    # Unknown subdivision of the US
    u"\U0001f3f4\U000e0075\U000e0073\U000e007a\U000e007a\U000e007a\U000e007a\U000e007f": "us-zzzz"
}

emoji_module = {
    ":Scotland:": ":gb-sct:",
    ":Wales:": ":gb-wls:",
    ":England:": ":gb-eng:"
}

wrong_codes = [
    # Black flag:
    u"\U0001f3f4",
    # White flag:
    u"\U0001f3f3",
    # Missing cancel tag: blackflag g b e n g:
    u"\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067",
    # whiteflag g b e n g cancel:
    u"\U0001f3f3\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
    # blackflag g b cancel:
    u"\U0001f3f4\U000e0067\U000e0062\U000e007f",
    # blackflag space g b e n g cancel:
    u"\U0001f3f4 \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
    # blackflag g b e n g space cancel:
    u"\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067 \U000e007f",
    # blackflag g b space e n g cancel:
    u"\U0001f3f4\U000e0067\U000e0062 \U000e0065\U000e006e\U000e0067\U000e007f",
    # blackflag whiteflag b e n g cancel:
    u"\U0001f3f4\U0001f3f3\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
    # Pirate flag:
    u"\U0001F3F4\U0000200D\U00002620\U0000FE0F",
    # blackflag G b e n g cancel:
    u"\U0001f3f4\U000e0047\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
    # blackflag g b E n g cancel:
    u"\U0001f3f4\U000e0067\U000e0062\U000e0045\U000e006e\U000e0067\U000e007f",
    # blackflag g b - e n g cancel:
    u"\U0001f3f4\U000e0067\U000e0062\U000e002d\U000e0065\U000e006e\U000e0067\U000e007f",

]


def encode(text):
    assert flag.flagize(
        text, subregions=True) == flag.flagize(
        flag.flagize_subregional(text))
    assert flag.flagize(
        flag.flagize_subregional(text)) == flag.flagize_subregional(
        flag.flagize(text))
    return flag.flagize(text, subregions=True)


def decode(text):
    assert flag.dflagize(
        text, subregions=True) == flag.dflagize(
        flag.dflagize_subregional(text))
    assert flag.dflagize(
        flag.dflagize_subregional(text)) == flag.dflagize_subregional(
        flag.dflagize(text))
    return flag.dflagize(text, subregions=True)


def test_basic():
    for value, ascii in basic.items():
        assert decode(value) == ascii
        assert encode(ascii) == value


def test_basic_mixed():
    for value, ascii in basic_mixed.items():
        assert decode(value) == ascii
        assert encode(ascii) == value


def test_valid_codes():
    for value, ascii in valid_codes.items():
        ascii_lower = ":%s:" % ascii.lower()
        ascii_upper = ":%s:" % ascii.upper()

        x = decode(value)
        y0 = encode(ascii_lower)
        y1 = encode(ascii_upper)
        z0 = decode(y0)
        z1 = decode(y1)

        assert x == ascii_lower
        assert y0 == value
        assert y1 == value
        assert x == z0
        assert z0 == z1


def test_compare_with_emoji_module():
    for emojicode, ascii in emoji_module.items():
        assert encode(ascii) == emoji.emojize(emojicode)


def test_wrong_codes():
    for code in wrong_codes:
        x = decode(code)

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
