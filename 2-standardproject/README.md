# Use uv from scratch

## install uv

The easiest is to install from pip

```bash
pip install uv
```

alternatively install from the standalone script

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Check https://docs.astral.sh/uv/#highlights for references

For the purposes of this example you can also use the provided dockerfile


## running standalone UV from scratch


```bash
uv init
uv add pandas
uv run test.py
```

All packages are isntalled to .venv which is also virtualenv compliant

```bash
. .venv/bin/activate
python test.py
```

## which project files to commit?

- pyproject.toml
- uv.lock


## How to install packages from an existing project I pulled from github?

If the project has a uv.lock and pyproject.toml

```
uv sync
```

## More functionality

### Install from github

```
uv add git+https://github.com/psf/requests
```

### Install with a constraint

```bash
uv add 'requests==2.31.0'
```

### Run commands that come from a package

``` bash
$ uv add flask
$ uv run -- flask run -p 3000
```
