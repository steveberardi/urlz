from typing import Any
from urllib.parse import urlparse, urljoin

class Wurl:

    def __init__(self, url: str):
        self.url = url
        self.parsed = urlparse(url)
    
    def __getattr__(self, attr) -> Any:
        # simple pass-through to the parsed result
        return getattr(self.parsed, attr)
    
    def __truediv__(self, other) -> "Wurl":
        return Wurl(url=urljoin(f"{self.url}/", other))

    def __str__(self):
        return self.url
    
    def __repr__(self):
        return self.url
    
    @property
    def domain(self):
        return self.parsed.netloc



