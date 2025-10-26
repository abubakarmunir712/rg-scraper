def fetch_dummy_api_data(topic: str):
    # Return dummy JSON
    return [
        {"title": f"Paper 1 on {topic}", "abstract": "Abstract 1"},
        {"title": f"Paper 2 on {topic}", "abstract": "Abstract 2"}
    ]
