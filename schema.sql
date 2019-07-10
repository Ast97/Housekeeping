DROP TABLE IF EXISTS asset;

CREATE TABLE asset (
  assetId TEXT PRIMARY KEY,
  assetName TEXT UNIQUE NOT NULL
);

CREATE TABLE task (
  taskId TEXT PRIMARY KEY,
  taskName TEXT UNIQUE NOT NULL
);

CREATE TABLE worker (
  workerId TEXT PRIMARY KEYT,
  workerName TEXT UNIQUE NOT NULL
);

CREATE TABLE payload(
  assetId TEXT NOT NULL,
  taskId TEXT NOT NULL,
  workerId TEXT NOT NULL,
  timeOfAllocation DATE NOT NULL,
  taskToBePerformedBy TEXT NOT NULL,
  FOREIGN KEY (assetId) REFERENCES asset (assetId),
  FOREIGN KEY (taskId) REFERENCES task (taskId),
  FOREIGN KEY (workerId) REFERENCES worker (workerId)
);
