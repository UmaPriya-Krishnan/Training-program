from flask import Flask, jsonify,render_template,request,redirect,url_for
from flask_mysqldb import  MySQL
from flask_cors import CORS
import sys
sys.path.append("C:\\Users\\umapriya.krishnan\\Desktop\\student_project\\Student_project-kanth_feature\\src\\test")
import unittest
from ut import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'studentProject'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False

CORS(app)
CORS()
mysql=MySQL(app)

@app.route('/tables')
def tables():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    fetchdata = cur.fetchall()
    tables = jsonify(fetchdata)
    return tables
    cur.close()

@app.route('/')
def tab():
    return render_template('index.html') 

@app.route('/testing', methods=["POST", "GET"])
def testing():
    if request.method == 'POST':
      result = request.json
      x = list(result.values())
      table_name=x[0]
      test_name = 'test_%s_creation' % table_name
      test = test_creation(table_name)
      setattr(check_student, test_name, test)
      test_name = 'test_%s_validation' % table_name
      test2 = test_validations(table_name)
      setattr(check_student, test_name, test2)
      test_name = 'test_%s_insertion' % table_name
      test1 = test_insertion(table_name)
      setattr(check_student, test_name, test1)
      #with open ("templates\\testing.html", "r+") as data:
      data = open ("C:\\Users\\umapriya.krishnan\\Desktop\\angular\\grid\\src\\app\\testing\\testing.component.html", "r+")
      data.seek(0)
      data.truncate()
      runner = unittest.TextTestRunner(data)
      unittest.main(testRunner=runner, exit = False)
      data.flush()
      data.close()          
    return "True"

@app.route('/select/<string:tablename>')
def select(tablename):
    print(tablename)
    cur = mysql.connection.cursor()
    #sql = "SELECT * FROM %s;"
    sql = ("SELECT * FROM {}" .format(tablename))
    cur.execute(sql)
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    x = list(fetchdata[0].keys())
    #print(x[0])
    cur.close()
    return response

@app.route('/update/<string:tablename>', methods = ["POST", "GET"])
def update(tablename):
    if request.method == "POST":
        dataa=request.json
        print(dataa)
        x=list(dataa.values())
        print(x)
        cur = mysql.connection.cursor()
        query = ("SELECT * FROM {}" .format(tablename))
        cur.execute(query)
        fetchdata = cur.fetchall()
        print(fetchdata[0])
        print(type(fetchdata[0]))
        colName = list(fetchdata[0].keys())
        actualLength = len(colName)
        dataLength = len(x[0])
        print(actualLength, dataLength)
        for i in range(1, len(colName)-2):
            if len(colName) == len(x[0]):
            #print(tablename, colName[i],  x[0][i], colName[i-2], colName[0], x[0][0])
                print(i)
                # sql = "update {} set {} = {}, {} = curdate() where {} = {}" .format(tablename, colName[i],  x[0][i], colName[len(colName)-2], colName[0], x[0][0])
                # print(sql)
                sql = "update %s set %s = %s, %s = curdate() where %s = %s;"
                print(sql)
                cur.execute(sql, [tablename, colName[i], x[0][i], colName[len(colName)-2], colName[0], x[0][0]])
            # else:
            #     #n = int(dataLength/actualLength)
            #     #for ct in range(2, n+1):
            #     #print(ct*i)
            #     sql = "update {} set {} = {}, {} = curdate() where {} = {}" .format(tablename, colName[i],  x[0][i], colName[len(colName)-2], colName[0], x[0][0])
            #     print(sql)
            #     print(tablename, colName[i],  x[0][actualLength+i], colName[len(colName)-2], colName[0], x[0][actualLength])
            #         #sql = "update {} set {} = {}, {} = curdate() where {} = {}" .format(tablename, colName[i],  x[0][int(ct*i)], colName[len(colName)-2], colName[0], x[0][actualLength])
                    #print(sql)
            # cur.execute(sql)
            # sql = "update %s set %s = %s, %s = curdate() where %s = %s;"
            # print(sql)
            #cur.execute(sql, [tablename, colName[i], x[0][i], colName[len(colName)-2], colName[0], x[0][0]])
            #mysql.connection.commit()
        cur.close()   
    return "True"

@app.route('/delete/<string:tablename>', methods=["POST", "GET"])
def delete(tablename):
    if request.method == 'POST':
        dataa = request.json
        print(dataa)
        x = list(dataa.values())
        cur = mysql.connection.cursor()
        query = ("SELECT * FROM {}" .format(tablename))
        cur.execute(query)
        fetchdata = cur.fetchall()
        colName = list(fetchdata[0].keys())
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = ("delete from {} where {} = {} ;" .format(tablename, colName[0], x[0][1]))
        # cur.execute(sql)
        # mysql.connection.commit()
        print(sql)
        cur.close()
    return "True" 

app.run(debug = True)