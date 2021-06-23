# -*- coding: UTF-8 -*-


import sys

try:
    import flag as my_module
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    import flag as my_module
    print("Imported flag from %s" % os.path.abspath(os.path.join(include, "flag")))
from flag import *

def test_import():
    assert "🇩🇪" == my_module.flagize(":DE:")

    assert ":DE:" == my_module.dflagize("🇩🇪")

    assert "Inline🇪🇸test" == my_module.flagize("Inline:ES:test")

    assert "Inline:ES:test" == my_module.dflagize("Inline🇪🇸test")

    assert "Other🇳🇷unicode👍test" == my_module.flagize("Other:NR:unicode👍test")

    assert "Other:NR:unicode👍test" == my_module.dflagize("Other🇳🇷unicode👍test")

    assert "❤️🇮🇱✡️" == my_module.flagize("❤️:IL:✡️")

    assert "❤️:IL:✡️" == my_module.dflagize("❤️🇮🇱✡️")

    assert "🇮🇱" == my_module.flag("IL")

    assert "🇮🇱" == my_module.Flag(".", ".").flagize(".IL.")


def test_import_star():
    assert "🇩🇪" == flagize(":DE:")

    assert ":DE:" == dflagize("🇩🇪")

    assert "Inline🇪🇸test" == flagize("Inline:ES:test")

    assert "Inline:ES:test" == dflagize("Inline🇪🇸test")

    assert "Other🇳🇷unicode👍test" == flagize("Other:NR:unicode👍test")

    assert "Other:NR:unicode👍test" == dflagize("Other🇳🇷unicode👍test")

    assert "❤️🇮🇱✡️" == flagize("❤️:IL:✡️")

    assert "❤️:IL:✡️" == dflagize("❤️🇮🇱✡️")

    assert "🇮🇱" == flag("IL")

    assert "🇮🇱" == Flag(".", ".").flagize(".IL.")

def runall():
    for fname, f in list(globals().items()):
        if fname.startswith('test_'):
            print("%s()" % fname)
            f()
            print("Ok.")


if __name__ == '__main__':
    if 'idlelib' in sys.modules:
        print("Please run this file in a console!")

    runall()
