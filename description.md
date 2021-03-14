flag
====

Flag emoji for Python.  
Converts flag emoji to ASCII and other way round.

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
```

Install
-------

`pip install emoji-country-flag`

See [https://pypi.org/project/emoji-country-flag/](https://pypi.org/project/emoji-country-flag/)

Documentation
-------------

See [https://flag.readthedocs.io](https://flag.readthedocs.io)

How it works
-----------

All the flag emoji are actually composed of two unicode letters. These are the 26 [regional indicator symbols](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol).

Alone they look like this:  
🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿

If you pair them up according to ISO 3166 some browsers and phones will display a flag.  
For example TW is Taiwan: 🇹 + 🇼 = 🇹🇼

So, to encode an ASCII code like `:TW:` to 🇹🇼, we just need to convert the ASCII **T** and **W** to the corresponding regional indicator symbols 🇹 and 🇼.  
To reverse it, we translate the regional indicator symbols back to ASCII letters.
