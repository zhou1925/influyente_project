from celery.utils.log import get_task_logger
from celery import Celery
from celery import shared_task
from django.core.mail import send_mail


app = Celery()


logger = get_task_logger(__name__)


# apply_async(kwrags={'email':email'})
@shared_task
def send_mail_celery(**kwrags):
    """ send email by buy boost """
    customer_email = kwargs['email']
    print(customer_email)
    subject = "Boost bought"
    content = "you buyed a boost your time is {}hrs"
    src_email = "test@gmail.com"
    send_mail(subject, content, src_email, [customer_email])
