import sys
import json

# Load the sentiment keywords
with open("keywords.json", "r") as f:
    keywords = json.load(f)

positive_keywords = set(keywords["positive"])
negative_keywords = set(keywords["negative"])

# Mapper function
for line in sys.stdin:
    review = line.strip().split(",")[1].lower()
    positive_count = sum(1 for word in review.split() if word in positive_keywords)
    negative_count = sum(1 for word in review.split() if word in negative_keywords)

    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"{sentiment}\t1")
