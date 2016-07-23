from smtplib import SMTP              # sending email
from email.mime.text import MIMEText  # constructing messages

from jinja2 import Environment        # Jinja2 templating
from jinja2 import FileSystemLoader

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
subject = "Dengi tagutunnara!!!"
sender= "raghuveer.kanakamedala@gmail.com"
recipient = "raghuveerk@outlook.com, pradeepv.datla@gmail.com"
# Specify any input variables to the template as a dictionary.
templateVars = { "name" : "Pedda raju..."}
TEMPLATE_FILE = "/Users/raghuveerk/workspace/python-utils/python-utils/com/rkanakam/email/templates/sample_template.html"

templateLoader = FileSystemLoader( searchpath= "/" )
templateEnv = Environment(loader=templateLoader)
template = templateEnv.get_template( TEMPLATE_FILE )
outputText = template.render( templateVars )

# Create a text/html message from a rendered template
msg = MIMEText(outputText, "html")


msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Send the message via our own local SMTP server.
s = SMTP('localhost')
s.sendmail(sender, [recipient], msg.as_string())
s.quit()