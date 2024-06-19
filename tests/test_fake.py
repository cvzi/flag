import pytest

import flag
from flag import InvalidFlag, UnsupportedFlag


def test_fake():
    # Test fake data with a flag that is supported but not valid and a flag that is valid but not supported
    # This needs to be artifical data, because the actual data may change between Unicode releases

    flag.infos(extended=True)
    flag.data._flag_data["ZZ"] = {  # type: ignore
        "id_status": "region",
        "supported": True,
        "valid": False,
    }
    flag.data._flag_data["zzzzzz"] = {  # type: ignore
        "id_status": "subdivision",
        "supported": False,
        "valid": True,
    }

    flag.flag_safe("ZZ", unsupported="error", invalid="allow")
    with pytest.raises(InvalidFlag):
        flag.flag_safe("ZZ", unsupported="allow", invalid="error")

    flag.flag_safe("zzzzzz", unsupported="allow", invalid="error")
    with pytest.raises(UnsupportedFlag):
        flag.flag_safe("zzzzzz", unsupported="error", invalid="allow")

    assert flag.flagize(":ZZ:") != ":ZZ:"
    assert flag.flagize(":zz-zzzz:", subregions=True) != ":zz-zzzz:"

    f = flag.Flag(only_supported=True, only_valid=False, allow_subregions=True)
    assert f.flagize(":ZZ:") != ":ZZ:"
    assert f.flagize(":zz-zzzz:") == ":zz-zzzz:"

    f = flag.Flag(only_supported=False, only_valid=True, allow_subregions=True)
    assert f.flagize(":ZZ:") == ":ZZ:"
    assert f.flagize(":zz-zzzz:") != ":zz-zzzz:"

    f = flag.Flag(only_supported=True, only_valid=True, allow_subregions=True)
    assert f.flagize(":ZZ:") == ":ZZ:"
    assert f.flagize(":zz-zzzz:") == ":zz-zzzz:"

    # Revert database
    del flag.data._flag_data["ZZ"]  # type: ignore
    del flag.data._flag_data["zzzzzz"]  # type: ignore
