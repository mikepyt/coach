import os

import sendgrid
from dotenv import load_dotenv
from sendgrid.helpers.mail import *

load_dotenv()
API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")


def send(estudiantes_asignados: list):
    """Envio de correos de bienvenida

    Args:
        estudiantes asignados(list): estudiantes asignados a enviar bienvenida
    """
    emails = [i["CORREO"] for i in estudiantes_asignados]
    for email in emails:
        sg = sendgrid.SendGridAPIClient(api_key=API_KEY)
        from_email = Email(FROM_EMAIL)

        mail = Mail(from_email, to_emails=email)
        mail.template_id = "d-200e9a65c99e45639f30e693ec86f3f3"
        response = sg.client.mail.send.post(request_body=mail.get())

        print(f"Correo enviado al estudiante: {email}")

    print("Correo enviado a todos los estudiantes asignados")
