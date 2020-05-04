import pytest
from pythonic_grage_band.garage_band import Musician,Guitarist,Drummer,Bassist

def test_abstract_musician():
    with pytest.raises(TypeError):
        Musician("?","?")

def test_Band_instance_count():
    a = Guitarist()
    b = Bassist()
    c = Drummer()
    assert Musician.count == 3

def test_guitarist_with_unknown_name():
    dntno = Guitarist()
    actual = dntno.name
    expected = "unknown"
    assert actual == expected

def test_guitarist():
    jimmy = Guitarist("Jimmy Page")
    assert jimmy.name == "Jimmy Page"
    assert jimmy.instrument == "Guitar"
    assert jimmy.play_solo() =="heart melting guitar wailing"

def test_bassist():
    cliff = Bassist("Cliff Burton")
    assert cliff.name =="Cliff Burton"
    assert cliff.instrument == "Bass"
    assert cliff.play_solo() =="thum, thupy"

def test_Drummer():
    john = Drummer("John Bonhan")
    assert john.name == "John Bonhan"
    assert john.instrument =="Drumm"
    assert john.play_solo() =="crash boom"

def test_Drummer_play_solo():
    x = Drummer()
    x.play_solo()
    assert x.play_solo() =="crash boom"

""" @pytest.fixture
def some_band():
    nirvana = Band("Nirvana",[
        Guitarist ("Jimmy Page"),
        Bassist("Cliff Burton"),
        Drummer("John Bonhan")
         ])
    return """
