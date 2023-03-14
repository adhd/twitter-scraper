import configparser
from celery import Celery

config = configparser.ConfigParser()
config.read('config.ini')

app = Celery(
    'celery_main',
    broker=config['celery']['broker'],
    backend='rpc://',
    include=['celery_main.task_receiver']
)