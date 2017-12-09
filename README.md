flag
====

Flag emoji for Python.  
Converts flag emoji to ASCII and other way round.

This is based on http://schinckel.net/2015/10/29/unicode-flags-in-python/ by [schinckel](https://github.com/schinckel/)


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

    >>> flag.flagize("Flag of Israel :IL:")
    'Flag of Israel 🇮🇱'
    
    >>> flag.dflagize(u"Flag of Israel 🇮🇱")
    'Flag of Israel :IL:'
```


