import mysql.connector
import CreateTable

def getConnection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root"
    )
    return mydb

def createQueryBuilder():
    object = {
        "user" : """INSERT INTO User VALUES (%s, %s, %s)""",
        "blog" : """INSERT INTO Blog VALUES (%s, %s, %s, %s, %s, %s)""",
        "comment" : """INSERT INTO Comment VALUES (%s, %s, %s, %s, %s)""",
        "tag" : """INSERT INTO Tag VALUES (%s, %s)""",
        "tagmap" : """INSERT INTO TagMap VALUES (%s, %s)"""
    }
    return object

def insertIntoTable(queryObj,table,values):
    myconn = getConnection()
    mycurr = myconn.cursor()
    mycurr.execute("USE Test")
    insert_sql = queryObj[table]
    try:
        mycurr.execute(insert_sql,values)
    except mysql.connector.Error as error:
        print(values,error)
    myconn.commit()
    myconn.close()

def populate():
    CreateTable.create()
    queryObj = createQueryBuilder()
    # User insert
    value = (1,"Anupam1","anupam")
    insertIntoTable(queryObj,"user",value)
    value = (2,"Anupam2","anupam")
    insertIntoTable(queryObj,"user",value)
    # Blog insert
    value = (1,"Anupam_first","agghghgh",1,1,0)
    insertIntoTable(queryObj,"blog",value)
    value = (2,"Anupam_second","khkjhhkh",1,0,1)
    insertIntoTable(queryObj,"blog",value)
    value = (1,"Anupam_new","hjfkjshh",2,0,0)
    insertIntoTable(queryObj,"blog",value)
    value = (3,"Anupam_second","khkjhhkh",11,0,1)
    insertIntoTable(queryObj,"blog",value)
    value = (None,"Anupam_new","hjfkjshh",2,0,0)
    insertIntoTable(queryObj,"blog",value)
    # Comment Insert
    value = (1,"review1",1,1,1)
    insertIntoTable(queryObj,"comment",value)
    value = (2,"review2",1,0,2)
    insertIntoTable(queryObj,"comment",value)
    value = (3,"review3",1,0,3)
    insertIntoTable(queryObj,"comment",value)
    # Tag Insert
    value = (1,"CS")
    insertIntoTable(queryObj,"tag",value)
    value = (2,"DDS")
    insertIntoTable(queryObj,"tag",value)
    value = (3,"ML")
    insertIntoTable(queryObj,"tag",value)
     # Tag Map Insert
    value = (1,1)
    insertIntoTable(queryObj,"tagmap",value)
    value = (2,2)
    insertIntoTable(queryObj,"tagmap",value)
    value = (3,3)
    insertIntoTable(queryObj,"tagmap",value)

populate()