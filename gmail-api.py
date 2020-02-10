import threading

import conf
from simplegmail import Gmail


gmail = Gmail()

def envia_email(email):
  params = {
    "to": email,
    "sender": conf.de,
    "subject": conf.assunto,
    "msg_html": conf.msg_html,
    "signature": True  # use my account signature
  }

  print("Enviando Email para", email)
  message = gmail.send_message(**params) 


THREADS = []
for email in conf.para.split():
  envia_email(email)
#   t = threading.Thread(target=envia_email, args=[email])
#   THREADS.append(t)

# for t in THREADS:
#   t.start()

# for t in THREADS:
#   t.join()

