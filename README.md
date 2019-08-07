Intermediate Python
===================

A workshop on building better scientific software with Python.


Components
----------

You can view the workshop materials as a website. First clone the repository locally:

```
git clone https://github.rcac.purdue.edu/glentner/Intermediate-Python
```

Build if necessary.

```
python -m pip install --user sphinx sphinx_rtd_theme
cd Intermediate-Python/docs && make html
```

Host locally.

```
python -m http.server --directory _build/html
```
