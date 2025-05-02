# Set up

Create benchmarking docker

```bash
docker build . -t uvpreso
docker run --rm -ti --entrypoint /bin/bash  uvpreso                                                                                                                                                                                                           INT ✘ 
```


# Benchmarking

Install matplotlib, pandas, seaborn, scikit-learn, torch using the timing and benchmarkign scripts

```
python time_it ./uv.sh venv
python time_it ./uv.sh venv_cache

```

Repeat for conda and venv respectively


| system    | no cache | cache  |
| -------- | --------- |------- |
| venv+pip | 90.34s    | 23.54s |
| conda    | 41.54s    | 5.88s  |
| uv       | 55.59s    | 0.26s  |


What's happening
Both venv and uv will pull their packages from pypi.org and conda from conda-forge. Download speeds of the respective servers on that day will affect performance