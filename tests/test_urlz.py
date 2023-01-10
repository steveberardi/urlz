import pytest

from urlz import URL

@pytest.fixture
def url():
    yield URL("https://wordbrew.io")

def test_url_concat(url):
    assert str(url / "about") == "https://wordbrew.io/about"
    assert str(url / "about" / "index.html") == "https://wordbrew.io/about/index.html"
    

def test_url_attributes(url):
    assert url.scheme == "https"
    assert url.domain == "wordbrew.io"
    
    assert (url / "about" / "index.html").path == "/about/index.html"

def test_url_normalize():
    normalized = URL("https://wordbrew.io")
    assert str(normalized) == "https://wordbrew.io/"

    not_normalized = URL("https://wordbrew.io", normalize=False)
    assert str(not_normalized) == "https://wordbrew.io"

def test_url_replace():
    u = URL("https://wordbrew.io/about/index.html")
    assert str(u.replace(scheme="http")) == "http://wordbrew.io/about/index.html"
