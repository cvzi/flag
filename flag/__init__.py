# -*- coding: utf-8 -*-
"""
Converts flag emoji to ascii and back
https://github.com/cvzi/flag
Based on http://schinckel.net/2015/10/29/unicode-flags-in-python/

Unicode country code emoji flags for Python
~~~~~~~~~~~~~~~~
    >>> import flag
    >>> flag.flagize("Flag of Israel :IL:")
    'Flag of Israel 🇮🇱'
    >>> flag.dflagize(u"Flag of Israel 🇮🇱")
    'Flag of Israel :IL:'
    >>> flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True)
    'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'
    >>> flag.dflagize(u"England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True)
    'England :gb-eng: is part of the UK :GB:'
"""

__version__ = '1.1.0'
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
CANCELTAG = u"\U000E007F"
BLACKFLAG = u"\U0001F3F4"

PY2 = sys.version_info.major is 2


def flagize(text, subregions=False):
    """Encode flags. Replace all two letter codes ``:XX:`` with unicode flags
    (emoji flag sequences)

    :param str text: The text
    :param bool subregions: Also replace subregional/subdivision codes
        ``:xx-xxx:`` with unicode flags (flag emoji tag sequences).
    :return: The text with all occurences of ``:XX:`` replaced by unicode flags
    :rtype: str
    """
    def flag(code):
        points = [ord(x) + OFFSET for x in code.upper()]

        if PY2:
            return ("\\U%08x\\U%08x" % tuple(points)).decode("unicode-escape")
        else:
            return chr(points[0]) + chr(points[1])

    def flag_repl(matchobj):
        return flag(matchobj.group(1))

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
    if PY2:
        return dflagize_py2(text, subregions)
    else:
        return dflagize_py3(text, subregions)


def dflagize_py3(text, subregions=False):
    def dflag(i):
        points = tuple(ord(x) - OFFSET for x in i)
        return ":%c%c:" % points

    def dflag_repl(matchobj):
        return dflag(matchobj.group(0))

    regex = re.compile(u"([\U0001F1E6-\U0001F1FF]{2})", flags=re.UNICODE)

    text = regex.sub(dflag_repl, text)

    if subregions:
        text = dflagize_subregional_py3(text)

    return text


def dflagize_py2(text, subregions=False):
    def dflag_repl(matchobj):
        a = int(matchobj.group(1), 16)
        b = int(matchobj.group(2), 16)
        if a >= 127462 and a <= 127487 and b >= 127462 and b <= 127487:
            return ":%c%c:" % (a - OFFSET, b - OFFSET)
        return matchobj.group(0)  # Not a regional indicator

    regex = re.compile(r"\\U([0-9a-fA-F]{8})\\U([0-9a-fA-F]{8})")

    text = regex.sub(dflag_repl, text.encode("unicode-escape"))

    text = text.decode("unicode-escape")

    if subregions:
        text = dflagize_subregional_py2(text)

    return text


def flagize_subregional(text):
    """Encode subregional/subdivision flags. Replace all regional codes
    ``:xx-xxx:`` with unicode flags (flag emoji tag sequences)

    :param str text: The text
    :return: The text with all occurences of ``:xx-xxx:`` replaced by
        unicode flags
    :rtype: str
    """
    def flag(code):
        points = [ord(x) + OFFSET_TAG for x in code.lower()]
        if PY2:
            tags = (u"\\U%08x" * len(points) % tuple(points))
            return BLACKFLAG + tags.decode("unicode-escape") + CANCELTAG
        else:
            tags = "".join([chr(point) for point in points])
            return BLACKFLAG + tags + CANCELTAG

    def flag_repl(matchobj):
        return flag(matchobj.group(1) + matchobj.group(2))

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
    if PY2:
        return dflagize_subregional_py2(text)
    else:
        return dflagize_subregional_py3(text)


def dflagize_subregional_py3(text):
    def dflag(i):
        points = [ord(x) - OFFSET_TAG for x in i]
        suffix = "".join("%c" % point for point in points[2:]) + ":"
        return ":%c%c-%s" % (points[0], points[1], suffix)

    def dflag_repl(matchobj):
        return dflag(matchobj.group(1))

    regex = re.compile(
        BLACKFLAG +
        u"([\U000E0030-\U000E0039\U000E0061-\U000E007A]{3,6})" +
        CANCELTAG,
        flags=re.UNICODE)
    text = regex.sub(dflag_repl, text)

    return text


def dflagize_subregional_py2(text):
    BLACKFLAG_repr = "\\" + BLACKFLAG.encode("unicode-escape")
    CANCELTAG_repr = "\\" + CANCELTAG.encode("unicode-escape")

    regex = re.compile(
        BLACKFLAG_repr +
        r"((?:\\U[0-9a-fA-F]{8}){3,6})" +
        CANCELTAG_repr)

    text = regex.sub(
        _dflagize_subregional_py2_repl,
        text.encode("unicode-escape"))

    return text.decode("unicode-escape")


def _is_not_valid_tag(i):
    return i < 0xE0030 or i > 0xE007A or (i > 0xE0039 and i < 0xE0061)


def _dflagize_subregional_py2_repl(matchobj):
    plain = []

    skipped = ""
    group1 = matchobj.group(1)
    while group1.startswith("\U0001f3f4"):
        # This is a special case where there was a black flag followed
        # by a subregional flag. The pattern matches from the first black
        # flag, but the for loop would skip the whole regional flag,
        # because the second char would be a black flag again.
        # Save the skipped black flag and shorten the match:
        skipped += group1[0:10]
        group1 = group1[10:]

    for tag in group1.split("\\U")[1:]:
        i = int(tag, 16)
        if _is_not_valid_tag(i):
            return matchobj.group(0)  # Not a valid tag

        plain.append("%c" % (i - OFFSET_TAG))

    return skipped + ":" + plain[0] + plain[1] + "-" + "".join(plain[2:]) + ":"
