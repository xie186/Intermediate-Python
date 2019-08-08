Intermediate Python for Scientific Computing and Data Analysis
==============================================================

This workshop covers topics that are essential for scientific computing and 
data analysis in Python, but typically *not* covered in an introductory course 
or workshop. These are the thing you *need* to know if you are writing software
that meets any of the following criteria:

* You expect to be working on it for more than a couple of weeks.
* You expect that it will be composed of more than a hundred or so lines of code.
* You want it to produce results that can be trusted - for example, if you are 
  publishing a research paper based on those results.
* You expect that it will be used by other people.
* You are contributing to another project - e.g., an open-source software package.


Topics Covered
--------------

1. How to create an installable *package* instead of a loose collection of files.
2. How to create *unit tests* that ensure correctness, even as you make changes.
3. How to document your code so it's easy for you and others to use.
4. How to improve the usability of your code.
5. How to improve the performance of your code.


Prerequisites
-------------

This workshop assumes you know the very basics of programming with Python. If you can 
write a loop and a function in Python, and if you know how to run a ``.py`` script, 
you should be able to follow this tutorial easily.

If you plan to participate in the hands-on exercises, you will need:

* A laptop with `Anaconda <https://www.anaconda.com/download/>`_ installed.
* One or more friends. It is **highly** encouraged to work in groups,
  so if you haven't already, please introduce yourself to your neighbors.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   packaging
   testing
   documenting
   usability
   performance