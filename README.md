flag
====

[![foodemoji on PyPI](https://img.shields.io/pypi/v/emoji-country-flag.svg)](https://pypi.python.org/pypi/emoji-country-flag)
[![Python Versions](https://img.shields.io/pypi/pyversions/emoji-country-flag.svg)](https://pypi.python.org/pypi/emoji-country-flag)
[![Coverage Status](https://coveralls.io/repos/github/cvzi/flag/badge.svg?branch=main)](https://coveralls.io/github/cvzi/flag?branch=main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6030d5de808c4fe2b2216699f1a7eafb)](https://app.codacy.com/gh/cvzi/flag/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/cf1f88720896db4d1b0a/maintainability)](https://codeclimate.com/github/cvzi/flag)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cvzi_flag&metric=alert_status)](https://sonarcloud.io/dashboard?id=cvzi_flag)

Flag emoji for Python.  
Converts flag emoji to ASCII and other way round.

This is based on [http://schinckel.net/2015/10/29/unicode-flags-in-python/](http://web.archive.org/web/20180425063617/https://schinckel.net/2015/10/29/unicode-flags-in-python/) by [schinckel](https://github.com/schinckel/)

How it works
------------

All the flag emoji are actually composed of two unicode letters. These are the 26 [regional indicator symbols](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol).

Alone they look like this:  
🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿

If you pair them up according to ISO 3166 some browsers and phones will display a flag.  
For example TW is Taiwan: 🇹 + 🇼 = 🇹🇼

So, to encode an ASCII code like `:TW:` to 🇹🇼, we just need to convert the ASCII **T** and **W** to the corresponding regional indicator symbols 🇹 and 🇼.  
To reverse it, we translate the regional indicator symbols back to ASCII letters.

Example
-------

```python
    >>> import flag
    
    >>> flag.flag("IL")
    '🇮🇱'
    
    >>> flag.flag("GBENG")
    '🏴󠁧󠁢󠁥󠁮󠁧󠁿'
    
    >>> flag.flagize("Flag of Israel :IL:")
    'Flag of Israel 🇮🇱'
    
    >>> flag.dflagize("Flag of Israel 🇮🇱")
    'Flag of Israel :IL:'
    
    >>> flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True)
    'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'
    
    >>> flag.dflagize("England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True)
    'England :gb-eng: is part of the UK :GB:'

    >>> my_flags = flag.Flag(only_supported=True, allow_subregions=True)
    >>> my_flags.flagize("Convert actual flags like :US: but not unsupported ones like :XX:")
    'Convert actual flags like 🇺🇸 but not unsupported ones like :XX:'
```

Install
-------

`pip install emoji-country-flag`

See: [https://pypi.org/project/emoji-country-flag/](https://pypi.org/project/emoji-country-flag/)

Python 3.10 or higher is required for the latest release.
The last release for Python 3.7 to 3.9 was [v1.3.2](https://github.com/cvzi/flag/releases/tag/v1.3.2).
The last release for Python 2.7, 3.4 and 3.5 was [v1.2.4](https://github.com/cvzi/flag/releases/tag/v1.2.4).

Documentation
-------------

[![Documentation Status](https://readthedocs.org/projects/flag/badge/?version=latest)](https://flag.readthedocs.io/en/latest/?badge=latest)

Documentation at [https://flag.readthedocs.io](https://flag.readthedocs.io)
