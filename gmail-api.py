import configparser
import codecs
import os

from simplegmail import Gmail


gmail = Gmail()

caminho = os.path.abspath(os.getcwd())
caminho_conf = '{}\\conf.ini'.format(caminho)
caminho_emails = '{}\\emails.txt'.format(caminho)
caminho_corpo_email = '{}\\corpo_email.html'.format(caminho)

config = configparser.ConfigParser()
config.read(caminho_conf)

emails = codecs.open(caminho_emails, 'r')
emails = emails.read().split()

corpo_email = codecs.open(caminho_corpo_email, 'r')
corpo_email = corpo_email.read()

def envia_email(email):
  params = {
    "to": email,
    "sender": config.get('email', 'de'),
    "subject": config.get('email', 'assunto'),
    "msg_html": corpo_email,
    "signature": True  # use my account signature
  }

  print("Enviando Email para", email)
  gmail.send_message(**params) 


for email in emails:
  envia_email(email)
