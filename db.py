import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE admin (adminId TEXT PRIMARY KEY, password TEXT UNIQUE NOT NULL)')
conn.execute('CREATE TABLE asset (assetId TEXT PRIMARY KEY, assetName TEXT NOT NULL)')
conn.execute('CREATE TABLE task (taskId TEXT PRIMARY KEY, taskName TEXT NOT NULL, frequency TEXT NOT NULL)')
conn.execute('CREATE TABLE worker (workerId TEXT PRIMARY KEY, workerName TEXT UNIQUE NOT NULL)')
conn.execute('CREATE TABLE payload (assetId TEXT NOT NULL,taskId TEXT NOT NULL,workerId TEXT NOT NULL,timeOfAllocation DATE NOT NULL,taskToBePerformedBy TEXT NOT NULL,FOREIGN KEY (assetId) REFERENCES asset (assetId),FOREIGN KEY (taskId) REFERENCES task (taskId), FOREIGN KEY (workerId) REFERENCES worker (workerId))')
conn.close()