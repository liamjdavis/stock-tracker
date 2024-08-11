web: gunicorn stock_tracker_web_app.wsgi
worker: celery -A stock_tracker_web_app worker --loglevel=info
beat: celery -A stock_tracker_web_app beat --loglevel=info