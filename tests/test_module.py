import flag as my_module
from flag import flagize, flag, dflagize, Flag


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
