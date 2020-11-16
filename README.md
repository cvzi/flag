flag
====

[![foodemoji on PyPI](https://img.shields.io/pypi/v/emoji-country-flag.svg)](https://pypi.python.org/pypi/emoji-country-flag)
[![Python Versions](https://img.shields.io/pypi/pyversions/emoji-country-flag.svg)](https://pypi.python.org/pypi/emoji-country-flag)
[![Coverage Status](https://coveralls.io/repos/github/cvzi/flag/badge.svg?branch=master)](https://coveralls.io/github/cvzi/flag?branch=master)
[![Build Status](https://travis-ci.com/cvzi/flag.svg?branch=master)](https://travis-ci.com/cvzi/flag)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e897c2f701ee44f5aa36457d0ab1a84a)](https://app.codacy.com/app/cvzi/flag?utm_source=github.com&utm_medium=referral&utm_content=cvzi/flag&utm_campaign=Badge_Grade_Dashboard)
[![Maintainability](https://api.codeclimate.com/v1/badges/cf1f88720896db4d1b0a/maintainability)](https://codeclimate.com/github/cvzi/flag/maintainability)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cvzi_flag&metric=alert_status)](https://sonarcloud.io/dashboard?id=cvzi_flag)

Flag emoji for Python.  
Converts flag emoji to ASCII and other way round.

This is based on [http://schinckel.net/2015/10/29/unicode-flags-in-python/](http://web.archive.org/web/20180425063617/https://schinckel.net/2015/10/29/unicode-flags-in-python/) by [schinckel](https://github.com/schinckel/)

How it works
-----------

All the flag emoji are actually composed of two unicode letters. These are the 26 [regional indicator symbols](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol).

Alone they look like this:  
🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿

If you pair them up according to ISO 3166 some browsers and phones will display a flag.  
For example CZ is Czechia: 🇨 + 🇿 = 🇨🇿

So, to encode an ASCII code like `:NR:` to 🇳🇷, we just need to convert the ASCII **N** and **R** to the corresponding regional indicator symbols 🇳 and 🇷.  
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
    
    >>> flag.dflagize(u"Flag of Israel 🇮🇱")
    'Flag of Israel :IL:'
    
    >>> flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True)
    'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'
    
    >>> flag.dflagize(u"England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True)
    'England :gb-eng: is part of the UK :GB:'
```

Install
-------

`pip install emoji-country-flag`

See: [https://pypi.org/project/emoji-country-flag/](https://pypi.org/project/emoji-country-flag/)

Documentation
-------------

[![Documentation Status](https://readthedocs.org/projects/flag/badge/?version=latest)](https://flag.readthedocs.io/en/latest/?badge=latest)

Documentation at [https://flag.readthedocs.io](https://flag.readthedocs.io)
