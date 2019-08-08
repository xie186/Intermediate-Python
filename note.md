

## Configure the environment

```
conda create -p /scratch/halstead/x/xie186/Intermediate-Python/env python=3
conda install -c anaconda sphinx
pip install sphinx_rtd_theme
```


## Make the html information

```
cd docs/
make html
python -m http.server 8809
```
