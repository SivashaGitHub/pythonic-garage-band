from pythonic_grage_band.garage_band_class import Band,Musician,Guitarist,Drummer,Bassist
import pytest

@pytest.fixture
def one_band():
    #return Band.create(one_band_data)
  
    some_band = Band ("Nirvana",[Guitarist("Kurt"),
            Bassist("Krist"), Drummer("Dave")])

    return some_band        

def test_band_name():
    nirvana =Band("Nirvana",[])
    assert nirvana.name == "Nirvana"

def test_guitarist():
    jimi =Guitarist("Jimi")
    assert jimi.name =="Jimi"
    assert jimi.get_instrument() == "guitar"

def test_bassist():
    fale =Bassist("Fale")
    assert fale.name =="Fale"
    assert fale.get_instrument() == "Bass"

def test_drummer():
    ginger =Drummer("Ginger")
    assert ginger.name =="Ginger"
    assert ginger.get_instrument() == "Drums"

def test_individual_solos(one_band):
    for member in one_band.members:
        if member.get_instrument() == "Guitar":
            assert member.play_solo() == "Face melting guitar solo"
        elif member.get_instrument() == "Bass":
            assert member.play_solo() == "bom dhu  bom bom"
        elif member.get_instrument() == "Durms":
            assert member.play_solo() == "rattle boom crash"


def test_solos_for_whole_band(one_band):
    solos = one_band.play_solos()
    assert len(solos) == 3
    assert solos[0] =="Face melting guitar solo"
    assert solos[1] =="bom dhu  bom bom"
    assert solos[2] =="rattle boom crash"


#@pytest.mark.skip("pending")
def test_band_members(one_band):
    for member in one_band.members:
        assert isinstance(member,Musician)







