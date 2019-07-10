from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('addAsset.html')

@app.route('/add-asset')
def new_asset():
   return render_template('addAsset.html')

@app.route('/addasset',methods = ['POST', 'GET'])
def addasset():
   msg=None
   if request.method == 'POST':
      try:
         assetId = request.form['assetId']
         assetName = request.form['assetName']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO asset (assetId,assetName) VALUES (?,?)",(assetId,assetName) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("results.html",msg = msg)
         con.close()

@app.route('/assets/all')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from asset")
   
   rows = cur.fetchall();
   return render_template("assetList.html",rows = rows)

@app.route('/add-task')
def new_task():
   return render_template('addTask.html')

@app.route('/addtask',methods = ['POST', 'GET'])
def addtask():
   msg=None
   if request.method == 'POST':
      try:
         taskId = request.form['taskId']
         taskName = request.form['taskName']
         frequency = request.form['frequency']
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO task (taskId,taskName,frequency) VALUES (?,?,?)",(taskId,taskName,frequency) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("results.html",msg = msg)
         con.close()

@app.route('/add-worker')
def new_worker():
   return render_template('addWorker.html')

@app.route('/addworker',methods = ['POST', 'GET'])
def addworker():
   msg=None
   if request.method == 'POST':
      try:
         workerId = request.form['workerId']
         workerName = request.form['workerName']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO worker (workerId,workerName) VALUES (?,?)",(workerId,workerName) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("results.html",msg = msg)
         con.close()

@app.route('/allocate-task')
def alloc_task():
   return render_template('payload.html')

@app.route('/alloc',methods = ['POST', 'GET'])
def alloc():
   msg=None
   if request.method == 'POST':
      try:
         assetId = request.form['assetId']
         taskId = request.form['taskId']
         workerId = request.form['workerId']
         timeOfAllocation = request.form['timeOfAllocation']
         taskToBePerformedBy = request.form['taskToBePerformedBy']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO payload (assetId,taskId,workerId,timeOfAllocation,taskToBePerformedBy) VALUES (?,?,?,?,?)",(assetId,taskId,workerId,timeOfAllocation,taskToBePerformedBy))
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("results.html",msg = msg)
         con.close()

@app.route('/get-tasks-for-workers/<workerId>')
def getTasksList(workerId):
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   print(workerId)
   cur = con.cursor()
   cur.execute("select task.taskId,taskName,frequency from (payload INNER JOIN task ON payload.taskId=task.taskId) where payload.workerId=?",(workerId,))
   rows = cur.fetchall();
   return render_template("taskList.html",rows=rows)

if __name__ == '__main__':
   app.run(debug = True)