from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = "12341234"

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_DB"] = "login1"

db = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
      if request.method == 'POST':
            if 'phonenumber' in request.form and 'password' in request.form:
                  phonenumber = request.form['phonenumber']
                  password = request.form['password']
                  cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
                  cursor.execute("SELECT * FROM details WHERE phnm=%s AND password=%s", (phonenumber, password))
                  info = cursor.fetchone()
                  print(info)
                  if info['phnm'] == phonenumber and info['password'] == password:
                        return "login successful"
                  else:
                        return "login unsuccessful, please register"
      return render_template("login.html")

if __name__ == '__main__':
      app.run(debug=True)