# Parts of Speech Counter

A Python text-analysis tool for counting broad part-of-speech categories across `.txt` files.

## Overview

This project was originally created as a utility for the MapLemon Corpus. It uses NLTK to tokenize and tag text files, then counts selected part-of-speech categories, including nouns, verbs, adjectives, adverbs, pronouns, prepositions, and proper nouns.

## Features

- Reads all `.txt` files in a selected folder
- Tokenizes text with NLTK
- Tags each token with a part-of-speech label
- Counts broad POS categories
- Exports results to a text file

## POS Categories Counted

- Adjectives
- Nouns
- Prepositions
- Proper nouns
- Personal pronouns
- Possessive pronouns
- Adverbs
- Verbs

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Download required NLTK data:
```python
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
```

## How to Run
```bash
python pos_counter.py
```
You will be prompted to enter:
1. The folder path containing your `.txt` files
2. The name of the output file

## Skills Demonstrated
* Python scripting
* Natural language processing
* Corpus analysis
* Part-of-speech tagging
* File and directory handling
* Frequency counting

## Future Improvements
* Add command-line arguments
* Export results as CSV
* Add normalized POS counters per 1,000 words
* Visualize POS distribution
* Compare POS patterns across corpora
