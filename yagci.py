from flask import *
import xlrd
import xlwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import json
from pathlib import Path



def contact_yagci(studentname, studentemail, studentmessage):
    email = "imnotarobotlol1234@gmail.com"
    password = "imnotarobot"
    send_to_email = "imnotarobotlol1234@gmail.com"
    subject = 'Question from student'
    message = "\nFrom: " + str(studentname) + "\nStudent Name: " + str(studentemail) + "\nMessage: {}".format(studentmessage)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        return 1
    except:
        return 0


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'yagci' or request.form['password'] != 'tagci2':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/assignments')
def assignments():
    with sqlite3.connect("Thisistest.db") as conn:
        command1 = "SELECT * FROM table_assignments"
        cursor1 = conn.execute(command1)
        table_assignments = cursor1.fetchall()
        # print(table_assignments)
    return render_template("assignments.html", table_assignments=table_assignments)


@app.route('/assignment_creation')
def assignment_creation():
    return render_template("assign_take.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        result = contact_yagci(request.form['name'], request.form['email'], request.form['message'])
        if result == 1:
            return render_template('contact.html', result="Email was sent successfully.")
        elif result == 0:
            return render_template('contact.html', result="Email was not successfully sent.")
    else:
        return render_template("contact.html")


@app.route('/background')
def background():
    return render_template("background.html")


if __name__ == "__main__":
    app.run(debug=True)
