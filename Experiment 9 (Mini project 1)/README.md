# ⚡ 30-Second News Reel Brief Generator (NLP Project - Exp 9)

An NLP-powered system designed for social media creators and influencers to transform complex, multi-paragraph news articles into punchy, high-engagement 30-second video scripts (75–85 words) with on-screen text, trending hashtags, fact-safety scoring, and ROUGE evaluation.

---

## 🌟 Key Features

1. **Multi-Channel News Ingestion**:
   - **Live RSS Feeds**: Real-time headline fetching from *The Hindu, NDTV, Times of India, and BBC World News*.
   - **URL Article Extractor**: Extracts boilerplate-free clean article text using `trafilatura` and `newspaper3k`.
   - **Direct Text Input**: Paste any custom news text or topic.

2. **Core NLP Preprocessing**:
   - Clean sentence tokenization.
   - Named Entity Recognition (NER) preserving organizations, locations, people, dates, and metrics.
   - Stopword removal & frequency-based keyword extraction.
   - Automatic Topic Classifier (*Space & Science, Tech & AI, Politics & Policy, Business & Economy, Sports, Entertainment*).

3. **Hybrid Summarization & Reel Styling**:
   - **Extractive Summarization**: Graph-based **TextRank** (PageRank over cosine sentence similarity matrix) selecting key fact anchors.
   - **Reel Script Formulation**:
     - **Hook (0–3s)**: High-curiosity opening that prevents scrolling.
     - **Body (3–24s)**: 2–3 crisp, bite-sized factual sentences.
     - **Closer / CTA (24–30s)**: High-converting call to action.
   - **Multi-Tone Support**: *Informative, Dramatic, Casual, and Hinglish*.
   - **Speaking Duration Meter**: Calibrated to 2.5–2.8 words/second (~75–85 words total).

4. **Influencer Production Package**:
   - **On-Screen Text Flash Cards**: Overlay cards for the video editor.
   - **Hashtag Generator**: Auto-tags based on topics and extracted entities.
   - **Social Media Caption**: Ready-to-post Instagram / YouTube Shorts / TikTok caption.
   - **One-Click Copy** teleprompter view.

5. **Academic & NLP Evaluation Suite**:
   - **ROUGE Metrics**: Computes ROUGE-1, ROUGE-2, and ROUGE-L comparing source facts to the generated script.
   - **Fact Safety Guard**: Cross-verifies entity and numeric preservation to minimize AI hallucination.

---

## 🚀 How to Run the Application

1. **Activate Environment & Run Streamlit UI**:
   ```bash
   streamlit run app.py
   ```
2. Open your browser at the displayed local URL (typically `http://localhost:8501`).

3. **Test the Pipeline**:
   ```bash
   python test_pipeline.py
   ```

---

## 📁 Project Structure

```
experiment 9/
│
├── app.py              # Streamlit interactive UI & teleprompter
├── nlp_pipeline.py     # NLP logic (TextRank, Extraction, NER, ROUGE, Reel Generator)
├── test_pipeline.py    # Unit & pipeline verification tests
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation & report overview
```
