from flask import Flask, render_template, request
import mysql.connector
from random import randint

application = Flask(__name__, template_folder="template")

application.static_folder = 'static'

@application.route('/')
def index():
    return render_template("pager1.html")

@application.route('/', methods = ["POST"])
def validation():
    conn = mysql.connector.connect(database = "flask_booking", user="root", password = "Riddhi@14", auth_plugin='mysql_native_password')
    cur = conn.cursor()
    fname = request.form["fname"]
    fl = fname[0].upper()
    fname = fl + fname[1:len(fname)]

    email = request.form["email"]

    phnumber = request.form["phnumber"]

    fromPlace = request.form["fromPlace"]
    fpl = fromPlace[0].upper()
    fromPlace = fpl + fromPlace[1:len(fromPlace)]
    
    toPlace = request.form["toPlace"]
    tpl = toPlace[0].upper()
    toPlace = tpl + toPlace[1:len(toPlace)]

    ddate = request.form["ddate"]
    
    class_seat = request.form["class"]
    cl = class_seat[0].upper()
    class_seat = cl + class_seat[1:len(class_seat)]
    
    bookingno = randint(0,100000)

    cur.execute("INSERT INTO names VALUES ({0}, '{1}', '{2}', {3},'{4}', '{5}','{6}','{7}')".format(bookingno, fname,email,phnumber,fromPlace,toPlace,ddate,class_seat))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("pager2.html",bid = bookingno, uname = fname, mail=email, phno = phnumber,fplace = fromPlace,tplace= toPlace,depdate = ddate, cs =class_seat)

if __name__ == '__main__':
    # app.run(debug=True)
    application.run()





