from flask import Flask, jsonify,render_template, redirect, request, url_for
from flask_mysqldb import  MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False
CORS(app)
mysql=MySQL(app)
  
@app.route('/details_main')
def details_main():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details_main")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    return response
    cur.close()

@app.route('/display')
def display():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details_main")
    fetchdata=cur.fetchall()
    #response=jsonify(fetchdata)
    return render_template("display.html", values = fetchdata)

@app.route('/update/<string:id>', methods = ['GET', 'POST'])
# @app.route('/update', methods = ['GET', 'POST'])
def update(id):
    cur = mysql.connection.cursor()
    if request.method == "POST":
        student_id = request.form['STUDENT_ID']
        name = request.form['NAME']
        dob = request.form ['DOB']
        gender = request.form ['GENDER']
        guardian_name = request.form ['GUARDIAN_NAME']
        address = request.form ['ADDRESS']
        phone_no = request.form ['PHONE_NO']
        doj = request.form ['DOJ']
        sql = "update details_main set student_id = %s , name = %s, dob = %s, gender = %s, guardian_name = %s, address = %s, Phone_no = %s, doj = %s where student_id = %s"
        cur.execute(sql, [student_id, name, dob, gender, guardian_name, address, phone_no, doj, student_id])
        mysql.connection.commit()
        cur.close()
        return redirect (url_for ("display"))
    sql = "select * from details_main where student_id = %s"
    cur.execute(sql, [id])
    fetchdata = cur.fetchone()                   
    return render_template('update.html', data = fetchdata)
    #return redirect (url_for ("display"))

@app.route('/delete/<string:id>', methods = ['GET', 'POST'])
def delete(id):
    cur = mysql.connection.cursor()
    query = "SET foreign_key_checks=0"
    cur.execute(query)
    sql = "delete from details_main where STUDENT_ID = %s"
    cur.execute(sql, [id])
    mysql.connection.commit()
    cur.close()
    return redirect (url_for ("display"))

app.run(port = 3200, debug = True)