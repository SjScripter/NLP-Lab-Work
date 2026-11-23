# Natural Language Processing (NLP) Lab Experiments

This repository contains Python implementations of fundamental **Natural Language Processing (NLP)** concepts, **Deep Learning**, and **Exploratory Data Analysis (EDA)** performed as part of laboratory experiments.

The experiments are implemented using **Jupyter Notebooks / Google Colab** with industry-standard libraries including **Pandas, NumPy, Matplotlib, Seaborn, NLTK, spaCy, PyTorch, Scikit-Learn, HuggingFace Transformers, HuggingFace Tokenizers, and SentencePiece**.

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
├── glove_corpus.txt
├── IMDB_sample_2k.csv
├── employee_information_100.csv
│
├── Experiment-1.docx
├── Experiment-3.docx
├── Experiment-4_ Term Frequency and NER.docx
├── Experiment-5.docx
├── Experiment-6.docx
├── Experiment-7.docx
├── Experiment-8.docx
│
├── Experiment_1.ipynb
├── Experiment_2.ipynb
├── Experiment_3.ipynb
├── Experiment_4.ipynb
├── Experiment_5.ipynb
├── Experiment_6.ipynb
├── Experiment_7.ipynb
├── Experiment_8.ipynb
│
└── README.md
```

## Data Files Used Across Experiments

| Data File | Used In | Description |
|---|---|---|
| `employee_information_100.csv` | **Experiment 1** | Employee Data Analysis (EDA on 100 employee records) |
| `2.1_text_data.txt` | **Experiment 2** | Text Preprocessing (2.1: cleaning, lowercase conversion, punctuation and digit removal) |
| `2.2_tokenization_data.txt` | **Experiment 2** | Tokenization (2.2: manual, NLTK, spaCy, and regex tokenization) |
| `2.3_clean_data.txt` | **Experiment 2** | Stop Word Removal (2.3: filtering stopwords from text) |
| `4.1_4.2_input.txt` | **Experiment 4** | Term Frequency & NER (4.1 spaCy-based TF/NER, 4.2 manual TF without toolkits, 4.3 TF-IDF) |
| `input_sub_word_data.txt` | **Experiment 5** | Subword Tokenization (5.1 BPE, 5.2 SentencePiece, 5.4 POS with frequencies) |
| `corpus_sentencepiece.vocab` | **Experiment 5** | Vocabulary produced while training SentencePiece tokenizer |
| `glove_corpus.txt` | **Experiment 6** | GloVe Word Embeddings (custom domain corpus for co-occurrence counting) |
| `IMDB_sample_2k.csv` | **Experiment 7** | IMDB Movie Reviews (sentiment classification using classical and neural models) |

---

# Experiment 1 - Employee Data Analysis

## Objective
Perform **Exploratory Data Analysis (EDA)** on an employee dataset using Python.

## Topics Covered
- Reading CSV files using Pandas
- Data aggregation and department-wise analysis
- Salary statistics and distribution histograms
- Experience vs. Salary scatter plots
- Top 10 highest-paid employees
- Gender and age distributions with pie charts and histograms

---

# Experiment 2 - Text Preprocessing & NLP

## Objective
Perform basic **Natural Language Processing (NLP) preprocessing** techniques on text data.

## Topics Covered
- Text Cleaning (casing, punctuation, digits, whitespace)
- Tokenization (Manual, NLTK, spaCy, and Regex)
- Stop Word Removal and vocabulary normalization

---

# Experiment 3 - Stemming, Lemmatization & Regular Expressions

## Objective
Understand and implement **stemming, lemmatization, and regular expression-based information extraction** using Python.

## Topics Covered
- Stemming using the Porter Stemmer (`nltk.stem.PorterStemmer`)
- Lemmatization using WordNet (`nltk.stem.WordNetLemmatizer`)
- Regular Expressions (`re`) to extract Emails, URLs, Phone numbers, Hashtags, and Mentions

---

# Experiment 4 - Term Frequency & Named Entity Recognition (NER)

## Objective
Implement Term Frequency analysis with and without NLP toolkits, and perform Named Entity Recognition.

## Topics Covered
- SpaCy NER (`PERSON`, `ORG`, `GPE`, `DATE`, etc.) and frequency computation
- Term Frequency analysis from scratch without NLP libraries
- Full TF-IDF implementation from scratch across multiple documents

---

# Experiment 5 - Subword Level Tokenization and POS Tagging

## Objective
Implement **subword-level tokenization** using BPE and SentencePiece tokenizers, and **Part-of-Speech (POS) tagging** using both spaCy and NLTK.

## Topics Covered
- **5.1 BPE Tokenization**: Pretrained (`gpt2`) and Trained from Scratch (`tokenizers.BpeTrainer`).
- **5.2 SentencePiece Tokenization**: Pretrained (`google/mt5-small`) and Trained from Scratch (`sentencepiece.SentencePieceTrainer`).
- **5.3 POS Tagging**: SpaCy (`en_core_web_sm`) and NLTK (`nltk.pos_tag`).
- **5.4 POS Frequency Analysis**: Unique tokens, grammatical tag explanations, and corpus occurrence frequencies.

---

# Experiment 6 - GloVe Word Embeddings & Statistical Language Modeling

## Objective
Implement vector word representations and probabilistic next-word prediction:
1. **GloVe (Global Vectors for Word Representation)**:
   - **6.1(a) GloVe From Scratch**: Build a symmetric co-occurrence matrix with harmonic distance weighting ($1/d$), optimize word and context vectors with AdaGrad against the log-bilinear least squares objective, and find words most similar to `"king"`.
   - **6.1(b) Pretrained GloVe (Gensim)**: Load pretrained vectors (`glove-wiki-gigaword-50`), evaluate nearest neighbors for `"king"`, and demonstrate vector analogies ($\text{king} - \text{man} + \text{woman} \approx \text{queen}$).
2. **Statistical Language Model (N-Gram Approach)**:
   - Build Unigram, Bigram, and Trigram language models from scratch with sentence boundary markers (`<s>`, `</s>`).
   - Implement Laplace (add-1 / add-$\alpha$) smoothing.
   - Predict subsequent words given conversational contexts (e.g. `"machine learning"` $\to$ `"is"`, `"and"`).

---

# Experiment 7 - Sentiment Analysis Using Deep Learning and Transformers

## Objective
Implement binary sentiment classification on the **IMDB Movie Reviews Dataset** comparing four architectures:
1. **Logistic Regression (TF-IDF Baseline)**: N-gram TF-IDF features with L2 regularization.
2. **Bidirectional LSTM Classifier**: PyTorch recurrent neural network capturing sequential token dependencies.
3. **Vanilla Transformer Encoder**: PyTorch multi-head self-attention with sinusoidal positional encoding.
4. **Pretrained BERT (`bert-base-uncased`)**: Fine-tuned bidirectional transformer representations.

## Evaluation
- Metrics: **Accuracy, Precision, Recall, and F1-Score**.
- **Confusion Matrices** for each model comparing true vs. predicted sentiment.
- Inference testing on custom unseen movie reviews.

---

# Experiment 8 - Abstractive Text Summarization Using Multilingual Transformers

## Objective
Implement and benchmark abstractive text summarization using sequence-to-sequence multilingual models on the **Hindi XL-Sum (Cross-Lingual Summarization) dataset**:
1. **mT5 (Multilingual Text-to-Text Transfer Transformer)** (`google/mt5-small`): 101-language span corruption pretrained encoder-decoder.
2. **mBART (Multilingual Bidirectional Auto-Regressive Transformers)** (`facebook/mbart-large-50-many-to-many-mmt`): Sequence-level denoising autoencoder with Hindi language tag prefixes (`hi_IN`).

## Evaluation Metrics
- **Lexical Overlap Metrics**: ROUGE-1, ROUGE-2, and ROUGE-L.
- **Contextual Semantic Metric**: Multilingual BERTScore (mBERTScore: Precision, Recall, and F1).
- Qualitative comparison of generated summaries versus ground-truth references.

---

# Technologies Used

- Python 3.10+
- Jupyter Notebook / Google Colab
- Pandas, NumPy, Scipy
- Matplotlib, Seaborn
- NLTK & spaCy
- PyTorch
- Scikit-Learn
- HuggingFace Transformers & Datasets
- HuggingFace Tokenizers & SentencePiece
- Gensim

---

# Author

**Sarthak Jakhmola**  
B.Tech CSE (AI & ML)  
UPES, Dehradun
