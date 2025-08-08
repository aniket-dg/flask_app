from celery import Celery

# Create the celery app instance
celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def log_response(data):
    f = open("response.json", "a+")
    import json
    f.write(json.dumps(data))
    f.close()
    return
