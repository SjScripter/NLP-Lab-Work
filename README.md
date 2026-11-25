# Natural Language Processing (NLP) Lab Experiments

This repository contains complete Python implementations of fundamental **Natural Language Processing (NLP)** concepts, **Deep Learning**, and **Multilingual Language Modeling** performed as part of laboratory experiments and course mini-projects (Experiments 1 through 10).

The experiments are implemented using **Jupyter Notebooks / Google Colab** with industry-standard libraries including **Pandas, NumPy, Matplotlib, Seaborn, NLTK, spaCy, PyTorch, Scikit-Learn, HuggingFace Transformers, HuggingFace Tokenizers, SentencePiece, and Gensim**.

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
├── Experiment-9.docx
├── Experiment-10.docx
│
├── Experiment_1.ipynb
├── Experiment_2.ipynb
├── Experiment_3.ipynb
├── Experiment_4.ipynb
├── Experiment_5.ipynb
├── Experiment_6.ipynb
├── Experiment_7.ipynb
├── Experiment_8.ipynb
├── Experiment_9.ipynb
├── Experiment_10.ipynb
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
- Exploratory Data Analysis (EDA) on structured enterprise records using Pandas and Matplotlib.
- Departmental salary averages, gender balance pie charts, salary distribution histograms, experience vs. salary scatter plots, and workforce age distributions.

---

# Experiment 2 - Text Preprocessing & NLP
- Text sanitation (casing normalization, punctuation/digit removal).
- Comparative word and sentence tokenization across NLTK, spaCy, and regular expressions.
- Stopword elimination and vocabulary reduction metrics.

---

# Experiment 3 - Stemming, Lemmatization & Regular Expressions
- Heuristic suffix stripping with the Porter Stemmer (`nltk.stem.PorterStemmer`).
- Morphological dictionary reduction with WordNet Lemmatizer (`nltk.stem.WordNetLemmatizer`).
- Regular expression parsing (`re`) for emails, URLs, telephone numbers, hashtags, and social handles.

---

# Experiment 4 - Term Frequency & Named Entity Recognition (NER)
- Entity extraction using spaCy pipeline (`PERSON`, `ORG`, `GPE`, `DATE`, etc.).
- Term frequency computation from scratch without NLP toolkits.
- Multi-document TF-IDF mathematical derivation and matrix generation from first principles.

---

# Experiment 5 - Subword Level Tokenization and POS Tagging
- **BPE Tokenization**: Pretrained (`gpt2`) and Custom-trained (`tokenizers.BpeTrainer`).
- **SentencePiece Tokenization**: Pretrained (`google/mt5-small`) and Custom-trained (`sentencepiece.SentencePieceTrainer`).
- **POS Tagging**: Comparative grammatical tagging using spaCy and NLTK.
- **Corpus Frequency Profiling**: Token occurrences mapped with detailed linguistic explanations.

---

# Experiment 6 - GloVe Word Embeddings & Statistical Language Modeling
- **GloVe from Scratch**: Co-occurrence matrix with harmonic distance weighting ($1/d$), AdaGrad optimization, and nearest neighbor extraction for `"king"`.
- **Pretrained GloVe (Gensim)**: Vector similarity queries and semantic analogies ($\text{king} - \text{man} + \text{woman} \approx \text{queen}$).
- **Statistical N-Gram Language Modeling**: Unigram, Bigram, and Trigram language model with Laplace smoothing for next-word probability estimation.

---

# Experiment 7 - Sentiment Analysis Using Deep Learning and Transformers
- Binary sentiment classification on the IMDB Movie Reviews dataset comparing:
  1. Logistic Regression (TF-IDF Baseline)
  2. Bidirectional LSTM (PyTorch)
  3. Vanilla Transformer Encoder (PyTorch)
  4. Pretrained BERT (`bert-base-uncased`)
- Evaluation using Accuracy, Precision, Recall, F1-Score, and $2 \times 2$ Confusion Matrices.

---

# Experiment 8 - Abstractive Text Summarization Using Multilingual Transformers
- Multilingual sequence-to-sequence summarization on the **Hindi XL-Sum dataset** comparing:
  1. `google/mt5-small` (Span corruption encoder-decoder)
  2. `facebook/mbart-large-50-many-to-many-mmt` (Denoising autoencoder with `hi_IN` prefixes)
- Evaluation via surface n-gram overlap (**ROUGE-1, ROUGE-2, ROUGE-L**) and contextual vector alignment (**mBERTScore**).

---

# Experiment 9 - Multiclass News Article Classification
- Thematic document classification across four classes (*World, Sports, Business, Sci/Tech*) on the **AG News** dataset comparing:
  1. Classical ML (TF-IDF + LinearSVC) — 91.28% Accuracy, 0.12 ms/sample latency
  2. Deep Learning (Bi-LSTM with Word Embeddings) — 88.45% Accuracy
  3. Pretrained Transformer (Fine-Tuned DistilBERT) — 93.85% Accuracy, 93.84% F1
- Evaluation via Normalized Confusion Matrices, Accuracy vs. Latency trade-offs, and live headline inference.

---

# Experiment 10 - Low-Resource Neural Machine Translation (NMT)
- Bidirectional neural machine translation for low-resource Indic languages using transfer learning on the **WMT 2026 Shared Task on Low-Resource Indic Language Translation**:
  1. Zero-shot Multilingual Baseline (`facebook/nllb-200-distilled-600M`)
  2. Domain Fine-Tuned Bidirectional NMT Model (English $\leftrightarrow$ Indic)
  3. Recurrent Seq2Seq with Attention and Custom Transformer comparisons
- Quantitative benchmark using **SacreBLEU**, **chrF++**, and **Translation Edit Rate (TER)** in both translation directions (En $\to$ X and X $\to$ En).

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
- NLLB-200, DistilBERT, BERT, mT5, mBART
- Gensim

---

# Author

**Sarthak Jakhmola**  
SAP ID: 500122482 | Roll No: R2142231632  
B.Tech CSE (AI & ML), Semester VII  
School of Computer Science, UPES, Dehradun
