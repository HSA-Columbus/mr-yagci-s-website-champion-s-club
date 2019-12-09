from flask import *
import xlrd
import xlwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import json
from pathlib import Path
# --------this works------
with sqlite3.connect("Thisistest.db") as conn:
    command = "SELECT * FROM table_assignments"
    cursor = conn.execute(command)
    table_assignments = cursor.fetchall()
    print(table_assignments)
# --------this works------

app = Flask(__name__)


@app.route('/contact')
def contact1():
    return render_template("contact.html")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/assignments')
def assignments():
    with sqlite3.connect("Thisistest.db") as conn:
        command = "SELECT * FROM table_assignments"
        cursor = conn.execute(command)
        table_assignments = cursor.fetchall()
        # print(table_assignments)
    return render_template("assignments.html", table_assignments=table_assignments)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    email = "imnotarobotlol1234@gmail.com"
    password = "imnotarobot"
    send_to_email = "imnotarobotlol1234@gmail.com"
    subject = 'Question from student'
    name = request.form['name']
    email1 = request.form['email']
    message = request.form['message'] + "\nFrom: " + str(email1) + "\nStudent Name: " + str(name)

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
    return render_template("contact.html")


@app.route('/background')
def background():
    return render_template("background.html")


if __name__ == "__main__":
    app.run(debug=True)
