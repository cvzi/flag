import flag

print(flag.flagize(":DE:"))

print(flag.dflagize("🇩🇪"))

print(flag.flagize("Inline:ES:test"))

print(flag.dflagize("Inline🇪🇸test"))

print(flag.flagize("Other:NR:unicode👍test"))

print(flag.dflagize("Other🇳🇷unicode👍test"))

print(flag.flagize("❤️:IL:✡️"))

print(flag.dflagize("❤️🇮🇱✡️"))

print(flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True))

print(flag.dflagize("England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True))

print(flag.flagize_subregional("Flag of Scotland :gb-sct:"))

print(flag.dflagize_subregional("Flag of Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿"))

my_flags = flag.Flag(only_supported=True, allow_subregions=True)
print(my_flags.flagize("Convert actual flags like :US: but not unsupported ones like :XX:"))
