# chatbot.py
import json
import random
import spacy
import os
from typing import List

# Load spaCy medium model (must be installed: python -m spacy download en_core_web_md)
nlp = spacy.load("en_core_web_md")

# Load intents file
INTENTS_FILE = "intents.json"
if not os.path.exists(INTENTS_FILE):
    raise FileNotFoundError(f"{INTENTS_FILE} not found in current directory.")

with open(INTENTS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Build patterns and tag mapping
patterns: List[str] = []
tags: List[str] = []

for intent in data.get("intents", []):
    tag = intent.get("tag")
    for p in intent.get("patterns", []):
        patterns.append(p)
        tags.append(tag)

# Preprocessing: lowercase, lemmatize, remove stopwords & non-alpha tokens
def preprocess(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens) if tokens else text.lower()

# Create vector for each pattern (use preprocess -> spaCy vector)
pattern_vectors = []
for p in patterns:
    vec = nlp(preprocess(p)).vector
    pattern_vectors.append(vec)

# Cosine similarity helper
def cosine_similarity(a, b) -> float:
    # a, b are numpy-like vectors
    denom = ( (a**2).sum()**0.5 ) * ( (b**2).sum()**0.5 )
    if denom == 0:
        return 0.0
    return float(a.dot(b) / denom)

# Get response using semantic similarity
def get_response(user_input: str, threshold: float = 0.55):
    # Preprocess and vectorize user input
    proc = preprocess(user_input)
    user_vec = nlp(proc).vector

    # Compute similarity to each pattern
    sims = []
    for vec in pattern_vectors:
        sims.append(cosine_similarity(user_vec, vec))

    # If there are no patterns, fallback
    if not sims:
        return random.choice(next((it["responses"] for it in data["intents"] if it["tag"] == "unknown"), ["Sorry, I don't understand."])), 0.0

    best_index = int(max(range(len(sims)), key=lambda i: sims[i]))
    best_score = sims[best_index]

    # Decide tag based on threshold
    if best_score < threshold:
        tag = "unknown"
    else:
        tag = tags[best_index]

    # Pick a random response from that tag
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent.get("responses", ["Sorry, I don't understand."])), best_score

    # Final fallback
    return "Sorry, I don't understand.", best_score

# CLI runner
if __name__ == "__main__":
    print("Chatbot (spaCy vectors) ready. Type 'quit' to exit.")
    while True:
        try:
            user = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

        if not user:
            continue

        if user.lower() in ("quit", "exit"):
            print("Bot: Goodbye!")
            break

        response, score = get_response(user)
        # Show score for debugging — remove or hide in final submission if you prefer
        print(f"Bot ({score:.2f}): {response}")
