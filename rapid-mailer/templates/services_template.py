from app.infrastructure.resend_client import ResendClient
from app.domain.models import Email

class SendEmailUseCase:
    def __init__(self, resend_client: ResendClient):
        self.resend_client = resend_client

    async def execute(self, email: Email):
        await self.resend_client.send_email(email)