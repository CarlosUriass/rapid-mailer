import httpx
from app.core.config import RESEND_API_KEY
from app.core.config import EMAIL_SENDER
from app.domain.models import Email

class ResendClient:
    def __init__(self):
        self.api_key = RESEND_API_KEY
        self.base_url = "https://api.resend.com"

    async def send_email(self, email: Email):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        json_data = {
            "from": EMAIL_SENDER,
            "to": [email.to],
            "subject": email.subject,
            "html": email.body
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/emails", headers=headers, json=json_data)
            response.raise_for_status()