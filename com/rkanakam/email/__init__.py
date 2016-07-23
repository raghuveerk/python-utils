from smtplib import SMTP              # sending email
from email.mime.text import MIMEText  # constructing messages

from jinja2 import Environment        # Jinja2 templating


TEMPLATE = """
<html>
<head>
<title>{{ title }}</title>
</head>
<body>

<b>Hello World!.</b>

</body>
</html>
"""  # Our HTML Template

# Create a text/html message from a rendered template
msg = MIMEText(
    Environment().from_string(TEMPLATE).render(
        title='Hello World!'
    ), "html"
)

subject = "Subject Line"
sender= "raghuveer.kanakamedala@gmail.com"
recipient = "raghuveerk@outlook.com"

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Send the message via our own local SMTP server.
s = SMTP('localhost')
s.sendmail(sender, [recipient], msg.as_string())
s.quit()