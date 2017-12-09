# -*- coding: UTF-8 -*-

import flag

print(flagize(":DE:"))

print(dflagize(u"🇩🇪"))

print(flagize("Inline:ES:test"))

print(dflagize(u"Inline🇪🇸test"))

print(flagize(u"Other:NR:unicode👍test"))

print(dflagize(u"Other🇳🇷unicode👍test"))

print(flagize(u"❤️:IL:✡️"))

print(dflagize(u"❤️🇮🇱✡️"))
