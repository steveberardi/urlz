# urlz
[![tests](https://github.com/steveberardi/urlz/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/steveberardi/urlz/actions/workflows/test.yml)

urlz is a simple URL parsing library that provides Pathlib-like usage to URLs in Python:

```python
>>>> from urlz import URL
>>>> url = URL("https://wordbrew.io")
>>>> str(url / "about" / "index.html")
'https://wordbrew.io/about/index.html'
```

It also provides a special URL-building function `urlify`:

```python
>>>> from urlz import urlify
>>>> urlify("https://wordbrew.io", "about", "index.html")
'https://wordbrew.io/about/index.html'

# with querystring params:
>>>> urlify("https://wordbrew.io", "search", params={"q": "hello world"})
'https://wordbrew.io/search?q=hello+world'
```

## TODO
- QS param helpers
- Path replacements (e.g. `url.replace(path="/new/stuff/")`)
- Validation helpers


## Alternatives
For more URL-parsing fun, check out these libraries:

- [furl](https://github.com/gruns/furl)
- [purl](https://github.com/codeinthehole/purl)
- [imurl](https://github.com/thesketh/imurl)
