# fix_my_functions

Working title.

A Python code formatter which applies a single transform: function signature tabulation. A formatting style designed to read type annotations with ease. Based on [`redbaron`](https://github.com/PyCQA/redbaron), which in turn wraps the [`baron`](https://github.com/PyCQA/baron) parser.

It formats a functions to look like the following:

```python
def spaghetti(self,
        determinant           : int,                       # foo
        fraction              : float      = 42,
        hidden_features       : float      = 42,           # bar
        hyper_determinant                  = None,
        hyper_fraction        : str | None = "spaghetti",  # baz
        hyper_hidden_features : str | None = "spaghetti",
        ) -> bool | None:
    pass
```

Notable features of this formatting, and why I like it:

* Doubly indented arguments and return annotations.
	* Visually separates the function arguments from the function body,
	* In a way most naive text editors are able to fold the whole function.
* The `self` and `cls` argument is folded onto the same line as the function name.
	* Saves space
* Forced trailing comma.
	* Makes it easy to reorder lines.
* Tabulated formatting
	* argument names, then type annotations, then default values, then comments
	* Very easy to seek and read

The bad:

* Changes in column width touches a lot of lines, which puts the `git blame` on you.
* A bit limited when restricted to 80 columns, but workable

## Features

- _Comment preservation:_ Tries to preserve comments.
- _Iterative mode:_ apply only a single transformation at a time, inspired by `git add --patch`.


## Status

I made the core of this in a day, with the intention of developing it further.
I then discovered that [`baron`](https://github.com/PyCQA/baron) has issues such as [this](https://github.com/PyCQA/redbaron/issues/210), [this](https://github.com/PyCQA/baron/issues/170) and [this](https://github.com/PyCQA/baron/issues/137), making it impractical to use in production.

Can this formatter be rewritten using parso?
Can it be added as a knob to yapf? Maybe!
