# -*- coding: utf-8 -*-
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

__version__ = '1.2.3'
__author__ = 'cuzi'
__email__ = 'cuzi@openmail.cc'
__source__ = 'https://github.com/cvzi/flag'
__license__ = """
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
    "flagize",
    "dflagize",
    "flagize_subregional",
    "dflagize_subregional"]

import sys
import re

OFFSET = 127397  # = ord("🇦") - ord("A")
OFFSET_TAG = 0xE0000
CANCELTAG = "\U000E007F"
BLACKFLAG = "\U0001F3F4"
ASCII_LOWER = "abcdefghijklmnopqrstuvwxyz0123456789"


def flag(countrycode):
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
    elif len(code) > 2 and len(code) < 7:
        # Tag sequence
        return flag_tag_sequence(code)
    found = ''.join(code)
    raise ValueError(
        'invalid countrycode, found %d (%r) in %r.' %
        (len(found), found, countrycode))


def flag_regional_indicator(code):
    """Two letters are converted to regional indicator symbols

    :param str code: two letter ISO 3166 code
    :return: regional indicator symbols of the country flag
    :rtype: str
    """

    return "".join([chr(ord(c.upper()) + OFFSET) for c in code])


def flag_tag_sequence(code):
    """Three to seven letters/digits are converted to  a tag sequence.

    :param str code: regional code from ISO 3166-2.
    :return: The unicode tag sequence of the subregional flag
    :rtype: str
    """

    tags = "".join([chr(ord(c.lower()) + OFFSET_TAG) for c in code])
    return BLACKFLAG + tags + CANCELTAG


def flagize(text, subregions=False):
    """Encode flags. Replace all two letter codes ``:XX:`` with unicode flags
    (emoji flag sequences)

    :param str text: The text
    :param bool subregions: Also replace subregional/subdivision codes
        ``:xx-xxx:`` with unicode flags (flag emoji tag sequences).
    :return: The text with all occurrences of ``:XX:`` replaced by unicode
        flags
    :rtype: str
    """

    def flag_repl(matchobj):
        return flag_regional_indicator(matchobj.group(1))

    text = re.sub(":([a-zA-Z]{2}):", flag_repl, text)

    if subregions:
        text = flagize_subregional(text)

    return text


def dflagize(text, subregions=False):
    """Decode flags. Replace all unicode country flags (emoji flag sequences)
    in text with ascii two letter code ``:XX:``

    :param str text: The text
    :param bool subregions: Also replace subregional/subdivision flags
        (flag emoji tag sequences) with ``:xx-xxx:``
    :return: The text with all unicode flags replaced by ascii
        sequence ``:XX:``
    :rtype: str
    """

    def dflag(i):
        points = tuple(ord(x) - OFFSET for x in i)
        return ":%c%c:" % points

    def dflag_repl(matchobj):
        return dflag(matchobj.group(0))

    regex = re.compile("([\U0001F1E6-\U0001F1FF]{2})", flags=re.UNICODE)

    text = regex.sub(dflag_repl, text)

    if subregions:
        text = dflagize_subregional(text)

    return text


def flagize_subregional(text):
    """Encode subregional/subdivision flags. Replace all regional codes
    ``:xx-xxx:`` with unicode flags (flag emoji tag sequences)

    :param str text: The text
    :return: The text with all occurrences of ``:xx-xxx:`` replaced by
        unicode flags
    :rtype: str
    """

    def flag_repl(matchobj):
        return flag_tag_sequence(matchobj.group(1) + matchobj.group(2))

    # Enforces a hyphen after two chars, allows both:
    # - The natural 2-letter unicode_region_subtag and subdivision_suffix like
    #   California USCA ":us-ca:", England GBENG ":gb-eng:"
    # - For sake of completeness: 3-digit unicode_region_subtag like 840 for
    #   US formatted as ":84-0:"
    text = re.sub(
        ":([a-zA-Z]{2}|[0-9]{2})-([0-9a-zA-Z]{1,4}):",
        flag_repl,
        text)

    return text


def dflagize_subregional(text):
    """Decode subregional/subdivision flags. Replace all unicode regional
    flags (flag emoji tag sequences) in text with their ascii
    code ``:xx-xxx:``

    :param str text: The text
    :return: The text with all regional flags replaced by ascii
        sequence ``:xx-xxx:``
    :rtype: str
    """

    def dflag(i):
        points = [ord(x) - OFFSET_TAG for x in i]
        suffix = "".join(["%c" % point for point in points[2:]]) + ":"
        return ":%c%c-%s" % (points[0], points[1], suffix)

    def dflag_repl(matchobj):
        return dflag(matchobj.group(1))

    regex = re.compile(
        BLACKFLAG +
        "([\U000E0030-\U000E0039\U000E0061-\U000E007A]{3,6})" +
        CANCELTAG,
        flags=re.UNICODE)
    text = regex.sub(dflag_repl, text)

    return text
