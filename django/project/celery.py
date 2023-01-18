import os

from celery import Celery
from celery import current_app
import requests

current_app.conf.CELERY_ALWAYS_EAGER = True
current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.dev')

app = Celery('project')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, get_status_loan.s())

@app.task
def get_status_loan():
    print(os.getenv("DJANGO_APP_API_ROOT_URL") + "api/status/")
    requests.get(os.getenv("DJANGO_APP_API_ROOT_URL") + "api/status/", verify=False)