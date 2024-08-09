web: gunicorn stock_tracker_web_app.wsgi
worker: celery -A stock_tracker_web_app worker -l info
beat: celery -A stock_tracker_web_app beat -l info