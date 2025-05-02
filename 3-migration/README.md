# Migration

## starting from a requirements.txt

If you alraedy have a requirements.txt file you can use that as a starting point

```bash
uv add -r requirements.txt
```

`venv` and `pip` can also be easily transitioned to use `uv` under the hood

```bash
uv venv --python 3.11 my-name
. my-name/bin/activate
uv pip install ruff
uv pip install "git+https://github.com/astral-sh/ruff"
uv pip install "ruff @ ./projects/ruff"
```

## starting from a pyproject.toml

In my experience it is easiest to create one using `uv init` and then manually modifying the dependencies entry. Followed by `uv lock` and `uv sync`.

```
[project]
dependencies = [
  "httpx",
  "ruff>=0.3.0"
]
```


## System level installs

Instead of creating a virtual environment you might want to do a system level install
```
uv pip install --system pandas
```

This is useful when doing Dockerfile isntallations

## uv with jupyter notebooks

https://docs.astral.sh/uv/guides/integration/jupyter/