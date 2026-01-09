def calculate_confidence(num_sources: int, num_chunks: int) -> str:
    score = min(100, (num_sources * 20) + (num_chunks * 5))

    if score >= 80:
        return "High Confidence"
    elif score >= 50:
        return "Medium Confidence"
    else:
        return "Low Confidence"
