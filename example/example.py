# -*- coding: UTF-8 -*-

import flag

print(flag.flagize(":DE:"))

print(flag.dflagize(u"🇩🇪"))

print(flag.flagize("Inline:ES:test"))

print(flag.dflagize(u"Inline🇪🇸test"))

print(flag.flagize(u"Other:NR:unicode👍test"))

print(flag.dflagize(u"Other🇳🇷unicode👍test"))

print(flag.flagize(u"❤️:IL:✡️"))

print(flag.dflagize(u"❤️🇮🇱✡️"))

print(flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True))

print(flag.dflagize(u"England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True))

print(flag.flagize_subregional("Flag of Scotland :gb-sct:"))

print(flag.dflagize_subregional(u"Flag of Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿"))
