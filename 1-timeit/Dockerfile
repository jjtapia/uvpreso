FROM python:3.12-slim

# Install necessary tools

# Install UV
RUN pip install uv virtualenv

RUN apt-get update && apt-get install -y wget curl bzip2 ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
ENV CONDA_DIR opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

# Add conda to path
ENV PATH="$PATH:/opt/conda/bin"

# # Initialize conda for shell interaction and update
RUN conda init bash && \
    conda update -n base -c defaults conda

# # Add these commands to your Dockerfile to warm up Conda
RUN conda config --set always_yes yes && \
    conda update -n base -c defaults conda && \
    conda install -n base conda-libmamba-solver && \
    conda config --set solver libmamba && \
    conda create -n warmup_env python=3.10 -y && \
    conda install -n warmup_env numpy -y && \
    conda remove -n warmup_env --all -y


COPY . /app

WORKDIR /app

# ENV UV_CACHE_DIR=/opt/uv-cache/
