Usage
=====

.. _installation:

Installation
------------

To use CMKT, first install it into your laptop/pc through the following commands:

::
  git clone https://github.com/lingo-iitgn/CMKT.git
  
::
  cd CMKT

::
  pip install -r "requirements.txt"

.. _data acquisition module:

Data Acquisition Module
-----------------------

This module enables effortless loading and downloading of datasets in various formats from external and local resources. Additionally, it offers a curated collection of 15 datasets tailored for different NLP tasks specific to Hindi-English code-mixed text. Supported file formats of datasets:- pickle json txt csv conll

Datasets available in cmkt datahub for following tasks. Use the specifed names of tasks to search for datasets in cmkt datahub

["lid", "ner", "pos", "machine translation", "sentiment analysis", "hate speech detection", "irony detection", "humor detection", "sarcasm detection"]