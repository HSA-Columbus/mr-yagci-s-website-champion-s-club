from flask import *
from flask_mail import Mail, Message
import xlrd
import xlwt

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.hushmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'jipodo2642@mytmail.net'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER'] = 'jipodo2642@mytmail.net'
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

# mail = Mail()
# mail.init_app(app)


@app.route('/')
def index():
    msg = Message('hi there', recipients=['jipodo2642@mytmail.net'])
    msg.body = 'This is a test email sent from jeremiah\'s app. You don\'t have to reply.'
    mail.send(msg)

    return 'Message has been sent!'


if __name__ == '__main__':
    app.run()
