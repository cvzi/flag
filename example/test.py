# -*- coding: UTF-8 -*-

import flag

assert u"🇩🇪" == flagize(":DE:")

assert ":DE:" == dflagize(u"🇩🇪")

assert u"Inline🇪🇸test" == flagize("Inline:ES:test")

assert "Inline:ES:test" == dflagize(u"Inline🇪🇸test")

assert u"Other🇳🇷unicode👍test" == flagize(u"Other:NR:unicode👍test")

assert u"Other:NR:unicode👍test" == dflagize(u"Other🇳🇷unicode👍test")

assert u"❤️🇮🇱✡️" == flagize(u"❤️:IL:✡️")

assert u"❤️:IL:✡️" == dflagize(u"❤️🇮🇱✡️")
