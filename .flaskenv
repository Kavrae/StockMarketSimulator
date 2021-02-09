FLASK_ENV=development
FLASK_APP=StockMarketApi.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:////tmp/StockMarketApi.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
