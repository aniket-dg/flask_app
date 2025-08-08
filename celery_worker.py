from tasks import celery_app

# This makes sure the worker picks up the tasks in tasks.py
celery_app.worker_main()
