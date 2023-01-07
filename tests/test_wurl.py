import pytest

from wurl import Wurl



def test_wurl_concat():
    wu = Wurl("https://wordbrew.io")

    assert wu / "about" == "https://wordbrew.io/about"
    assert wu / "about" / "index.html" == "https://wordbrew.io/about/index.html"
    

def test_wurl_attributes():
    wu = Wurl("https://wordbrew.io")
    
    assert wu.scheme == "https"
    assert wu.domain == "wordbrew.io"
    
    assert (wu / "about" / "index.html").path == "/about/"
