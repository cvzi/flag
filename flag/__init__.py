"""
Converts flag emoji to ascii and back
https://github.com/cvzi/flag
Based on http://schinckel.net/2015/10/29/unicode-flags-in-python/

Unicode country code emoji flags for Python
~~~~~~~~~~~~~~~~
    >>> import flag
    >>> flag.flag("IL")
    '🇮🇱'
    >>> flag.flagize("Flag of Israel :IL:")
    'Flag of Israel 🇮🇱'
    >>> flag.dflagize("Flag of Israel 🇮🇱")
    'Flag of Israel :IL:'
    >>> flag.flagize(":gb-eng: is part of the UK :GB:", subregions=True)
    'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'
    >>> flag.dflagize("England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True)
    'England :gb-eng: is part of the UK :GB:'
"""

import warnings
import re
from typing import (
    Callable,
    MutableMapping,
    Mapping,
    Any,
    Literal,
    Iterable,
    Optional,
    List,
)

__version__: str = "2.1.0"
__author__: str = "cuzi"
__email__: str = "cuzi@openmail.cc"
__source__: str = "https://github.com/cvzi/flag"
__license__: str = """
MIT License

Copyright (c) cuzi 2018

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__all__ = [
    "flag",
    "flagize",
    "dflagize",
    "flagize_subregional",
    "dflagize_subregional",
    "Flag",
]


OFFSET = ord("🇦") - ord("A")
OFFSET_TAG = 0xE0000
CANCELTAG = "\U000e007f"
BLACKFLAG = "\U0001f3f4"
ASCII_LOWER = "abcdefghijklmnopqrstuvwxyz0123456789"

_FlagInfo = MutableMapping[str, str | bool | None]
_FlagInfos = MutableMapping[str, _FlagInfo]


class FlagError(ValueError):
    pass


class InvalidFlag(FlagError):
    pass


class UnsupportedFlag(FlagError):
    pass


class UnknownCountryCode(InvalidFlag):
    pass


def check_prefix(custom_str: str) -> bool:
    """Check if prefix will safely work with flagize and subregional flags

    :param str custom_str: Custom prefix
    :return: False if the string will safely work with subregional flags
    :rtype: bool
    """

    return len(custom_str) == 0


def check_suffix(custom_str: str) -> bool:
    """Check if suffix will safely work with flagize and subregional flags

    :param str custom_str: Custom suffix
    :return: False if the string will safely work with subregional flags
    :rtype: bool
    """

    if custom_str.startswith("-"):
        return True
    if len(custom_str) < 4:
        custom_str = custom_str.lower()
        for c in ASCII_LOWER:
            if c in custom_str:
                return True
    return False


def flag_regional_indicator(code: Iterable[str]) -> str:
    """Two letters are converted to regional indicator symbols

    :param str code: two letter ISO 3166 code
    :return: regional indicator symbols of the country flag
    :rtype: str
    """

    return "".join([chr(ord(c.upper()) + OFFSET) for c in code])


def flag_tag_sequence(code: Iterable[str]) -> str:
    """Three to seven letters/digits are converted to  a tag sequence.

    :param str code: regional code from ISO 3166-2.
    :return: The unicode tag sequence of the subregional flag
    :rtype: str
    """

    tags = "".join([chr(ord(c.lower()) + OFFSET_TAG) for c in code])
    return BLACKFLAG + tags + CANCELTAG


class Flag:
    """This class offers different prefix and suffix instead
    of colons and allows to only convert widely supported or valid flags.
    """

    only_supported: bool
    only_valid: bool
    allow_subregions: bool
    _data: Optional[_FlagInfos]

    def __init__(
        self,
        prefix_str: str = ":",
        suffix_str: str = ":",
        only_supported: bool = True,
        only_valid: bool = True,
        allow_subregions: bool = True,
        warn: bool = True,
    ) -> None:
        """Set a custom prefix and suffix. Instead of ``:XY:`` it will
        use ``{prefix}XY{suffix}``.

        To encode subregional flags, use a suffix that is either longer
        than 4 characters or that does not contain A-Z, a-z, 0-9 and
        does not start with a - (minus).

        :param str prefix_str: The leading symbols
        :param str suffix_str: The trailing symbols
        :param bool only_supported: Only convert country codes that are widely supported by browsers and devices
        :param bool only_valid: Only convert country codes that are considered "valid" by Unicode
        :param bool allow_subregions: Also replace subregional/subdivision codes e.g. Scottland as :gb-sct:
        :param bool warn: Show a warning if an unsafe prefix or suffix is used
        """

        self._prefix = prefix_str
        self._prefix_re = re.escape(prefix_str)
        self._prefix_warn = warn and check_prefix(self._prefix)

        self._suffix = suffix_str
        self._suffix_re = re.escape(suffix_str)
        self._suffix_warn = warn and check_suffix(self._suffix)

        self.only_supported = only_supported
        self.only_valid = only_valid
        self.allow_subregions = allow_subregions

        self._data = None

    def flag(self, countrycode: str) -> str:
        """Encodes a single flag to unicode. Two letters are converted to
        regional indicator symbols
        Three or more letters/digits are converted to tag sequences.
        Dashes, colons and other symbols are removed from input, only a-z, A-Z
        and 0-9 are processed.

        In general a valid flag is either a two letter code from ISO 3166
        (e.g. ``GB``), a code from ISO 3166-2 (e.g. ``GBENG``) or a numeric
        code from ISO 3166-1.
        However, not all codes produce valid unicode, see
        http://unicode.org/reports/tr51/#flag-emoji-tag-sequences for more
        information.
        From ISO 3166-2 only England ``gbeng``, Scotland ``gbsct`` and
        Wales ``gbwls`` are considered RGI (recommended for general
        interchange) by the Unicode Consortium,
        see http://www.unicode.org/Public/emoji/latest/emoji-test.txt

        Depending on the settings, the function may raise an error if the
        flag is not supported or invalid.

        :param str countrycode: Two letter ISO 3166 code or a regional code
            from ISO 3166-2.
        :return: The unicode representation of the flag
        :rtype: str
        """

        if self.only_supported or self.only_valid:
            return flag_safe(
                countrycode,
                unsupported="error" if self.only_supported else "allow",
                invalid="error" if self.only_valid else "allow",
                custom_data=self._data,
            )
        return flag(countrycode)

    def _is_legal(self, code: str) -> bool:
        """Return false if the flag violetes either the only_supported
        and only_valid setting. Otherwise true"""
        if not self.only_supported and not self.only_valid:
            return True
        r = _check_flag(code, self._data)
        if any(isinstance(e, UnsupportedFlag) for e in r) and self.only_supported:
            return False
        if any(isinstance(e, InvalidFlag) for e in r) and self.only_valid:
            return False
        return True

    def flagize(
        self, text: str, handle_illegal: Optional[Callable[[str, str], str]] = None
    ) -> str:
        """Encode flags. Replace all two letter codes ``{prefix}XX{suffix}`` with unicode
        flags (emoji flag sequences)

        For this method the suffix should not contain
        A-Z, a-z or 0-9 and not start with a - (minus).

        Depending on the settings, the function may only convert supported or valid flags.
        If an unsupported or invalid flag is found, the flag is either ignored or
        ``handle_illegal`` is called.

        :param str text: The text
        :param callable handle_illegal: A function that is called when an illegal flag is found.
            The function should take two arguments, the match i.e. `:XY:` and the code i.e. `XY`
            and return a string to replace the illegal flag.
        :return: The text with all occurrences of ``{prefix}XX{suffix}`` replaced by unicode
            flags
        :rtype: str
        """

        def flag_repl(matchobj: re.Match[str]) -> str:
            code = matchobj.group(1)
            if self._is_legal(code):
                return flag_regional_indicator(matchobj.group(1))
            elif handle_illegal is not None:
                return handle_illegal(matchobj.group(0), code)
            else:
                return matchobj.group(0)

        text = re.sub(
            self._prefix_re + "([a-zA-Z]{2})" + self._suffix_re, flag_repl, text
        )

        if self.allow_subregions:
            text = self.flagize_subregional(text, handle_illegal)

        return text

    def dflagize(
        self, text: str, handle_illegal: Optional[Callable[[str, str], str]] = None
    ) -> str:
        """Decode flags. Replace all unicode country flags (emoji flag
        sequences) in text with ascii two letter code ``{prefix}XX{suffix}``

        Depending on the settings, the function may only convert supported or valid flags.
        If an unsupported or invalid flag is found, the flag is either ignored or
        ``handle_illegal`` is called.

        :param str text: The text
        :param callable handle_illegal: A function that is called when an illegal flag is found.
            The function should take two arguments, the unicode flag and the code i.e. `XY`
            and return a string to replace the illegal flag.
        :return: The text with all unicode flags replaced by ascii
            sequence ``{prefix}XX{suffix}``
        :rtype: str
        """

        pattern = f"{self._prefix}%s{self._suffix}"

        def dflag_repl(matchobj: re.Match[str]) -> str:
            points = matchobj.group(0)
            c1 = chr(ord(points[0]) - OFFSET)
            c2 = chr(ord(points[1]) - OFFSET)
            cc = f"{c1}{c2}"
            if self._is_legal(cc):
                return pattern % (cc)
            elif handle_illegal is not None:
                return handle_illegal(matchobj.group(0), cc)
            else:
                return matchobj.group(0)

        regex = re.compile("([\U0001f1e6-\U0001f1ff]{2})", flags=re.UNICODE)

        text = regex.sub(dflag_repl, text)

        if self.allow_subregions:
            text = self.dflagize_subregional(text, handle_illegal)

        return text

    def flagize_subregional(
        self, text: str, handle_illegal: Optional[Callable[[str, str], str]] = None
    ) -> str:
        """Encode subregional/subdivision flags. Replace all regional codes
        ``{prefix}xx-xxx{suffix}`` with unicode flags (flag emoji tag sequences)

        For this method the suffix should not contain
        A-Z, a-z or 0-9 and not start with a - (minus).

        :param str text: The text
        :param callable handle_illegal: See `flag.flagize()`
        :return: The text with all occurrences of ``{prefix}xx-xxx{suffix}`` replaced by
            unicode flags
        :rtype: str
        """

        if self._prefix_warn:
            warnings.warn(
                """The empty prefix (%r) is unsafe for subregional flags.
You can use Flag(%r, %r, warn=False) to disable this warning"""
                % (self._prefix, self._prefix, self._suffix),
                UserWarning,
                stacklevel=1,
            )
            self._prefix_warn = False
        elif self._suffix_warn:
            warnings.warn(
                """The suffix (%r) is unsafe for subregional flags
because it is short and contains a-z, 0-9 or starts with -
You can use Flag(%r, %r, warn=False) to disable this warning"""
                % (self._suffix, self._prefix, self._suffix),
                UserWarning,
                stacklevel=1,
            )
            self._suffix_warn = False

        def flag_repl(matchobj: re.Match[str]) -> str:
            code = matchobj.group(1) + matchobj.group(2)
            if self._is_legal(code):
                return flag_tag_sequence(code)
            elif handle_illegal is not None:
                return handle_illegal(matchobj.group(0), code)
            else:
                return matchobj.group(0)

        # Enforces a hyphen after two chars, allows both:
        # - The natural 2-letter unicode_region_subtag and subdivision_suffix
        #   like California USCA ":us-ca:", England GBENG ":gb-eng:"
        # - For sake of completeness: 3-digit unicode_region_subtag like 840
        #   for US formatted as ":84-0:"
        text = re.sub(
            self._prefix_re
            + "([a-zA-Z]{2}|[0-9]{2})-([0-9a-zA-Z]{1,4})"
            + self._suffix_re,
            flag_repl,
            text,
        )

        return text

    def dflagize_subregional(
        self, text: str, handle_illegal: Optional[Callable[[str, str], str]] = None
    ) -> str:
        """Decode subregional/subdivision flags. Replace all unicode regional
        flags (flag emoji tag sequences) in text with their ascii
        code ``{prefix}xx-xxx{suffix}``

        :param str text: The text
        :param callable handle_illegal: See `flag.flagize()`
        :return: The text with all regional flags replaced by ascii
            sequence ``{prefix}xx-xxx{suffix}``
        :rtype: str
        """

        def dflag_repl(matchobj: re.Match[str]) -> str:
            code = "".join(
                chr(i) for i in [ord(c) - OFFSET_TAG for c in matchobj.group(1)]
            )
            if self._is_legal(code):
                return f"{self._prefix}{code[0:2]}-{code[2:]}{self._suffix}"
            elif handle_illegal is not None:
                return handle_illegal(matchobj.group(0), code)
            else:
                return matchobj.group(0)

        regex = re.compile(
            BLACKFLAG
            + "([\U000e0030-\U000e0039\U000e0061-\U000e007a]{3,6})"
            + CANCELTAG,
            flags=re.UNICODE,
        )
        text = regex.sub(dflag_repl, text)

        return text

    def add_flag(self, countrycode: str, supported: bool = True, valid: bool = True):
        """Add a custom flag. This can be used to overwrite the standard values
        and allow custom flags to be considered supported and/or valid or remove
        supported flags.
        The current use-case for this function is the flag of Texas, which is
        only supported by WhatsApp. It is also possible to censor a flag.
        Example to add Texas flag: ``flag.add_flag("XT", supported=True, valid=True)``
        Example to censor Italy flag: ``flag.add_flag("IT", supported=False, valid=False)``

        :param str text: The text
        :param callable handle_illegal: See `flag.flagize()`
        :return: The text with all regional flags replaced by ascii
            sequence ``{prefix}xx-xxx{suffix}``
        :rtype: str
        """
        if self._data is None:
            self._data = {}

        code = [c for c in countrycode.lower() if c in ASCII_LOWER]

        if len(code) == 2:
            # Regional indicator symbols
            code = "".join(code).upper()
        elif len(code) > 2 and len(code) < 7:
            # Tag sequence
            code = "".join(code).lower()
        else:
            raise UnknownCountryCode(
                "illegal countrycode, found %r in %r." % (code, countrycode)
            )

        data: _FlagInfo = {"supported": supported, "valid": valid}
        self._data[code] = data


def flag(countrycode: str) -> str:
    """Encodes a single flag to unicode. Two letters are converted to regional
    indicator symbols
    Three or more letters/digits are converted to tag sequences.
    Dashes, colons and other symbols are removed from input, only a-z, A-Z and
    0-9 are processed.

    In general a valid flag is either a two letter code from ISO 3166
    (e.g. ``GB``), a code from ISO 3166-2 (e.g. ``GBENG``) or a numeric code
    from ISO 3166-1.
    However, not all codes produce valid unicode, see
    http://unicode.org/reports/tr51/#flag-emoji-tag-sequences for more
    information.
    From ISO 3166-2 only England ``gbeng``, Scotland ``gbsct`` and
    Wales ``gbwls`` are considered RGI (recommended for general interchange)
    by the Unicode Consortium,
    see http://www.unicode.org/Public/emoji/latest/emoji-test.txt

    :param str countrycode: Two letter ISO 3166 code or a regional code
        from ISO 3166-2.
    :return: The unicode representation of the flag
    :rtype: str
    """

    code = [c for c in countrycode.lower() if c in ASCII_LOWER]
    if len(code) == 2:
        # Regional indicator symbols
        return flag_regional_indicator(code)
    if len(code) > 2 and len(code) < 7:
        # Tag sequence
        return flag_tag_sequence(code)
    found = "".join(code)
    raise UnknownCountryCode(
        "illegal countrycode, found %r in %r." % (found, countrycode)
    )


_on_illegal = Callable[[_FlagInfo], Any] | Literal["error", "allow"]


def flag_safe(
    countrycode: str,
    unsupported: _on_illegal = "error",
    invalid: _on_illegal = "error",
    custom_data: Optional[_FlagInfos] = None,
) -> Any:
    """Encodes a single flag to unicode. Two letters are converted to regional
    indicator symbols
    Three or more letters/digits are converted to tag sequences.
    Dashes, colons and other symbols are removed from input, only a-z, A-Z and
    0-9 are processed.

    The ``unsupported`` and ``invalid`` parameter control which flags are
    converted. If a flag is not supported or invalid, the function will
    return the result of the ``on_illegal`` function or raise an error
    if either parameter is set to "error".

    :param str countrycode: Two letter ISO 3166 code or a regional code
        from ISO 3166-2.
    :param str|callable unsupported: "error" | "allow" | Callable(dict)

        If "allow" return the flag.
        If "error" raise an error if flag is unsupported. If callable
        return the result of the callable if flag is unsupported. The callable
        receives the result of the :meth:`flag.info()` function e.g.
        ``{'id_status': 'regular', 'supported': False, 'valid': True}``
    :param str|callable invalid: Same as ``unsupported`` but for invalid flags
    :param dict custom_data: Custom maps dict with custom valid/supported values to overwrite
        the standard values. For example with the WhatsApp Texas flag:
        ``{'XT': {'id_status': 'regular', 'supported': False, 'valid': True}}``
    :return: The unicode representation of the flag
    :rtype: str
    """
    code = [c for c in countrycode.lower() if c in ASCII_LOWER]
    if len(code) == 2:
        # Regional indicator symbols
        r = _check_flag("".join(code).upper(), custom_data)
    elif len(code) > 2 and len(code) < 7:
        # Tag sequence
        r = _check_flag("".join(code).lower(), custom_data)
    else:
        found = "".join(code)
        r = [
            UnknownCountryCode(
                "illegal countrycode, found %r in %r." % (found, countrycode)
            )
        ]

    if (
        any(isinstance(uf_exp := e, UnsupportedFlag) for e in r)
        and unsupported != "allow"
    ):
        match unsupported:
            case "error":
                raise uf_exp
            case _:
                return unsupported(info(countrycode))

    if any(isinstance(if_exp := e, InvalidFlag) for e in r) and invalid != "allow":
        match invalid:
            case "error":
                raise if_exp
            case _:
                return invalid(info(countrycode))

    return flag(countrycode)


def _check_flag(
    code: str, custom_data: Optional[_FlagInfos] = None
) -> Iterable[FlagError]:
    """Return errors for unsupported or invalid flags.

    :param str code: two-letter codes must be upper-case code, others must be lower-case
    :param dict custom_data: Custom maps dict with custom valid/supported values to overwrite
                             the standard values
    """

    if custom_data is not None and code in custom_data:
        data = custom_data[code]
    else:
        data = info(code, extended=False)
    r: List[FlagError] = []
    if not data["supported"]:
        r.append(UnsupportedFlag("".join(code)))
    if not data["valid"]:
        r.append(InvalidFlag("".join(code)))
    return r


def flagize(text: str, subregions: bool = False) -> str:
    """Encode flags. Replace all two letter codes ``:XX:`` with unicode flags
    (emoji flag sequences)

    :param str text: The text
    :param bool subregions: Also replace subregional/subdivision codes
        ``:xx-xxx:`` with unicode flags (flag emoji tag sequences).
    :return: The text with all occurrences of ``:XX:`` replaced by unicode
        flags
    :rtype: str
    """

    try:
        standard.allow_subregions = subregions
        return standard.flagize(text)
    finally:
        standard.allow_subregions = False


def dflagize(text: str, subregions: bool = False) -> str:
    """Decode flags. Replace all unicode country flags (emoji flag sequences)
    in text with ascii two letter code ``:XX:``

    :param str text: The text
    :param bool subregions: Also replace subregional/subdivision flags
        (flag emoji tag sequences) with ``:xx-xxx:``
    :return: The text with all unicode flags replaced by ascii
        sequence ``:XX:``
    :rtype: str
    """

    try:
        standard.allow_subregions = subregions
        return standard.dflagize(text)
    finally:
        standard.allow_subregions = False


def flagize_subregional(text: str) -> str:
    """Encode subregional/subdivision flags. Replace all regional codes
    ``:xx-xxx:`` with unicode flags (flag emoji tag sequences)

    :param str text: The text
    :return: The text with all occurrences of ``:xx-xxx:`` replaced by
        unicode flags
    :rtype: str
    """

    return standard.flagize_subregional(text)


def dflagize_subregional(text: str) -> str:
    """Decode subregional/subdivision flags. Replace all unicode regional
    flags (flag emoji tag sequences) in text with their ascii
    code ``:xx-xxx:``

    :param str text: The text
    :return: The text with all regional flags replaced by ascii
        sequence ``:xx-xxx:``
    :rtype: str
    """

    return standard.dflagize_subregional(text)


def info(countrycode: str, extended: bool = False) -> _FlagInfo:
    """
    Retrieve information about a country code.
    E.g. ``{'id_status': 'regular', 'supported': False, 'valid': True}``
    """

    flag_data = infos(extended)
    default: _FlagInfo = {"id_status": None, "supported": False, "valid": False}
    if countrycode in flag_data:
        return {**default, **flag_data[countrycode]}
    return default


def infos(extended: bool = False) -> _FlagInfos:
    """
    Dict containing all supported and valid country codes.
    If extended is True, the dict will contain all country
    and subregional codes.
    """

    global _get_infos, _get_extended_infos

    try:
        if extended:
            # type: ignore [name-defined, reportUndefinedVariable]
            return _get_extended_infos()
        else:
            # type: ignore [name-defined, reportUndefinedVariable]
            return _get_infos()
    except NameError:
        from .data import (
            get_infos as _get_infos,
            get_extended_infos as _get_extended_infos,
        )

        if extended:
            # type: ignore [name-defined, reportUndefinedVariable]
            return _get_extended_infos()
        else:
            # type: ignore [name-defined, reportUndefinedVariable]
            return _get_infos()


def version() -> Mapping[Literal["module", "cldr", "emoji"], str]:
    """Return the version of this module, the Unicode CLDR version
    of the data and the Unicode Emoji version of the validity data.
    """

    from .data import version_cldr, version_emoji

    return {
        "module": __version__,
        "cldr": version_cldr,
        "emoji": version_emoji,
    }


standard = Flag(
    ":", ":", warn=True, only_supported=False, only_valid=False, allow_subregions=False
)
