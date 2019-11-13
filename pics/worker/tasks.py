import os
import logging

from .worker import app
from django.conf import settings


logger = logging.getLogger(__name__)


@app.task(bind=True, name='send_pictures_to_email')
def send_pictures_to_email(filepath):
    import time; time.sleep(5)

