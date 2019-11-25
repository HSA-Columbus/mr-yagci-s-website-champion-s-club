from flask import *
import xlrd
import xlwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def contactyagci():
    global email, password, message
    email = email
    password = password
    send_to_email = "bb4007670@gmail.com"
    subject = 'Question from student'
    message = message

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()


app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/assignments')
def assignments():
    return render_template("assignments.html")


@app.route('/contact', methods=['POST'])
def contact():
    global email, password, message
    email = request.form['email']
    password = request.form['password']
    message = request.form['message']
    return render_template("contact.html")


@app.route('/background')
def background():
    return render_template("background.html")


if __name__ == "__main__":
    app.run(debug=True)
