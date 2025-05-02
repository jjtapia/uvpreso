# Getting started


## The Problem

Setting up Python environments and installing packages can be slow and frustrating between virtual environments and package resolution.

## The Solution: UV

UV is a modern Python package manager written in Rust that dramatically speeds up your workflow.

## Let's try it out

```
docker build . -t uvpreso2
docker run --rm -ti --entrypoint /bin/bash  uvpreso0
```

For the purposes of the demo I will use my own system.

Let's see what the workflow looks like

- With pip: 
```
pip install pandas
```
- With uv: 

```
uv add pandas
```

Let's try out just how fast each one is in your system.


## What is uv

uv is a package manager written in Rust that can serve almost as a drop in replacement for venv+pip. It is blazing fast in resolving project dependencies, and can be used for many things on top of that (managing multiple python versions, project publishing. etc)