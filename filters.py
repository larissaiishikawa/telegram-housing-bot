from config import (
    MAX_RENT,
    PREFERRED_AREAS,
    SECONDARY_AREAS,
)

def score_listing(item):

    score = 0

    area = item["area"].lower()

    if item["price"] <= MAX_RENT:
        score += 3

    for p in PREFERRED_AREAS:
        if p in area:
            score += 10

    for s in SECONDARY_AREAS:
        if s in area:
            score += 6

    title = item["title"].lower()

    transport_words = [
        "station",
        "bus",
        "halte",
        "ov",
    ]

    if any(x in title for x in transport_words):
        score += 4

    return score
