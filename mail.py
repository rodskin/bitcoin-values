#!/usr/bin/env python
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

import config as cfg

msg = MIMEText("Hello from exim")
msg["From"] = "noreply@localhost"
msg["To"] = cfg.email_to
msg["Subject"] = "Python sendmail test"
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
p.communicate(msg.as_string())
