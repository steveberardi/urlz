import pytest

from urlz import URL, urlify

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

    u = URL("https://wordbrew.io/about/index.html")
    assert str(u.replace(path="other")) == "https://wordbrew.io/other"

def test_urlify():
    result = urlify("https://wordbrew.io", "about", "index.html")
    assert result == "https://wordbrew.io/about/index.html"

def test_urlify_with_params():
    result = urlify(
        "https://wordbrew.io",
        "search",
        params={
            "q": "hello world",
            "more": "123@99"
        }
    )
    assert result == "https://wordbrew.io/search?q=hello+world&more=123%4099"
