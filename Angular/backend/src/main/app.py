from flask import Flask, jsonify,render_template,request,redirect,url_for
from flask_mysqldb import  MySQL
import MySQLdb
from flask_cors import CORS
import sys
import json
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
mysql=MySQL(app)

@app.route('/tables')
def tables():
    ''' To get the tables present in the selected db'''
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    fetchdata = cur.fetchall()
    tables = jsonify(fetchdata)
    return tables
    cur.close()

@app.route('/testing', methods=["POST", "GET"])
def testing():
    ''' To perform unittesting to check if the table creation and value insertion are done properly'''
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
    ''' To display the data whenever a table is selected - only active rows will be displayed'''
    try:
        cur = mysql.connection.cursor()
        sql = ("SELECT * FROM {} where ACTIVE_FLAG = 'Y'" .format(tablename))
        cur.execute(sql)
        fetchdata=cur.fetchall()         # fetches all the rows from the database which satisfies the given condition
        response=jsonify(fetchdata)      # converting the result to a format accepted by flask for return
        cur.close()
        return response
    except MySQLdb.Error as err:
        print(err)
        return str(err)
@app.route('/select/hidden/<string:tablename>')
def select_hidden(tablename):
    ''' To display the data whenever a table is selected - only passive rows will be displayed'''
    cur = mysql.connection.cursor()
    sql = ("SELECT * FROM {} where ACTIVE_FLAG = 'N'" .format(tablename))
    cur.execute(sql)
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    cur.close()
    return response

@app.route('/update/<string:tablename>', methods = ["POST", "GET"])
def update(tablename):
    '''To update the changes made in the table '''
    if request.method == "POST":
        receivedData = request.json             # gets the posted data in the form of json object
        #print(receivedData)
        x = list(receivedData.values())         # the values from the json object are stored in a list
        cur = mysql.connection.cursor()
        query = ("SELECT * FROM {}" .format(tablename))
        cur.execute(query)
        fetchdata = cur.fetchall()
        colName = list(fetchdata[0].keys())     # to get the column names alone
        actualLength = len(colName)             #length of single row of the table (or) no. of columns in a table
        dataLength = len(x[0])                  # length of number of values posted from the frontend - in order to verify the number of rows to be updated
        n = dataLength/actualLength             # the lengths are compared on order to perform update of multiple rows
        updateList = x[0][::actualLength]
        col = colName*int(n)
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        ind, count = 0, 0
        for i in (range(1, (dataLength))): 
            count+=1
            if count%actualLength == 0:  
                ind+=1   
            if col[i] != col[0]:              
                sql = "update {} set {} = %s where {} = %s" .format(tablename, col[i], col[0])
                print(sql, [x[0][i], updateList[ind]])
                cur.execute(sql, [x[0][i], updateList[ind]])                             
        mysql.connection.commit()
        cur.close()
    return "True"

@app.route('/s_delete/<string:tablename>', methods=["POST", "GET"])
def s_delete(tablename):
    ''' To do soft deletion on the rows selected in the table - a flag is set to indicate that the row is inactive '''
    if request.method == 'POST':
        receivedData = request.json
        x = list(receivedData.values())
        cur = mysql.connection.cursor()
        query = ("SELECT * FROM {}" .format(tablename))
        cur.execute(query)
        fetchdata = cur.fetchall()
        colName = list(fetchdata[0].keys())
        actualLength = len(colName)
        dataLength = len(x[0])
        print(actualLength, dataLength)
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        for i in range(0, dataLength, actualLength):
            sql = ("update {} set ACTIVE_FLAG = 'N', {} = curdate() where {} = %s ;" .format(tablename, colName[actualLength-1],  colName[0]))
            cur.execute(sql, [ x[0][i]])
        mysql.connection.commit()
        cur.close()
    return "True"

app.run(debug = True)