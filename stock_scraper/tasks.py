from celery import shared_task
from .models import Stock, Subscriber
from .scrape_data import get_stock_data
from .config import TICKERS

@shared_task
def scrape_stock_data():
    stock_data = []
    for ticker in TICKERS:
        stock_data.append(get_stock_data(ticker))