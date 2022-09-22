from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """ Send password recovery key """
    email_plaintext_message = "{}".format(reset_password_token.key)
    send_mail("password Reset", email_plaintext_message, "elnoobitaz@gmail.com", [reset_password_token.user.email])
    
