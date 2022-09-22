import redis
from celery.utils.log import get_task_logger
from celery import Celery
from celery import shared_task



r = redis.Redis(host='localhost',port=6379, db=1)

app = Celery()

logger = get_task_logger(__name__)

@shared_task
def flush_redisdb():
    """flush RedisDb every 24hrs"""

    logger.info("flush redis db")
    r.flushdb()
