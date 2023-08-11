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

You can refer to the demo files or the `Google Collab Notebook <https://colab.research.google.com/drive/11O3ApBUHgWhBe-Pv20KZaw-3o-1lm30h#scrollTo=j-MmU6Et9kZo>`_ for more information.

This site is still in the works. More detailed documentation to be added soon!!

.. _data acquisition module:

Data Acquisition Module
-----------------------
 
This module enables effortless loading and downloading of datasets in various formats from external and local resources. Additionally, it offers a curated collection of 15 datasets tailored for different NLP tasks specific to Hindi-English code-mixed text. Supported file formats of datasets:- pickle json txt csv conll

Datasets available in cmkt datahub for following tasks. Use the specifed names of tasks to search for datasets in cmkt datahub

["lid", "ner", "pos", "machine translation", "sentiment analysis", "hate speech detection", "irony detection", "humor detection", "sarcasm detection"]

You can use the ``cmkt.data.load_url()`` function:

.. autofunction:: cmkt.data.load_url()

You can use the ``cmkt.data.downloader.download_cmkt_datasets()`` function:

.. autofunction:: cmkt.data.downloader.download_cmkt_datasets()


.. _text preprocessing module:
Text Preprocessing Module
--------------------------

Text Preprocessing Module offers a range of functionalities for efficiently preprocessing code-mixed text. This module provides different types of tokenization and stemming specifically designed for code-mixed text. By utilizing the cmkt Text Preprocessing Module, you can efficiently preprocess your code-mixed text data for various downstream tasks such as NLP analysis and model training. In the subsequent sections, we provide detailed instructions and code examples to guide you through using these text preprocessing functionalities in cmkt.

Tokenization
~~~~~~~~~~~~

Tokenization in cmkt: Breaking Text into Meaningful Units

The text preprocessing module includes tokenization techniques at the sentence, word, and subword levels, along with stemming methods for English, Hindi, and Hindi-English mixed script text. Following tokenizers are available in cmtt:-

* Word Tokenizer 
* Sentence Tokenizer 
* SentencePiece Tokeizer 
  
The tokenizers are currently available for english, hindi and english-hindi mixed script text.

Stemming
~~~~~~~~

Stemming in CMKT: Reducing Words to their Base Form

Stemming is an essential part of code-mixed text processing, enabling the reduction of words to their base or root form. In the CMKT , we provide a range of stemmers specifically designed for different languages and language combinations. This chapter outlines the stemmers available in CMKT for English, Hindi, and English-Hindi mixed script text.

Following tokenizers are available in cmtt:-

* English Stemmer
* Hindi Stemmer
* Hindi-English mixed Stemmer
 
.. _tasks module: 
Tasks Module 
------------- 
  
This module provides elementary NLP tasks such as NER, POS, LID etc for code-mixed text. This module also provides functions to search for tasks and models available in cmkt. The Hierarchy of task module is defined below.

Task types available in cmkt: "syntactic", "semantic", and "generational"

TaskToolkit (Language specific)

* Syntactic tasks

  * lid
  * ner
  * pos

* Semantic tasks

  * sentiment analysis
  * hate speech detection
  * humor detection

* Generational tasks

  * machine translation

