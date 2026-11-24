import streamlit as st
from nlp_pipeline import (
    RSS_FEEDS, fetch_rss_articles, extract_article_text, preprocess_text,
    extractive_textrank, detect_topic, generate_reel_script,
    generate_social_assets, evaluate_summaries, verify_facts
)

# Page Configuration
st.set_page_config(
    page_title="News Reel Script Synthesizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Minimalist, Clean White Professional Styling (No Emojis)
st.markdown("""
<style>
    /* Global Font & Canvas */
    html, body, [class*="css"], .stApp {
        background-color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        color: #111827 !important;
    }

    section[data-testid="stSidebar"], div[data-testid="stSidebar"], div[data-testid="stSidebarContent"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0 !important;
        color: #1e293b !important;
    }
    
    .header-title {
        font-size: 1.65rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #0f172a;
        margin-bottom: 4px;
    }
    .header-subtitle {
        font-size: 0.92rem;
        color: #64748b;
        margin-bottom: 24px;
        line-height: 1.5;
    }
    
    /* Teleprompter Card */
    .script-container {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 24px;
        margin-top: 14px;
        margin-bottom: 20px;
    }
    .script-segment {
        margin-bottom: 16px;
        padding-bottom: 12px;
        border-bottom: 1px solid #edf2f7;
    }
    .script-segment:last-child {
        margin-bottom: 0px;
        padding-bottom: 0px;
        border-bottom: none;
    }
    .segment-label {
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 2px 7px;
        border-radius: 3px;
        margin-bottom: 6px;
    }
    .label-hook {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    .label-body {
        background-color: #e0f2fe;
        color: #0369a1;
    }
    .label-cta {
        background-color: #dcfce7;
        color: #15803d;
    }
    .segment-text {
        font-size: 1.05rem;
        line-height: 1.65;
        color: #1e293b;
    }
    
    /* Metrics display */
    div[data-testid="stMetric"] {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 12px 14px;
    }
    div[data-testid="stMetric"] label {
        color: #64748b !important;
        font-size: 0.78rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-weight: 600;
        font-size: 1.35rem !important;
    }

    /* Clean Borders for Form Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        color: #0f172a !important;
        border-radius: 4px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 1px #2563eb !important;
    }
    
    /* Button Styling */
    .stButton button {
        background-color: #f1f5f9;
        color: #0f172a;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        font-weight: 500;
        font-size: 0.88rem;
    }
    .stButton button:hover {
        background-color: #e2e8f0;
        border-color: #94a3b8;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        color: #64748b;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        color: #0f172a !important;
        border-bottom: 2px solid #2563eb !important;
    }

    /* Sidebar Content */
    section[data-testid="stSidebar"] h3 {
        color: #0f172a !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] label {
        color: #475569 !important;
    }
</style>
""", unsafe_allow_html=True)

# Minimal Header
st.markdown('<div class="header-title">News Reel Script Synthesizer</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">NLP-based summarization and concise speech synthesis for short-form journalism (30-Second Duration).</div>', unsafe_allow_html=True)

# Sidebar Parameters
with st.sidebar:
    st.markdown("### Configuration")
    
    tone = st.selectbox(
        "Narrative Tone",
        ["Informative", "Dramatic", "Casual", "Hinglish"],
        index=0,
        help="Adjusts hook structure and phrasing."
    )
    
    target_words = st.slider(
        "Speech Target (Words)",
        min_value=60,
        max_value=100,
        value=80,
        step=5,
        help="Calibrated to 2.6 words/sec speech cadence."
    )
    
    num_extractive_sents = st.slider(
        "Source Sentences Extracted",
        min_value=2,
        max_value=5,
        value=3,
        help="Number of core statements selected by TextRank graph ranking."
    )

    st.markdown("---")
    st.markdown("### System Pipeline")
    st.caption("1. Content Ingestion (RSS / URL / Raw Text)\n"
               "2. Trafilatura DOM Cleaning\n"
               "3. TextRank Graph Extraction\n"
               "4. Speech Synthesis & Duration Fitting\n"
               "5. ROUGE-1/2/L Evaluation & Fact Verification")

# Ingestion Tabs
tab_rss, tab_url, tab_manual = st.tabs(["RSS Live Feeds", "URL Parser", "Direct Text Input"])

with tab_rss:
    st.markdown("##### Select Article from Live RSS Feed")
    c1, c2 = st.columns([3, 1])
    with c1:
        selected_feed = st.selectbox("Publication Feed", list(RSS_FEEDS.keys()), label_visibility="collapsed")
    with c2:
        refresh_feed = st.button("Refresh Headlines", use_container_width=True)

    feed_url = RSS_FEEDS[selected_feed]
    articles = fetch_rss_articles(feed_url, limit=5)
    
    if articles:
        for idx, art in enumerate(articles):
            col_meta, col_act = st.columns([5, 1])
            with col_meta:
                st.markdown(f"**{art['title']}**")
                st.caption(f"{art['published']} | [Source Document]({art['link']})")
            with col_act:
                if st.button("Synthesize", key=f"btn_rss_{idx}"):
                    st.session_state["active_title"] = art['title']
                    with st.spinner("Extracting document body..."):
                        extracted = extract_article_text(art['link'])
                        st.session_state["active_text"] = extracted if extracted else art['summary']
    else:
        st.info("No articles returned from selected feed.")

with tab_url:
    st.markdown("##### Parse Article by URL")
    url_input = st.text_input("Source URL", placeholder="https://www.thehindu.com/...", label_visibility="collapsed")
    if st.button("Fetch and Extract"):
        if url_input.strip():
            with st.spinner("Extracting text via Trafilatura..."):
                extracted = extract_article_text(url_input.strip())
                if extracted:
                    st.session_state["active_title"] = "URL Ingested Article"
                    st.session_state["active_text"] = extracted
                    st.success(f"Article parsed ({len(extracted.split())} words).")
                else:
                    st.error("Extraction failed. Please paste the article body in the Direct Text tab.")
        else:
            st.warning("Please specify a URL.")

with tab_manual:
    st.markdown("##### Direct Text Input")
    custom_title = st.text_input("Article Headline", placeholder="Headline or topic...")
    custom_text = st.text_area("Article Body", height=180, placeholder="Paste article text here...")
    if st.button("Process Text"):
        if custom_text.strip():
            st.session_state["active_title"] = custom_title if custom_title else "Manual Submission"
            st.session_state["active_text"] = custom_text.strip()
            st.success("Input verified.")
        else:
            st.warning("Input buffer is empty.")

# Main Processing & Display Section
active_title = st.session_state.get("active_title", "")
active_text = st.session_state.get("active_text", "")

if active_text:
    st.markdown("---")
    st.markdown(f"#### Active Subject: *{active_title}*")
    
    with st.expander("Source Article Raw Text"):
        st.text(active_text[:2500] + ("\n[Truncated...]" if len(active_text) > 2500 else ""))

    # Processing Pipeline
    prep = preprocess_text(active_text)
    detected_topic = detect_topic(active_text)
    extractive_sents = extractive_textrank(prep["sentences"], num_sentences=num_extractive_sents)
    extractive_summary = " ".join(extractive_sents)
    
    reel_res = generate_reel_script(
        extractive_sents,
        topic=detected_topic,
        tone=tone,
        target_words=target_words,
        keywords=prep["keywords"]
    )
    
    social = generate_social_assets(
        title=active_title,
        topic=detected_topic,
        keywords=prep["keywords"],
        tone=tone
    )
    
    facts = verify_facts(prep["entities"], reel_res["full_script"])
    eval_scores = evaluate_summaries(active_text, extractive_summary, reel_res["full_script"])

    # High-level Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Estimated Duration", f"{reel_res['est_duration_sec']} s", f"{reel_res['word_count']} words")
    with m2:
        st.metric("Topic Category", detected_topic)
    with m3:
        st.metric("Fact Safety Index", f"{facts['safety_score']} %")
    with m4:
        st.metric("ROUGE-1 F-Score", f"{eval_scores['rouge1']['fmeasure']}")

    # Structured Teleprompter View
    st.markdown("#### Synthesized Teleprompter Script")
    st.markdown(f"""
    <div class="script-container">
        <div class="script-segment">
            <span class="segment-label label-hook">Hook (0 - 3s)</span>
            <div class="segment-text">{reel_res['hook']}</div>
        </div>
        <div class="script-segment">
            <span class="segment-label label-body">Key Facts (3 - 24s)</span>
            <div class="segment-text">{reel_res['body']}</div>
        </div>
        <div class="script-segment">
            <span class="segment-label label-cta">Call to Action (24 - 30s)</span>
            <div class="segment-text">{reel_res['closer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.text_area("Full Script Text", value=reel_res["full_script"], height=80, help="Plaintext format for teleprompter export or clipboard copying.")

    # Production Assets Row
    st.markdown("#### Production Assets")
    col_cards, col_cap = st.columns(2)
    
    with col_cards:
        st.markdown("**On-Screen Text Overlays**")
        for card in social["screen_cards"]:
            st.text(f"• {card}")
            
        st.markdown("**Hashtags**")
        st.code(" ".join(social["hashtags"]), language="text")

    with col_cap:
        st.markdown("**Social Caption**")
        st.text_area("Caption Text", value=social["caption"], height=160, label_visibility="collapsed")

    # NLP Analysis and Evaluation
    st.markdown("---")
    st.markdown("#### Natural Language Processing Evaluation")
    
    t_rouge, t_extract, t_entities = st.tabs(["ROUGE Metrics", "TextRank Extraction", "Entity Verification"])
    
    with t_rouge:
        st.markdown("Overlap evaluation between source key sentences and synthesized speech script:")
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown("**ROUGE-1 (Unigram)**")
            st.write(f"Precision: {eval_scores['rouge1']['precision']}")
            st.write(f"Recall: {eval_scores['rouge1']['recall']}")
            st.write(f"F1 Score: {eval_scores['rouge1']['fmeasure']}")
        with r2:
            st.markdown("**ROUGE-2 (Bigram)**")
            st.write(f"Precision: {eval_scores['rouge2']['precision']}")
            st.write(f"Recall: {eval_scores['rouge2']['recall']}")
            st.write(f"F1 Score: {eval_scores['rouge2']['fmeasure']}")
        with r3:
            st.markdown("**ROUGE-L (LCS)**")
            st.write(f"Precision: {eval_scores['rougeL']['precision']}")
            st.write(f"Recall: {eval_scores['rougeL']['recall']}")
            st.write(f"F1 Score: {eval_scores['rougeL']['fmeasure']}")

    with t_extract:
        st.markdown("Sentences identified by PageRank graph centrality:")
        for idx, sentence in enumerate(extractive_sents, 1):
            st.markdown(f"**[{idx}]** {sentence}")

    with t_entities:
        st.markdown("**Entity Preservation Audit**")
        if facts["preserved_entities"]:
            st.write("Preserved Entities: " + ", ".join(facts["preserved_entities"]))
        if facts["numbers_found"]:
            st.write(f"Numerical Figures Preserved: {', '.join(facts['numbers_found'])}")
        st.caption(f"Preservation Score: {facts['safety_score']}% (Cross-checks names, organizations, and quantities against hallucinations).")

else:
    st.markdown("<div style='color: #64748b; font-size: 0.95rem; margin-top: 10px;'>Select a feed article or provide an article URL above to generate a brief.</div>", unsafe_allow_html=True)
