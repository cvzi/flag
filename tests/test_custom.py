import warnings

import pytest

import flag


def test_custom_simple():
    for a, b in [
        ("🇧", "🇧"),
        ("🇩🇪", "🇩🇪"),
        ("DE", "DE"),
        ("A", "B"),
        ("1", "2"),
        ("#", "#"),
        (".", "."),
        ("-", "z"),
        ("0", "123"),
        ("\U0001f3f4", "\U0001f3f4"),
    ]:
        f = flag.Flag(a, b, warn=False, allow_subregions=True)

        assert f.flag(":il-") == "🇮🇱"
        assert flag.flag(":il-") == "🇮🇱"

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

        assert (
            "❤️\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️"
            == f.flagize("❤️%sgb-eng%s✡️" % (a, b))
        )

        assert "❤️%sgb-eng%s✡️" % (a, b) == f.dflagize(
            "❤️\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️"
        )

        assert (
            "❤️A\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️"
            == f.flagize("❤️A%sgb-eng%s✡️" % (a, b))
        )

        assert "❤️A%sgb-eng%s✡️" % (a, b) == f.dflagize(
            "❤️A\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️",
        )

        assert (
            "❤️0\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f1✡️"
            == f.flagize("❤️0%sgb-eng%s1✡️" % (a, b))
        )

        assert "❤️0%sgb-eng%s1✡️" % (a, b) == f.dflagize(
            "❤️0\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f1✡️"
        )

        assert (
            "❤️a\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️"
            == f.flagize("❤️a%sgb-eng%s✡️" % (a, b))
        )

        assert "❤️a%sgb-eng%s✡️" % (a, b) == f.dflagize(
            "❤️a\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f✡️"
        )


def test_warnings():
    for args in [("-", "-"), ("a", "b"), ("abc", "012"), ("345", "AbC"), ("",)]:
        f = flag.Flag(*args)
        f.allow_subregions = True
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.flagize("️🇮🇱")

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
        f.allow_subregions = True
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.flagize("️🇮🇱")
            f.flagize("️🇮🇱")
            f.flagize("️🇮🇱")
            f.flagize_subregional("️🇮🇱")
            f.flagize_subregional("️🇮🇱")

        assert len(w) == 2
        assert issubclass(w[-1].category, UserWarning)
        assert "subregional" in str(w[-1].message)

    for args in [
        ("-", "-"),
        ("a", "b"),
        ("abc", "012"),
        ("345", "AbC"),
        ("abc",),
        ("987",),
        ("abc",),
    ]:
        f = flag.Flag(*args)
        f.allow_subregions = True
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.dflagize("️🇮🇱")

        assert len(w) == 0

    for b in ["abcd", "9871"]:
        f = flag.Flag(suffix_str=b)
        f.allow_subregions = True
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            f.dflagize("️🇮🇱")

        assert len(w) == 0


valid_codes = {
    "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": "gb-eng",
    "\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f": "gb-sct",
    "\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f": "gb-wls",
}


def test_custom_subregions():
    for a, b in [
        ("🇧", "🇧"),
        ("DE", "DE"),
        ("-", "b-"),
        ("-", "auto"),
        ("ab", "0123"),
        ("#", "#"),
        (".", "."),
        ("0", "123"),
        ("\U0001f3f4", "\U0001f3f4"),
    ]:
        f = flag.Flag(a, b, warn=False, allow_subregions=True)

        for emoji, ascii in valid_codes.items():
            assert emoji == f.flagize("%s%s%s" % (a, ascii, b))

            assert "%s%s%s" % (a, ascii, b) == f.dflagize(emoji)

            assert a + emoji + b == f.flagize(
                "%s%s%s%s%s" % (a, a, ascii, b, b)
            )

            assert "%s%s%s%s%s" % (a, a, ascii, b, b) == f.dflagize(
                a + emoji + b
            )

            assert b + emoji + a == f.flagize(
                "%s%s%s%s%s" % (b, a, ascii, b, a)
            )

            assert "%s%s%s%s%s" % (b, a, ascii, b, a) == f.dflagize(
                b + emoji + a
            )


def test_allow_texas():
    f = flag.Flag(only_supported=True, only_valid=True, allow_subregions=True)

    with pytest.raises(flag.FlagError):
        f.flag("XT")

    with pytest.raises(flag.FlagError):
        f.flag("us-tx")

    assert f.flagize(":XT: :us-tx:") == ":XT: :us-tx:"

    f.add_flag("XT")

    assert f.flag("XT") is not None

    f.add_flag("us-tx")

    assert f.flag("ustx") is not None

    assert f.flagize(":XT: :us-tx:") == flag.flagize(":XT: :us-tx:", subregions=True)


def test_ban_italy():
    f = flag.Flag(only_supported=True, only_valid=True, allow_subregions=True)

    assert f.flag("IT") is not None

    f.add_flag("IT", supported=False, valid=False)

    with pytest.raises(flag.FlagError):
        f.flag("IT")

    assert f.flagize(":IT:") == ":IT:"


def test_add_corrupt_flag():
    f = flag.Flag(only_supported=True, only_valid=True, allow_subregions=True)
    with pytest.raises(flag.FlagError):
        f.add_flag("")
    with pytest.raises(flag.FlagError):
        f.add_flag("A ")
    

def test_defaults():
    f = flag.Flag(only_supported=False, only_valid=False, allow_subregions=False)

    assert f.flag("IT") == flag.flag("IT")
    assert f.flag("IT") == flag.flagize(":IT:")
    assert f.flagize(":DK: :NL:") == flag.flagize(":DK: :NL:")
    assert f.flagize(":DK: :NL:") != ":DK: :NL:"

