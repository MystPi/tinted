# tinted
![PyPI - Downloads](https://img.shields.io/pypi/dm/tinted) ![PyPI](https://img.shields.io/pypi/v/tinted) ![PyPI - License](https://img.shields.io/pypi/l/tinted) ![Python - Version](https://img.shields.io/badge/python-3%2B-yellow)

Give your print output the tint it deserves! Give colors, styles, and more to the console, all with a simple markup language.

## Installation
```bash
pip install tinted
```

## Usage
From a Python script:
```python
from tinted import tint

print(tint('Hello, [bold]world![/]'))
```

From a shell:
```bash
echo "Hello, [bold]world![/]" | tinted

# OR

tinted file.txt
```

## Basic syntax

Strings can be styled easily with an HTML-like syntax.

```
[bold][blue]Tinted[/] is [underline]cool[/]![/]
```

`[...]` denotes a starting tag, where `...` is a tag name.

`[/...]` indicates a closing tag. Tag names are not necessary, and are ignored if they are included.

## Tags

All of the available tags are listed below.

### Colors
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- lightgray
- darkgray
- lightred
- lightgreen
- lightyellow
- lightblue
- lightmagenta
- lightcyan
- white

### Background colors
Prefix any of the colors above with `bg`. Eg. `bglightred`.

### Styles
- bold
- dim
- italic
- underline
- blink
- reverse
- hidden

## Escaping tags
To escape a tag, simply include `[]` somewhere inside.

`[[]blue]These tags will be shown[[]/]`
