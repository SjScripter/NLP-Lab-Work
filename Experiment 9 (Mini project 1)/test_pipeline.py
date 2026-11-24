"""
Unit & Integration Test for News Reel Generator Pipeline
"""

from nlp_pipeline import (
    preprocess_text,
    extractive_textrank,
    detect_topic,
    generate_reel_script,
    generate_social_assets,
    evaluate_summaries,
    verify_facts
)

sample_news = """
The Indian Space Research Organisation (ISRO) on Sunday announced the launch date for its next-generation solar monitoring satellite.
Scientists confirmed that the mission aims to study coronal mass ejections and space weather phenomena that affect global communication networks.
ISRO Chairman highlighted that over 500 engineers worked on the payload over the past three years.
The satellite will be positioned at the Sun-Earth Lagrangian point L1, roughly 1.5 million kilometers from Earth.
Officials stated that international space agencies including NASA and ESA have expressed interest in sharing data from this mission.
Launch preparations are in full swing at the Satish Dhawan Space Centre in Sriharikota, with liftoff scheduled for next month.
"""

def test_pipeline():
    print("Testing Preprocessing...")
    prep = preprocess_text(sample_news)
    assert len(prep["sentences"]) >= 4, f"Sentences: {len(prep['sentences'])}"
    print(f"Sentences detected: {len(prep['sentences'])}")
    print(f"Keywords: {prep['keywords']}")
    print(f"Entities: {prep['entities'][:5]}")

    print("\nTesting Topic Detection...")
    topic = detect_topic(sample_news)
    print(f"Detected Topic: {topic}")
    assert topic == "Space & Science"

    print("\nTesting TextRank Extractive Summarization...")
    extractive = extractive_textrank(prep["sentences"], num_sentences=3)
    assert len(extractive) == 3
    for i, s in enumerate(extractive, 1):
        print(f"  {i}. {s}")

    print("\nTesting Reel Script Generation (Informative)...")
    reel = generate_reel_script(extractive, topic=topic, tone="Informative", target_words=80, keywords=prep["keywords"])
    print("Script Generated:")
    print("Hook:", reel["hook"])
    print("Body:", reel["body"])
    print("Closer:", reel["closer"])
    print(f"Words: {reel['word_count']} | Duration: {reel['est_duration_sec']}s")
    assert 20 <= reel["est_duration_sec"] <= 40

    print("\nTesting Social Assets Generation...")
    social = generate_social_assets("ISRO Solar Mission", topic, prep["keywords"], "Informative")
    print("Screen cards:", social["screen_cards"])
    print("Hashtags:", social["hashtags"])

    print("\nTesting Fact Safety...")
    facts = verify_facts(prep["entities"], reel["full_script"])
    print(f"Fact Safety Score: {facts['safety_score']}%")
    print(f"Numbers Found: {facts['numbers_found']}")

    print("\nTesting ROUGE Evaluation...")
    rouge = evaluate_summaries(sample_news, " ".join(extractive), reel["full_script"])
    print(f"ROUGE-1: {rouge['rouge1']}")
    print(f"ROUGE-2: {rouge['rouge2']}")
    print(f"ROUGE-L: {rouge['rougeL']}")

    print("\n--- ALL TESTS PASSED! ---")

if __name__ == "__main__":
    test_pipeline()
