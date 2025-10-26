from app.api_fetcher.api_fetcher import fetch_dummy_api_data

def fetch_dummy_data(topic: str):
    # Fetch dummy papers
    papers = fetch_dummy_api_data(topic)
    return papers
