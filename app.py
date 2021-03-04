from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL

from flask import Flask
from flask import render_template, redirect, flash
from flask import request
from flask_sqlalchemy import SQLAlchemy
from Result import Customer


app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'viet'
app.config['MYSQL_DB'] = 'classicmodels'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)
# db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST', 'GET'])
def search_results():
    cur = mysql.connection.cursor()
    result = []
    query = request.form['query_string']
    number = int(request.form['number'])
    print(number)
    if request.method == 'POST':
        query_field = request.form['field']
        if query_field == 'number':
            num_customers = cur.execute('Select customerNumber, customerName, phone, addressLine1, city, country from customers where customerNumber = %d limit %d' % (int(query), number))
            if num_customers > 0:
                result = cur.fetchall()
                # print(result)
        elif query_field == 'name':
            likeString = "'" + query + "%%'"
            num_customers = cur.execute(
                "Select customerNumber, customerName, phone, addressLine1, city, country from customers where customerName like %s limit %d" % (likeString, number))
            if num_customers > 0:
                result = cur.fetchall()
                # print(result)
        elif query_field == 'phone':
            likeString = "'" + query + "%%'"
            num_customers = cur.execute(
                "Select customerNumber, customerName, phone, addressLine1, city, country from customers where phone like %s limit %d" % (likeString, number))
            if num_customers > 0:
                result = cur.fetchall()
        elif query_field == 'address':
            likeString = "'" + query + "%%'"
            num_customers = cur.execute(
                "Select customerNumber, customerName, phone, addressLine1, city, country from customers where addressLine1 like %s limit %d" % (likeString, number))
            if num_customers > 0:
                result = cur.fetchall()
    if len(result) == 0:
        return "Not found anyone"
    else:
        return render_template('result.html', customers=result)

if __name__ == '__main__':
    app.run()
