import random
from django.core.mail import send_mail

def send_verification_code(email: str) -> int:
    code = random.randint(100000, 999999)
    subject = "Код подтверждения"
    message = f"Ваш код подтверждения: {code}"
    send_mail(
        subject,
        message,
        "noreply@example.com",
        [email],
        fail_silently=False,
    )
    return code
