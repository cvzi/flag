import pytest

import flag

testdata_supported = [
    ("ES", "🇪🇸"),
    ("US", "🇺🇸"),
    ("gb-eng", "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f"),
    ("gb-sct", "\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f"),
    ("gb-wls", "\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f"),
]

@pytest.mark.parametrize("code,unicode_flag", testdata_supported)
def test_unsupported(code: str, unicode_flag: str):
    assert flag.flag(code) == unicode_flag
    assert flag.flag_safe(code, "error", "error") == unicode_flag
    assert flag.flag_safe(code, lambda x: "_-", lambda x: "-_") == unicode_flag
    assert flag.flagize(f":{code}:", subregions=True) == unicode_flag
    assert flag.dflagize(unicode_flag, subregions=True) == f":{code}:"
    f = flag.Flag(only_supported=True, only_valid=True, allow_subregions=True)
    assert f.flag(code) == unicode_flag
    assert f.flagize(f":{code}:") == unicode_flag
    assert f.dflagize(unicode_flag) == f":{code}:"


testdata_unsupported_invalid = [
    (":gb-sfk:", "\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0066\U000e006b\U000e007f"),
    (":ZZ:", "🇿🇿"),
    (":XX:", "🇽🇽"),
    (":zz-zzz:", "\U0001f3f4\U000e007a\U000e007a\U000e007a\U000e007a\U000e007a\U000e007f"),
]

@pytest.mark.parametrize("code,_", testdata_unsupported_invalid)
def test_flag_safe_unsupported_invalid(code: str, _):
    r = flag.flag_safe(code, "allow", "allow")
    assert isinstance(r, str)
    assert r != code

    assert flag.flag_safe(code, lambda _: "unsupported", "allow") == "unsupported"

    assert flag.flag_safe(code, "allow", lambda _: "invalid") == "invalid"

    with pytest.raises(flag.FlagError):
        flag.flag_safe(code)

    with pytest.raises(flag.UnsupportedFlag):
        flag.flag_safe(code, unsupported="error", invalid="allow")

    with pytest.raises(flag.InvalidFlag):
        flag.flag_safe(code, unsupported="allow", invalid="error")


@pytest.mark.parametrize("code,_", testdata_unsupported_invalid)
def test_method_flag_unsupported_invalid(code: str, _):
    f = flag.Flag(only_supported=True, only_valid=False)

    with pytest.raises(flag.UnsupportedFlag):
        f.flag(code)

    f = flag.Flag(only_supported=False, only_valid=True)

    with pytest.raises(flag.InvalidFlag):
        f.flag(code)


@pytest.mark.parametrize("code, unicode_flag", testdata_unsupported_invalid)
def test_dflagize_unsupported_invalid(code: str, unicode_flag: str):
    f = flag.Flag(only_valid=True, only_supported=True, allow_subregions=True)

    assert f.dflagize(unicode_flag) == unicode_flag

    assert flag.dflagize(unicode_flag, subregions=True) == code

    with pytest.raises(flag.FlagError):
        f.flag(code)

    assert flag.flag(code) == unicode_flag



@pytest.mark.parametrize("code, unicode_flag", testdata_unsupported_invalid)
def test_handle_illegal(code: str, unicode_flag: str):
    f = flag.Flag(only_valid=True, only_supported=True, allow_subregions=True)

    assert f.dflagize(unicode_flag, handle_illegal=lambda x,y: "illegal") == "illegal"

    assert f.dflagize(unicode_flag, handle_illegal=lambda x,y: x) == unicode_flag

    assert f.flagize(code, handle_illegal=lambda x,y: "illegal") == "illegal"

    assert f.flagize(code, handle_illegal=lambda x,y: x) == code

testdata_unkown_codes = [
    "",
    "\n",
    "\t",
    "\r",
    "\\",
    '"',
    "'",
    "  ",
    "a ",
    " a ",
    "a\n",
    " a",
    "a-",
    "a--",
    "ää",
    "ÄÄ",
    "äÄ",
    "--",
    "a",
    "z",
    "a$",
    "$a",
    "a$",
    "a&$-",
    "a*&^%$",
    "A",
    "Z",
    "A-",
    "\U0001f1faS",
    "U\U0001f1f8",
    "\U0001f1fa\U0001f1f8",
    "\U000e0062\U000e0073",
    "zz-zzzzzz",
    "zzzzzzzz",
]


@pytest.mark.parametrize("string", testdata_unkown_codes)
def test_unknown(string: str):
    with pytest.raises(flag.UnknownCountryCode):
        print("string: ", string)
        flag.flag_safe(string)
