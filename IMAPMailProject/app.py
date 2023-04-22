from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import imaplib

app = Flask(__name__)
app.secret_key = 'any random string'
app.permanent_session_lifetime = timedelta(minutes=25)

@app.route("/")
@app.route("/start")
def start():
   return render_template("login.html")

@app.route("/login", methods=['POST','GET'])
def login():
   if request.method == "POST":
      session.permanent = True
      session['username'] = request.form['username']
      session['password'] = request.form['password']
      return redirect(url_for('auth'))

@app.route("/auth")
def auth():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']

   #connect to host using SSL
   imap = imaplib.IMAP4_SSL('imap.gmail.com')

   #login to server
   try:
      connection = imap.login(userid,passwd)
      print("<h1>Connected: Login Successful</h1>"+"\n")
      return redirect(url_for('home'))
   except Exception as e:
      print("<h1>AUTHENTICATION FAILED!</h1>"+"\n",e)
      return redirect(url_for('start'))

@app.route("/home")
def home():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']
      return render_template("home.html",uname = userid, pwd = passwd)

@app.route("/mails")
def mails():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']
      return render_template("mails.html",uname = userid, pwd = passwd)

@app.route("/SelectMailsDeletion")
def SelectMailsDeletion():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']
      return render_template("SelectMailsDeletion.html",uname = userid, pwd = passwd)

@app.route("/FromSearchForm")
def FromSearchForm():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']
      return render_template("FromSearchForm.html",uname = userid, pwd = passwd)

@app.route("/BodySearchForm")
def BodySearchForm():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']
      return render_template("BodySearchForm.html",uname = userid, pwd = passwd)

@app.route("/SinceDateForm")
def SinceDateForm():
   if "username" and "password" in session:
      userid = session['username']
      passwd = session['password']
      return render_template("SinceDateForm.html",uname = userid, pwd = passwd)

@app.route("/logout")
def logout():
   session.pop('username',None); 
   session.pop('password',None);
   session.pop('subject',None); 
   session.pop('from',None);
   session.pop('date',None);
   return redirect(url_for('start'))
   quit()

if __name__=='__main__':
   app.run(debug=True)