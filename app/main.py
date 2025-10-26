from fastapi import FastAPI
from app.scraper.scraper import fetch_dummy_data

app = FastAPI(title="Scraper Microservice")

@app.get("/scrape")
def scrape(topic: str):
    """
    Dummy endpoint to fetch scraped data for a topic.
    """
    data = fetch_dummy_data(topic)
    return {"topic": topic, "papers": data}
