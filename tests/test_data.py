import flag


def test_data_supported():
    assert flag.info("ES")["id_status"] == "regular"

    assert flag.info("DK")["supported"]
    
    assert flag.info("JP")["valid"]

def test_data_infos():

    d = flag.infos()

    assert d["NZ"]["valid"]

    assert d["NL"]["supported"]

    ext = flag.infos(extended=True)

    assert not ext["gbstb"]["supported"]

    assert ext["IT"]["valid"]


def test_extended():
    assert flag.info("si162", extended=True)["id_status"] == "regular"
    assert flag.info("almr", extended=True)["id_status"] == "deprecated"


def test_version():
    versions = flag.version()
    assert int(versions["module"].split(".")[0]) >= 2
    assert int(versions["emoji"].split(".")[0]) >= 15
    assert int(versions["cldr"].split(".")[0]) >= 45
