# urlz

urlz is a simple URL parsing library that provides Pathlib-like usage to URLs in Python:

```python
>>>> from urlz import URL
>>>> url = URL("https://wordbrew.io")
>>>> url / "about" / "index.html"
https://wordbrew.io/about/index.html

```

## TODO
- QS param helpers
- Path replacements (e.g. `url.replace(path="/new/stuff/")`)
- Validation helpers


## Alternatives

urlz was primarily inspired by [furl](https://github.com/gruns/furl), but along the way I've also discovered these useful URL-parsing libraries:

- [furl](https://github.com/gruns/furl)
- [purl](https://github.com/codeinthehole/purl)
- [imurl](https://github.com/thesketh/imurl)
