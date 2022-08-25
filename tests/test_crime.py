from pickle import FALSE
from api import Crime

def test_Crime_constructor():
    crime_one = Crime(id = 1)
    assert crime_one.__dict__ == {'id': 1}

