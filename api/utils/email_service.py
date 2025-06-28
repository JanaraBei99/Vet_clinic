from datetime import datetime
from django.utils import timezone

from django.utils.crypto import get_random_string
import smtplib
import ssl
from email.message import EmailMessage

from core import settings


class EmailService:
    def send_confirmation_email(self, receiver_email, confirmation_code):
        subject = "Ваш код подтверждения"
        body = f"Ваш код подтверждения: {confirmation_code}"

        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as server:
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Ошибка отправки: {e}")
            return False


    def generate_and_send_code(self, user):
        code = get_random_string(length=6, allowed_chars='0123456789')
        user.code = code
        user.is_used = False
        user.code_created_at = timezone.now()
        user.save()

        return self.send_confirmation_email(user.email, code)

    def verify_code(self, user, code):
        if user.code != code or user.is_used or user.is_code_expired():
            return False

        user.is_used = True
        user.is_active = True
        user.save()
        return True
