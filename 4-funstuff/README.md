# self instaling scripts

Taken from https://treyhunner.com/2024/12/lazy-self-installing-python-scripts-with-uv/

Something neat you can do in a system that already has uv are scripts that manage their own environments and dependencies if you place this in the header

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas",
# ]
# ///
```