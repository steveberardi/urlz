from typing import Any
from urllib.parse import urlparse, urljoin, urlencode


class URL:
    def __init__(self, url: str, normalize=True):
        self.url = url
        self.parsed = urlparse(url)
        self.normalized = normalize
        if normalize:
            self._normalize()

    def __getattr__(self, attr) -> Any:
        # simple pass-through to the parsed result
        return getattr(self.parsed, attr)

    def __truediv__(self, other) -> "URL":
        return URL(url=urljoin(f"{self.url}/", other))

    def __str__(self) -> str:
        return self.url

    def __repr__(self) -> str:
        return f"URL('{self.url}')"

    @property
    def domain(self) -> str:
        return self.parsed.netloc

    def replace(self, **kwargs) -> "URL":
        new_url = self.parsed._replace(**kwargs).geturl()
        return URL(new_url, normalize=self.normalized)

    def _reparse(self) -> None:
        self.parsed = urlparse(self.url)

    def _normalize(self) -> None:
        """Add a trailing slash if url is to root domain"""
        if not self.parsed.path:
            self.url = self.parsed._replace(path="/").geturl()
            self._reparse()


def urlify(*args, **kwargs) -> str:
    """Creates a URL by joining all args"""
    params = kwargs.get("params") or {}
    url = ""

    if args:
        url = args[0]
        for arg in args[1:]:
            url = urljoin(f"{url}/", arg)

    if params:
        encoded = urlencode(params)
        if url:
            url = f"{url}?{encoded}"
        else:
            url = encoded

    return url
