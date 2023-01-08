import pytest

from wurl import Wurl

@pytest.fixture
def wu():
    yield Wurl("https://wordbrew.io")

def test_wurl_concat(wu):
    assert str(wu / "about") == "https://wordbrew.io/about"
    assert str(wu / "about" / "index.html") == "https://wordbrew.io/about/index.html"
    

def test_wurl_attributes(wu):
    assert wu.scheme == "https"
    assert wu.domain == "wordbrew.io"
    
    assert (wu / "about" / "index.html").path == "/about/index.html"

def test_wurl_normalize():
    normalized = Wurl("https://wordbrew.io")
    assert str(normalized) == "https://wordbrew.io/"

    not_normalized = Wurl("https://wordbrew.io", normalize=False)
    assert str(not_normalized) == "https://wordbrew.io"
