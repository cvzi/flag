.. flag documentation master file, created by
   sphinx-quickstart on Fri Oct 26 10:43:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

flag
~~~~

Flag emoji for Python.

Converts flag emoji to ASCII and other way round.

`Source on Github <https://github.com/cvzi/flag>`_

This is based on `http://schinckel.net/2015/10/29/unicode-flags-in-python/ <http://schinckel.net/2015/10/29/unicode-flags-in-python/>`_ by `schinckel <https://github.com/schinckel/>`_

Example
=======

.. code-block:: python

    >>> import flag

    >>> flag.flagize("Flag of Israel :IL:")
    'Flag of Israel 🇮🇱'

    >>> flag.dflagize(u"Flag of Israel 🇮🇱")
    'Flag of Israel :IL:'

    >>> flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True)
    'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'

    >>> flag.dflagize(u"England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True)
    'England :gb-eng: is part of the UK :GB:'

Install
=======

.. code-block:: shell

   pip install emoji-country-flag

See: `https://pypi.org/project/emoji-country-flag/ <https://pypi.org/project/emoji-country-flag/>`_

How it works
============

All the flag emoji are actually composed of two unicode letters. These are the 26 `regional indicator symbols <https://en.wikipedia.org/wiki/Regional_Indicator_Symbol>`_.

Alone they look like this:  
🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿

If you pair them up according to ISO 3166 some browsers and phones will display a flag.  
For example CZ is Czechia: 🇨 + 🇿 = 🇨🇿

So, to encode an ASCII code like ``:NR:`` to 🇳🇷, we just need to convert the ASCII **N** and **R** to the corresponding regional indicator symbols 🇳 and 🇷.
To reverse it, we translate the regional indicator symbols back to ASCII letters.

`How do subregional flags work? <How subregional flags work_>`_

Functions
=========
.. currentmodule:: flag
.. autofunction:: flagize
.. autofunction:: dflagize
.. autofunction:: flagize_subregional
.. autofunction:: dflagize_subregional

Supported emojis and patterns
=============================

(List may be incomplete)

========    ========
Code        Emoji
========    ========
``:UN:``     🇺🇳
``:AC:``     🇦🇨
``:AD:``     🇦🇩
``:AE:``     🇦🇪
``:AF:``     🇦🇫
``:AG:``     🇦🇬
``:AI:``     🇦🇮
``:AL:``     🇦🇱
``:AM:``     🇦🇲
``:AO:``     🇦🇴
``:AQ:``     🇦🇶
``:AR:``     🇦🇷
``:AS:``     🇦🇸
``:AT:``     🇦🇹
``:AU:``     🇦🇺
``:AW:``     🇦🇼
``:AX:``     🇦🇽
``:AZ:``     🇦🇿
``:BA:``     🇧🇦
``:BB:``     🇧🇧
``:BD:``     🇧🇩
``:BE:``     🇧🇪
``:BF:``     🇧🇫
``:BG:``     🇧🇬
``:BH:``     🇧🇭
``:BI:``     🇧🇮
``:BJ:``     🇧🇯
``:BL:``     🇧🇱
``:BM:``     🇧🇲
``:BN:``     🇧🇳
``:BO:``     🇧🇴
``:BQ:``     🇧🇶
``:BR:``     🇧🇷
``:BS:``     🇧🇸
``:BT:``     🇧🇹
``:BV:``     🇧🇻
``:BW:``     🇧🇼
``:BY:``     🇧🇾
``:BZ:``     🇧🇿
``:CA:``     🇨🇦
``:CC:``     🇨🇨
``:CD:``     🇨🇩
``:CF:``     🇨🇫
``:CG:``     🇨🇬
``:CH:``     🇨🇭
``:CI:``     🇨🇮
``:CK:``     🇨🇰
``:CL:``     🇨🇱
``:CM:``     🇨🇲
``:CN:``     🇨🇳
``:CO:``     🇨🇴
``:CP:``     🇨🇵
``:CR:``     🇨🇷
``:CU:``     🇨🇺
``:CV:``     🇨🇻
``:CW:``     🇨🇼
``:CX:``     🇨🇽
``:CY:``     🇨🇾
``:CZ:``     🇨🇿
``:DE:``     🇩🇪
``:DG:``     🇩🇬
``:DJ:``     🇩🇯
``:DK:``     🇩🇰
``:DM:``     🇩🇲
``:DO:``     🇩🇴
``:DZ:``     🇩🇿
``:EA:``     🇪🇦
``:EC:``     🇪🇨
``:EE:``     🇪🇪
``:EG:``     🇪🇬
``:EH:``     🇪🇭
``:ER:``     🇪🇷
``:ES:``     🇪🇸
``:ET:``     🇪🇹
``:EU:``     🇪🇺
``:FI:``     🇫🇮
``:FJ:``     🇫🇯
``:FK:``     🇫🇰
``:FM:``     🇫🇲
``:FO:``     🇫🇴
``:FR:``     🇫🇷
``:GA:``     🇬🇦
``:GB:``     🇬🇧
``:GD:``     🇬🇩
``:GE:``     🇬🇪
``:GF:``     🇬🇫
``:GG:``     🇬🇬
``:GH:``     🇬🇭
``:GI:``     🇬🇮
``:GL:``     🇬🇱
``:GM:``     🇬🇲
``:GN:``     🇬🇳
``:GP:``     🇬🇵
``:GQ:``     🇬🇶
``:GR:``     🇬🇷
``:GS:``     🇬🇸
``:GT:``     🇬🇹
``:GU:``     🇬🇺
``:GW:``     🇬🇼
``:GY:``     🇬🇾
``:HK:``     🇭🇰
``:HM:``     🇭🇲
``:HN:``     🇭🇳
``:HR:``     🇭🇷
``:HT:``     🇭🇹
``:HU:``     🇭🇺
``:IC:``     🇮🇨
``:ID:``     🇮🇩
``:IE:``     🇮🇪
``:IL:``     🇮🇱
``:IM:``     🇮🇲
``:IN:``     🇮🇳
``:IO:``     🇮🇴
``:IQ:``     🇮🇶
``:IR:``     🇮🇷
``:IS:``     🇮🇸
``:IT:``     🇮🇹
``:JE:``     🇯🇪
``:JM:``     🇯🇲
``:JO:``     🇯🇴
``:JP:``     🇯🇵
``:KE:``     🇰🇪
``:KG:``     🇰🇬
``:KH:``     🇰🇭
``:KI:``     🇰🇮
``:KM:``     🇰🇲
``:KN:``     🇰🇳
``:KP:``     🇰🇵
``:KR:``     🇰🇷
``:KW:``     🇰🇼
``:KY:``     🇰🇾
``:KZ:``     🇰🇿
``:LA:``     🇱🇦
``:LB:``     🇱🇧
``:LC:``     🇱🇨
``:LI:``     🇱🇮
``:LK:``     🇱🇰
``:LR:``     🇱🇷
``:LS:``     🇱🇸
``:LT:``     🇱🇹
``:LU:``     🇱🇺
``:LV:``     🇱🇻
``:LY:``     🇱🇾
``:MA:``     🇲🇦
``:MC:``     🇲🇨
``:MD:``     🇲🇩
``:ME:``     🇲🇪
``:MF:``     🇲🇫
``:MG:``     🇲🇬
``:MH:``     🇲🇭
``:MK:``     🇲🇰
``:ML:``     🇲🇱
``:MM:``     🇲🇲
``:MN:``     🇲🇳
``:MO:``     🇲🇴
``:MP:``     🇲🇵
``:MQ:``     🇲🇶
``:MR:``     🇲🇷
``:MS:``     🇲🇸
``:MT:``     🇲🇹
``:MU:``     🇲🇺
``:MV:``     🇲🇻
``:MW:``     🇲🇼
``:MX:``     🇲🇽
``:MY:``     🇲🇾
``:MZ:``     🇲🇿
``:NA:``     🇳🇦
``:NC:``     🇳🇨
``:NE:``     🇳🇪
``:NF:``     🇳🇫
``:NG:``     🇳🇬
``:NI:``     🇳🇮
``:NL:``     🇳🇱
``:NO:``     🇳🇴
``:NP:``     🇳🇵
``:NR:``     🇳🇷
``:NU:``     🇳🇺
``:NZ:``     🇳🇿
``:OM:``     🇴🇲
``:PA:``     🇵🇦
``:PE:``     🇵🇪
``:PF:``     🇵🇫
``:PG:``     🇵🇬
``:PH:``     🇵🇭
``:PK:``     🇵🇰
``:PL:``     🇵🇱
``:PM:``     🇵🇲
``:PN:``     🇵🇳
``:PR:``     🇵🇷
``:PS:``     🇵🇸
``:PT:``     🇵🇹
``:PW:``     🇵🇼
``:PY:``     🇵🇾
``:QA:``     🇶🇦
``:RE:``     🇷🇪
``:RO:``     🇷🇴
``:RS:``     🇷🇸
``:RU:``     🇷🇺
``:RW:``     🇷🇼
``:SA:``     🇸🇦
``:SB:``     🇸🇧
``:SC:``     🇸🇨
``:SD:``     🇸🇩
``:SE:``     🇸🇪
``:SG:``     🇸🇬
``:SH:``     🇸🇭
``:SI:``     🇸🇮
``:SJ:``     🇸🇯
``:SK:``     🇸🇰
``:SL:``     🇸🇱
``:SM:``     🇸🇲
``:SN:``     🇸🇳
``:SO:``     🇸🇴
``:SR:``     🇸🇷
``:SS:``     🇸🇸
``:ST:``     🇸🇹
``:SV:``     🇸🇻
``:SX:``     🇸🇽
``:SY:``     🇸🇾
``:SZ:``     🇸🇿
``:TA:``     🇹🇦
``:TC:``     🇹🇨
``:TD:``     🇹🇩
``:TF:``     🇹🇫
``:TG:``     🇹🇬
``:TH:``     🇹🇭
``:TJ:``     🇹🇯
``:TK:``     🇹🇰
``:TL:``     🇹🇱
``:TM:``     🇹🇲
``:TN:``     🇹🇳
``:TO:``     🇹🇴
``:TR:``     🇹🇷
``:TT:``     🇹🇹
``:TV:``     🇹🇻
``:TW:``     🇹🇼
``:TZ:``     🇹🇿
``:UA:``     🇺🇦
``:UG:``     🇺🇬
``:UM:``     🇺🇲
``:US:``     🇺🇸
``:UY:``     🇺🇾
``:UZ:``     🇺🇿
``:VA:``     🇻🇦
``:VC:``     🇻🇨
``:VE:``     🇻🇪
``:VG:``     🇻🇬
``:VI:``     🇻🇮
``:VN:``     🇻🇳
``:VU:``     🇻🇺
``:WF:``     🇼🇫
``:WS:``     🇼🇸
``:XK:``     🇽🇰
``:YE:``     🇾🇪
``:YT:``     🇾🇹
``:ZA:``     🇿🇦
``:ZM:``     🇿🇲
``:ZW:``     🇿🇼
========    ========


Subregional flags
=================

The only widely supported subregional flags are currently: England, Scottland and Wales (as of iOS 12 and Android 9).

============        ========
Code                Emoji
============        ========
``:gb-sct:``         🏴󠁧󠁢󠁳󠁣󠁴󠁿
``:gb-wls:``         🏴󠁧󠁢󠁷󠁬󠁳󠁿
``:gb-eng:``         🏴󠁧󠁢󠁥󠁮󠁧󠁿
``:us-tx:``          🏴󠁵󠁳󠁴󠁸󠁿
============        ========

| WhatsApp offers one other state flag: Texas.
| If you use WhatsApp's emoji panel to select the Texas flag, WhatsApp uses 🇽🇹 i.e. `flagize(":XT:")` for Texas. This code "XT" is specified by Unicode as "excluded" meaning it is explicitly for private use and can be defined by anyone. Therefore, it is likely not diplayed as the Texas flag on other platforms.
| But WhatsApp also recognizes the flag emoji tag sequence `flagize(":us-tx:", subregions=True)` and displays the same flag.


How subregional flags work
==========================

They work very similar to the country flags. The ASCII codes are transformed by replacing them with specific codepoints that are called "tags".

.. Note::

    :``black_flag_emoji`` followed by ``region_code_in_tag`` followed by ``cancel_tag``:    The basic format for a tag flag
    :``black_flag_emoji``:    U+1F3F4 ( 🏴 )
    :``cancel_tag``:    U+E007F (invisible, signifies the end of the flag code)
    :``region_code_in_tag``:
        It is formed using the abbreviation defined in `ISO 3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:GB#Countries_and_province>`_ and adding 0xE0000 to every ASCII value of the code.
        For example England is GB-ENG.

        A full list of valid codes can be found here: `github.com/unicode-org/.../subdivisions/en.xml <https://github.com/unicode-org/cldr/blob/master/common/subdivisions/en.xml>`_

        It's also possible to use a 3-digit-code from `github.com/unicode-org/.../UnMacroRegions.txt <https://github.com/unicode-org/cldr/blob/master/tools/java/org/unicode/cldr/util/data/UnMacroRegions.txt>`_


Example:
--------
| Englang is ``GB-ENG`` in ISO 3166-2.
| We drop the hyphen and make it lowercase to get ``gbeng``.
| To transform this to "tags", we need to add the value 0xE0000 = 917504 to every unicode value of ``gbeng``:

| ``g`` is unicode 0x67 or decimal 103, so 103 + 917504 = 917607 or 0xE0067
| ``b`` is 0x62 and becomes 0xE0062
| ``e`` is 0x65 and becomes 0xE0065
| ``n`` is 0x6E and becomes 0xE006E
| ``g`` is 0x67 and becomes 0xE0067

So together it's:

.. code-block::

                          g        b        e        n        g
    ASCII:                0x67     0x62     0x65     0x6E     0x67
    Tags:   0x1F3F4    0xE0067  0xE0062  0xE0065  0xE006E  0xE0067  0xE007F
            black_flag                                             cancel_tag

Unlike the regional indicator symbols, tags are not rendered on incompatible system, they will simply be invisible and have no width.
So, if the particular flag is not supported or if tag flags are not supported at all, the only visible chararacter will be a black flag.


.. hint::
   If you don't see the flags in your browser, try with your phone

   |QR| https://flag.readthedocs.org

.. |QR| image:: _static/qr.png
   :alt: QR Code containg https://flag.readthedocs.org
   :target: https://flag.readthedocs.org

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

