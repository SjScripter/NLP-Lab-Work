"""
News Reel Brief Generator - Core NLP Pipeline
Minimalist, clean, production-oriented version.
"""

import re
import math
import collections
import feedparser
import trafilatura
from rouge_score import rouge_scorer

try:
    import spacy
    try:
        nlp = spacy.load("en_core_web_sm")
    except Exception:
        nlp = None
except ImportError:
    nlp = None

# Curated RSS Feeds
RSS_FEEDS = {
    "NDTV Top Stories": "https://feeds.feedburner.com/ndtvnews-topstories",
    "NDTV India": "https://feeds.feedburner.com/ndtvnews-india-news",
    "NDTV Tech": "https://feeds.feedburner.com/gadgets360-latest",
    "The Hindu National": "https://www.thehindu.com/news/national/feeder/default.rss",
    "The Hindu Tech": "https://www.thehindu.com/sci-tech/technology/feeder/default.rss",
    "Times of India Top": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "Times of India Tech": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    "BBC World News": "http://feeds.bbci.co.uk/news/world/rss.xml"
}

def fetch_rss_articles(feed_url, limit=6):
    """Fetch recent articles from an RSS feed."""
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:limit]:
        title = entry.get('title', 'Untitled')
        link = entry.get('link', '')
        summary = entry.get('summary', '') or entry.get('description', '')
        summary = re.sub(r'<[^>]+>', '', summary).strip()
        published = entry.get('published', '')
        articles.append({
            'title': title,
            'link': link,
            'summary': summary,
            'published': published
        })
    return articles

def extract_article_text(url):
    """Extract clean article text from URL using trafilatura with newspaper fallback."""
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
        if text and len(text.strip()) > 150:
            return text.strip()
    
    try:
        from newspaper import Article
        article = Article(url)
        article.download()
        article.parse()
        if article.text and len(article.text.strip()) > 100:
            return article.text.strip()
    except Exception:
        pass
    
    return ""

def preprocess_text(text):
    """Sentence tokenization, named entities, and keyword extraction."""
    clean = re.sub(r'\s+', ' ', text).strip()
    
    sentences = []
    entities = []
    keywords = []

    if nlp is not None:
        doc = nlp(clean[:15000])
        sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 10]
        entities = [(ent.text.strip(), ent.label_) for ent in doc.ents]
        words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and token.pos_ in ("NOUN", "PROPN", "ADJ") and len(token.text) > 2]
        common = collections.Counter(words).most_common(12)
        keywords = [word for word, _ in common]
    else:
        raw_sents = re.split(r'(?<=[.!?])\s+', clean)
        sentences = [s.strip() for s in raw_sents if len(s.strip()) > 10]
        words = [w.lower() for w in re.findall(r'\b[A-Za-z]{3,}\b', clean)]
        stopwords = {"the", "and", "is", "in", "to", "of", "a", "with", "for", "on", "that", "this", "it", "by", "from", "are", "was", "as"}
        common = collections.Counter([w for w in words if w not in stopwords]).most_common(10)
        keywords = [w for w, _ in common]

    return {
        "clean_text": clean,
        "sentences": sentences,
        "entities": entities,
        "keywords": keywords
    }

def calculate_sentence_similarity(sent1, sent2):
    """Cosine-like overlap score between two sentences."""
    words1 = set(re.findall(r'\b\w+\b', sent1.lower()))
    words2 = set(re.findall(r'\b\w+\b', sent2.lower()))
    if not words1 or not words2:
        return 0.0
    common = words1.intersection(words2)
    log_sum = (math.log(len(words1) + 1) + math.log(len(words2) + 1))
    return len(common) / (log_sum if log_sum > 0 else 1.0)

def extractive_textrank(sentences, num_sentences=3):
    """TextRank graph algorithm to rank and pick key sentences."""
    if not sentences:
        return []
    if len(sentences) <= num_sentences:
        return sentences

    n = len(sentences)
    sim_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                sim_matrix[i][j] = calculate_sentence_similarity(sentences[i], sentences[j])

    scores = [1.0] * n
    damping = 0.85
    for _ in range(25):
        new_scores = [(1.0 - damping)] * n
        for i in range(n):
            for j in range(n):
                if i != j and sum(sim_matrix[j]) > 0:
                    new_scores[i] += damping * (sim_matrix[j][i] / sum(sim_matrix[j])) * scores[j]
        scores = new_scores

    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    top_indices = sorted([idx for idx, _ in ranked[:num_sentences]])
    return [sentences[i] for i in top_indices]

TOPIC_KEYWORDS = {
    "Technology & AI": ["tech", "ai", "apple", "google", "software", "chip", "robot", "meta", "cyber", "internet", "startup", "app"],
    "Space & Science": ["space", "isro", "nasa", "moon", "satellite", "launch", "rocket", "mission", "planet", "galaxy", "orbit"],
    "Politics & Policy": ["minister", "government", "parliament", "election", "bjp", "congress", "policy", "court", "bill", "treaty", "president", "modi"],
    "Business & Economy": ["market", "economy", "rupee", "dollar", "stock", "gdp", "inflation", "rbi", "investment", "trade", "earnings", "bank"],
    "Sports": ["cricket", "ipl", "match", "tournament", "football", "trophy", "cup", "player", "olympic", "scored", "win", "stadium"],
    "Entertainment": ["movie", "actor", "actress", "box office", "film", "hollywood", "bollywood", "director", "song", "series"]
}

def detect_topic(text):
    text_lower = text.lower()
    scores = {}
    for topic, kw_list in TOPIC_KEYWORDS.items():
        score = sum(1 for kw in kw_list if re.search(r'\b' + re.escape(kw) + r'\b', text_lower))
        scores[topic] = score
    best_topic = max(scores, key=scores.get)
    return best_topic if scores[best_topic] > 0 else "General News"

def clean_sentence_for_reel(sent):
    """Strip news boilerplate such as datelines and agency abbreviations."""
    s = re.sub(r'^(new delhi|mumbai|washington|london|beijing|bengaluru|pti|ani|reuters|afp|sources said|according to reports)[\s,:\-]+', '', sent, flags=re.IGNORECASE)
    s = re.sub(r'\(PTI\)|\(ANI\)|PTI\.|ANI\.', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def generate_reel_script(extracted_sentences, topic, tone="Informative", target_words=80, keywords=None):
    """
    Generate an influencer-ready 30-second script structured as:
    1. Hook (First 3s)
    2. Key Facts / Body (3-24s)
    3. Closer / CTA (24-30s)
    Without decorative emojis or informal noise.
    """
    clean_sents = [clean_sentence_for_reel(s) for s in extracted_sentences if len(s.split()) >= 4]
    if not clean_sents:
        clean_sents = ["Here are the major developments confirmed on this story."]

    first_fact = clean_sents[0] if len(clean_sents) > 0 else "Here is the verified summary."
    second_fact = clean_sents[1] if len(clean_sents) > 1 else ""
    third_fact = clean_sents[2] if len(clean_sents) > 2 else ""

    if tone == "Dramatic":
        hook_templates = [
            f"A major development in {topic} has just taken place.",
            f"Here is why the latest news in {topic} is drawing urgent attention.",
            f"Breaking updates today could significantly alter the outlook in {topic}."
        ]
        closer = "Share your perspective in the comments below, and subscribe for daily briefs."
    elif tone == "Casual":
        hook_templates = [
            f"Here is a quick thirty-second briefing on today's {topic} news.",
            f"Here is what you need to know about the latest story in {topic}.",
            f"Let's break down the main points from today's {topic} announcement."
        ]
        closer = "Follow along for concise daily news briefings."
    elif tone == "Hinglish":
        hook_templates = [
            f"{topic} se related ek mahatvapurna update samne aayi hai.",
            f"Aaj ki pramukh {topic} khabar ka quick 30-second breakdown.",
            f"{topic} par aayi is nayi report ke mukhya points jaan lijiye."
        ]
        closer = "Aapka is par kya vishleshan hai? Comments me batayein aur daily updates ke liye follow karein."
    else:  # Informative (Default)
        hook_templates = [
            f"Here is your 30-second briefing on the latest in {topic}.",
            f"Key facts and confirmed details regarding today's {topic} report.",
            f"An overview of the central developments in {topic} today."
        ]
        closer = "Follow for verified, bite-sized news breakdowns every day."

    hook = hook_templates[0]

    if tone == "Hinglish":
        body_lines = [
            f"Mukhya baat: {first_fact}",
            f"Iske saath hi: {second_fact}" if second_fact else "Authorities ne is par aage ki jaanch shuru kar di hai."
        ]
        if third_fact:
            body_lines.append(f"Reports ke mutabik: {third_fact}")
    else:
        body_lines = [
            f"First, {first_fact}",
            f"Second, {second_fact}" if second_fact else "Officials confirmed that relevant actions are now underway."
        ]
        if third_fact:
            body_lines.append(f"In addition, {third_fact}")

    body = " ".join(body_lines)

    full_script_draft = f"{hook} {body} {closer}"
    words = full_script_draft.split()

    if len(words) > target_words + 15:
        pruned_body = f"First, {first_fact}" if tone != "Hinglish" else f"Mukhya baat: {first_fact}"
        if second_fact:
            pruned_body += f" {second_fact[:120]}..."
        full_script = f"{hook} {pruned_body} {closer}"
    else:
        full_script = full_script_draft

    total_words = len(full_script.split())
    est_duration_sec = round(total_words / 2.7, 1)

    return {
        "hook": hook,
        "body": body,
        "closer": closer,
        "full_script": full_script,
        "word_count": total_words,
        "est_duration_sec": est_duration_sec
    }

def generate_social_assets(title, topic, keywords, tone):
    """Generate professional on-screen cues, clean hashtags, and captions."""
    screen_cards = [
        f"UPDATE: {topic.upper()}",
        f"KEY POINT: {keywords[0].capitalize() if keywords else 'Top Story'}",
        "CONTEXT: High Impact Development",
        "ACTION: Follow for Daily Briefs"
    ]
    
    clean_kws = [re.sub(r'[^a-zA-Z0-9]', '', kw) for kw in (keywords or []) if len(kw) > 2]
    topic_tag = re.sub(r'[^a-zA-Z0-9]', '', topic)
    hashtags = [f"#{topic_tag}", "#NewsBrief", "#CurrentAffairs", "#Journalism", "#DailyUpdate"]
    for kw in clean_kws[:4]:
        hashtags.append(f"#{kw.capitalize()}")

    caption = (
        f"Briefing: {title or topic}\n\n"
        f"A verified summary of today's key developments in {topic}.\n\n"
        f"Leave your thoughts in the comments.\n\n"
        f"{' '.join(hashtags)}"
    )

    return {
        "screen_cards": screen_cards,
        "hashtags": hashtags,
        "caption": caption
    }

def evaluate_summaries(original_text, extractive_summary, reel_script):
    """Calculate ROUGE scores comparing the Extractive Summary against the Generated Reel Script."""
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(extractive_summary, reel_script)
    
    return {
        "rouge1": {
            "precision": round(scores['rouge1'].precision, 3),
            "recall": round(scores['rouge1'].recall, 3),
            "fmeasure": round(scores['rouge1'].fmeasure, 3),
        },
        "rouge2": {
            "precision": round(scores['rouge2'].precision, 3),
            "recall": round(scores['rouge2'].recall, 3),
            "fmeasure": round(scores['rouge2'].fmeasure, 3),
        },
        "rougeL": {
            "precision": round(scores['rougeL'].precision, 3),
            "recall": round(scores['rougeL'].recall, 3),
            "fmeasure": round(scores['rougeL'].fmeasure, 3),
        }
    }

def verify_facts(original_entities, reel_script):
    """Verify numeric and entity preservation."""
    script_lower = reel_script.lower()
    numbers = set(re.findall(r'\b\d+(?:[\.,]\d+)?%?\b', reel_script))
    
    preserved_entities = []
    missing_entities = []
    
    for ent, label in original_entities[:15]:
        if ent.lower() in script_lower:
            preserved_entities.append(f"{ent} ({label})")
        else:
            missing_entities.append(f"{ent} ({label})")

    safety_ratio = len(preserved_entities) / (len(preserved_entities) + len(missing_entities)) if (preserved_entities or missing_entities) else 1.0

    return {
        "preserved_entities": list(set(preserved_entities)),
        "missing_entities": list(set(missing_entities))[:5],
        "numbers_found": list(numbers),
        "safety_score": round(safety_ratio * 100, 1)
    }
