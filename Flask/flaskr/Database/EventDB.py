CreateEventTableText = """
    CREATE TABLE if not exists Event(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name varchar(255) NOT NULL,
        UniversityID int NOT NULL,
        CreatorID int NOT NULL,
        Description TEXT,
        StartTime time NOT NULL,
        EndTime time NOT NULL,
        Date date NOT NULL,
        CreationDate date NOT NULL,
        CreationTime time NOT NULL,
        Cost int,
        RoomNumber int,
        FOREIGN KEY (CreatorID) REFERENCES User(ID),
        FOREIGN KEY (UniversityID) REFERENCES University(ID)
    )
"""


class EventDB:
    #This is the actual name of the variables in the database table
    tableName = "Event"
    dbID = "ID"
    dbUniversityID = "UniversityID"
    dbCreatorID = "CreatorID"
    dbDescription = "Description"
    dbStartTime = "StartTime"
    dbEndTime = "EndTime"
    dbDate = "Date"
    dbCreationDate = "CreationDate"
    dbCreationTime = "CreationTime"
    dbCost = "Cost"
    dbRoomNumber = "RoomNumber"
    
    def __init__(self):
        self.ID = None
        self.universityID = None
        self.creatorID = None
        self.description = None
        self.startTIme = None
        self.endTime = None
        self.date = None
        self.creationDate = None
        self.creationTime = None
        self.cost = None
        self.roomNumber = None

