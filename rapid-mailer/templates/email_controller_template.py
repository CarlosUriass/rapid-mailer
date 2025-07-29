from fastapi import APIRouter, Depends, HTTPException
from app.schemas.email_schema import EmailRequest
from app.domain.services import SendEmailUseCase
from app.infrastructure.resend_client import ResendClient
from app.domain.models import Email

router = APIRouter()

def get_resend_client():
    return ResendClient()

def get_send_email_use_case(resend_client: ResendClient = Depends(get_resend_client)):
    return SendEmailUseCase(resend_client)

@router.post("/send")
async def send_email_endpoint(
    email_request: EmailRequest,
    send_email_use_case: SendEmailUseCase = Depends(get_send_email_use_case)
):
    email = Email(
        to=email_request.to,
        subject=email_request.subject,
        body=email_request.body
    )
    try:
        await send_email_use_case.execute(email)
        return {"message": "Email enviado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))