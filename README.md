# Natural Language Processing (NLP) Lab Experiments

This repository contains Python implementations of fundamental **Natural Language Processing (NLP)** concepts and **Exploratory Data Analysis (EDA)** performed as part of laboratory experiments.

The experiments are implemented using **Google Colab** and Python libraries such as **Pandas, NumPy, Matplotlib, Seaborn, NLTK, spaCy, and Regular Expressions (re)**.

---

## Repository Structure

```text
NLP-Lab/
│
├── 2.1_text_data.txt
├── 2.2_tokenization_data.txt
├── 2.3_clean_data.txt
├── 4.1_4.2_input.txt
│
├── Experiment-1.docx
├── Experiment-3.docx
├── Experiment-4_Term_Frequency_and_NER.docx
│
├── Experiment_1.ipynb
├── Experiment_2.ipynb
├── Experiment_3.ipynb
├── Experiment_4.ipynb
│
├── README.md
└── employee_information_100.csv
```

> **Note:** The Experiment 4 DOCX filename is shortened in the GitHub screenshot. Replace `Experiment-4_Term_Frequency_and_NER.docx` above with the exact filename if it differs.

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

# Technologies Used

- Python 3
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- spaCy
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
- NLP Preprocessing Pipelines
- Toolkit-based and Manual NLP Implementations
- Python Libraries for NLP and Data Analysis

---

# Author

**Sarthak Jakhmola**

B.Tech CSE (AI & ML)  
UPES, Dehradun
