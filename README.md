# Natural Language Processing (NLP) Lab Experiments

This repository contains Python implementations of fundamental **Natural Language Processing (NLP)** concepts and **Exploratory Data Analysis (EDA)** performed as part of laboratory experiments.

The experiments are implemented using **Google Colab** and Python libraries such as **Pandas, NumPy, Matplotlib, Seaborn, NLTK, spaCy, and Regular Expressions (re)**.

---

## Repository Structure

```text
NLP-Lab-Work/
│
├── 2.1_text_data.txt
├── 2.2_tokenization_data.txt
├── 2.3_clean_data.txt
├── 4.1_4.2_input.txt
├── input_sub_word_data.txt
├── corpus_sentencepiece.vocab
│
├── Experiment-1.docx
├── Experiment-3.docx
├── Experiment-4_Term_Frequency_and_NER.docx
│
├── Experiment_1.ipynb
├── Experiment_2.ipynb
├── Experiment_3.ipynb
├── Experiment_4.ipynb
├── Experiment_5.ipynb
│
├── README.md
└── employee_information_100.csv
```

## Data Files Used Across Experiments

Each data file in this repository is used by one or more of the experiments:

| Data File | Used In |
|---|---|
| `employee_information_100.csv` | **Experiment 1** – Employee Data Analysis (EDA on the employee dataset) |
| `2.1_text_data.txt` | **Experiment 2** – Text Preprocessing (2.1: cleaning, lowercasing, punctuation and number removal) |
| `2.2_tokenization_data.txt` | **Experiment 2** – Tokenization (2.2: manual, NLTK, spaCy and regex tokenization) |
| `2.3_clean_data.txt` | **Experiment 2** – Stop Word Removal (2.3: filtering stop words from tokenized text) |
| `4.1_4.2_input.txt` | **Experiment 4** – Term Frequency & NER (4.1 spaCy-based TF/NER, 4.2 manual TF without an NLP toolkit, 4.3 manual TF-IDF) |
| `input_sub_word_data.txt` | **Experiment 5** – Subword Tokenization (5.1 BPE, 5.2 SentencePiece - both training and inference) |
| `corpus_sentencepiece.vocab` | **Experiment 5** – Generated vocabulary file produced while training the SentencePiece tokenizer |

---

# Experiment 1 - Employee Data Analysis

## Objective

Perform **Exploratory Data Analysis (EDA)** on an employee dataset using Python.

## Topics Covered

- Reading CSV files using Pandas
- Data aggregation
- Department-wise analysis
- Salary analysis
- Employee statistics
- Data visualization

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

## Analysis Performed

- Average Salary by Department
- Employee Count by Department
- Gender Distribution
- Salary Distribution
- Experience vs Salary
- Top 10 Highest Paid Employees
- Maximum Salary in Each Department
- Employees Above Average Salary
- Average Experience by Department
- Age Distribution

---

# Experiment 2 - Text Preprocessing & NLP

## Objective

Perform basic **Natural Language Processing (NLP) preprocessing** techniques on text data.

## Topics Covered

- Text Cleaning
- Tokenization
- Stop Word Removal
- Regular Expressions
- Text Normalization

## Libraries Used

- os
- string
- re
- NLTK
- spaCy

## Experiments

### 2.1 Text Preprocessing

- Read text from a file
- Convert uppercase text to lowercase
- Count uppercase letters
- Remove punctuation
- Remove numbers
- Remove extra spaces

### 2.2 Tokenization

Tokenization is implemented using:

- Manual Method
- NLTK
- spaCy
- Regular Expressions

### 2.3 Stop Word Removal

- Load stop words
- Tokenize text
- Remove stop words
- Display filtered text

---

# Experiment 3 - Stemming, Lemmatization & Regular Expressions

## Objective

Understand and implement **stemming, lemmatization, and regular expression-based information extraction** using Python.

## Topics Covered

- Stemming
- Porter Stemmer
- Lemmatization
- WordNet Lemmatizer
- Part-of-Speech based lemmatization
- Regular Expressions
- Pattern Matching
- Information Extraction

## Libraries Used

- NLTK
- re

## Experiments

### 3.1 Stemming Using Porter Stemmer

Apply the **Porter Stemmer** to different forms of words and display their corresponding stems.

Examples:

```text
playing     → play
played      → play
studies     → studi
studying    → studi
connected   → connect
computers   → comput
```

This experiment demonstrates how stemming reduces related words to a common stem using rule-based transformations.

### 3.2 Lemmatization Using WordNet

Perform lemmatization using NLTK's **WordNetLemmatizer**.

Words used include:

- cats
- dogs
- running
- runs
- ran
- studies
- studying
- better
- children
- mice
- went
- ate
- leaves
- caring

This experiment demonstrates how lemmatization converts words into their meaningful base or dictionary forms.

### 3.3 Information Extraction Using Regular Expressions

Use Python Regular Expressions to extract information from text.

Information extracted includes:

- Email Addresses
- URLs
- Mobile Numbers
- Hashtags
- Mentions

Regex patterns are used with functions such as `re.findall()` to identify specific patterns within text.

---

# Experiment 4 - Term Frequency, Named Entity Recognition & TF-IDF

## Objective

Perform **Term Frequency analysis, Named Entity Recognition (NER), and TF-IDF calculation** using both NLP tools and manual Python implementations.

## Topics Covered

- Term Frequency (TF)
- Document Frequency (DF)
- Inverse Document Frequency (IDF)
- TF-IDF
- Named Entity Recognition (NER)
- Text Preprocessing
- Stop Word Removal
- Tokenization
- Frequency Analysis

## Libraries Used

- spaCy
- Pandas
- string
- collections
- math

## Experiments

### 4.1 Term Frequency Analysis and Named Entity Recognition Using spaCy

Perform **Term Frequency Analysis** and **Named Entity Recognition (NER)** using spaCy.

The experiment includes:

- Reading text from a file
- Processing text using spaCy
- Removing stop words
- Removing punctuation
- Converting words to lowercase
- Calculating word frequencies
- Identifying the top 10 most frequent terms
- Saving term frequencies to a CSV file
- Identifying named entities

NER can identify entities such as:

- `PERSON` - Person
- `ORG` - Organization
- `GPE` - Geopolitical Entity
- `LANGUAGE` - Language
- `DATE` - Date
- `CARDINAL` - Numerical value
- `ORDINAL` - Ordinal value

### 4.2 Term Frequency Analysis Without an NLP Toolkit

Perform Term Frequency analysis **without using NLTK, spaCy, or another NLP toolkit**.

The experiment includes:

- Reading text
- Converting text to lowercase
- Removing punctuation
- Tokenizing using basic Python
- Counting terms using `Counter`
- Sorting terms according to frequency
- Displaying the top 10 terms
- Saving the results to CSV

### 4.3 Manual TF-IDF Implementation

Implement **TF-IDF from scratch** without using NLTK, spaCy, or another NLP toolkit.

The program:

1. Reads multiple text documents
2. Converts text to lowercase
3. Removes punctuation
4. Tokenizes each document
5. Calculates **Term Frequency (TF)**
6. Calculates **Document Frequency (DF)**
7. Calculates **Inverse Document Frequency (IDF)**
8. Calculates **TF-IDF**
9. Displays Term, TF, DF, IDF, and TF-IDF values
10. Identifies the top 10 terms with the highest TF-IDF score for each document

### TF-IDF Formulas

```text
TF = Frequency of Term / Total Number of Terms

DF = Number of Documents Containing the Term

IDF = log(Total Number of Documents / Document Frequency)

TF-IDF = TF × IDF
```

TF-IDF assigns greater importance to terms that occur frequently in a particular document but are relatively rare across the entire document collection.

---

# Experiment 5 - Subword Level Tokenization and POS Tagging

## Objective

Implement **subword-level tokenization** using BPE and SentencePiece tokenizers, and **Part-of-Speech (POS) tagging** using both spaCy and NLTK.

## Topics Covered

- Byte Pair Encoding (BPE)
- Subword Tokenization
- Pretrained vs Trained Tokenizers
- HuggingFace `tokenizers` and `transformers`
- SentencePiece
- Part-of-Speech (POS) Tagging
- Token Frequency Analysis

## Libraries Used

- tokenizers
- transformers
- sentencepiece
- spaCy
- NLTK
- collections

## Experiments

### 5.1 Subword-Level Tokenization Using a BPE-based Tokenizer

Tokenize the input text into subword units and display the generated tokens with their corresponding token IDs.

**a. Using a pretrained model** - Load the pretrained `gpt2` BPE tokenizer from HuggingFace `transformers`.
**b. Without a pretrained model** - Build a BPE tokenizer using the `tokenizers` library and train it from scratch on `input_sub_word_data.txt` using `BpeTrainer`.

### 5.2 Subword-Level Tokenization Using a SentencePiece Tokenizer

Tokenize the input text into subword units and display the generated tokens with their corresponding token IDs.

**a. Using a pretrained model** - Load the SentencePiece-based `google/mt5-small` tokenizer.
**b. Without a pretrained model** - Train a SentencePiece BPE model from scratch on `input_sub_word_data.txt` using `spm.SentencePieceTrainer` (generates the `corpus_sentencepiece.vocab` file), then tokenize with the trained model.

### 5.3 POS Tagging on a Given Sentence

Perform Part-of-Speech tagging on:

```text
"The young student is reading an interesting book in the library."
```

and display the unique token, POS tag, and description of each POS tag.

**a. Using spaCy** - `en_core_web_sm` pipeline with `token.pos_` and `spacy.explain()`.
**b. Using NLTK** - `nltk.word_tokenize()` followed by `nltk.pos_tag()`.

### 5.4 POS Tagging with Token Frequency

Perform POS tagging on the full input text using **spaCy** and display the unique token, its POS tag, the description of each token, and its frequency of occurrence in the text.

---

# Technologies Used

- Python 3
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- spaCy
- HuggingFace transformers
- HuggingFace tokenizers
- SentencePiece
- Regular Expressions (re)

---

# Learning Outcomes

After completing these experiments, the following concepts were understood:

- Exploratory Data Analysis
- Data Preprocessing
- Data Visualization
- Text Preprocessing
- Text Normalization
- Tokenization
- Stop Word Removal
- Stemming
- Porter Stemmer
- Lemmatization
- WordNet Lemmatizer
- Regular Expressions
- Pattern-based Information Extraction
- Term Frequency (TF)
- Document Frequency (DF)
- Inverse Document Frequency (IDF)
- TF-IDF
- Named Entity Recognition (NER)
- Byte Pair Encoding (BPE)
- Subword-level Tokenization
- Pretrained vs Trained Tokenizers
- SentencePiece
- Part-of-Speech (POS) Tagging
- NLP Preprocessing Pipelines
- Toolkit-based and Manual NLP Implementations
- Python Libraries for NLP and Data Analysis

---

# Author

**Sarthak Jakhmola**

B.Tech CSE (AI & ML)  
UPES, Dehradun
