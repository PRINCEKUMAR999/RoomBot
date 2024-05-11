import mysql.connector
from telegram.ext import ConversationHandler

# Establish a connection to MySQL
def GetData():
    connection = mysql.connector.connect(
    host="greenbook.mysql.pythonanywhere-services.com",
    user="greenbook",
    password="@green852",
    database="roomfinder")

# Create a cursor object to interact with the database
    cursor = connection.cursor()
    return cursor,connection

# name = "ram"
# chatid = "ram45"
# mobile = "7878877"
# Prepare SQL query to insert data into the table
def NEWUSER(name,mobile,chatid):
    cursor,connection = GetData()
    sql_query = "INSERT INTO userlogin (chatid, full_name, mobile) VALUES (%s, %s, %s)"

# Sample user data
    # chatid = "john_doe"
    # full_name = "John Doe"
    # mobile = "1234567890"

# Execute the SQL query
    try:
        cursor.execute(sql_query, (chatid, name,mobile))
        connection.commit()
        cursor.close()
        connection.close()
        return(print("data added successfully"),"Data updated.")
    except Exception as error:
        print("data insertion failed")
        print(error)
        return(print("data is failed"),error)

# Commit changes to the database
    


def USERUPDATE(newname,newmobile,newchatid):
    cursor,connection = GetData()
    sql_query = "UPDATE userlogin SET full_name = %s, mobile = %s WHERE chatid = %s"

# New user data
    # new_full_name = "John Updated Doe"
    # new_mobile = "9876543210"
    # chatid = "john_doe"

# Execute the SQL query
    try:
        cursor.execute(sql_query, (newname,newmobile,newchatid))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return(print("data rooms found"),1,results)
    except mysql.connector.Error as error:
        print("data insertion failed")
        return(print("data is failed"),0,error)


# Commit changes to the database
    


def CHECKUSER(chatid):
    cursor,connection = GetData()
    sql_query = "SELECT * FROM userlogin WHERE chatid = %s;"

# New user data
    # new_full_name = "John Updated Doe"
    # new_mobile = "9876543210"
    # chatid = "john_doe"

# Execute the SQL query
    try:
        cursor.execute(sql_query,[chatid])
        print("reached here")
        userdata = cursor.fetchall()
        print(len(userdata))
        connection.commit()
        cursor.close()
        connection.close()
        return(2,"Data Already Exist.",len(userdata))
    except mysql.connector.Error as error:
        print("data found failed",error)
        return(1,error)


# Commit changes to the database

def NEWROOM(username,address,address1,roomtype,inverter,purewater,wifi,localaddress,mobile,whocanlive,rent):
    cursor,connection = GetData()
    sql_query = "INSERT INTO your_table_name (username,address,address1,roomtype,inverter,purewater,wifi,localaddress,mobile,whocanlive,rent) VALUES (%s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
    
    try:
        cursor.execute(sql_query, (username,address,address1,roomtype,inverter,purewater,wifi,localaddress,mobile,whocanlive,rent))
        connection.commit()
        cursor.close()
        connection.close()
        ConversationHandler.END
        return(0,print("Room data added successfully"),"Data updated.")
    except Exception as error:
        print("data insertion failed")
        print(error)
        ConversationHandler.END
        return(1,print("data is failed"),error)


def SEARCHROOM(LAT,LOG,LINIT,OFFS):
    cursor,connection = GetData()
    sql_query = '''
SELECT *,( 6371 * acos(
           cos( radians(%s) )
           * cos( radians(address) )
           * cos( radians(address1) - radians(%s) )
           + sin( radians(%s) )
           * sin( radians(address) )
       ) ) AS distance_km
FROM your_table_name
HAVING distance_km <= 10 order by distance_km LIMIT %s OFFSET %s;     
    '''
    
    try:
        cursor.execute(sql_query, (LAT,LOG,LAT,LINIT,OFFS))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        print(results)
        return(0,print("Room data added successfully"),"Data updated.",results)
    except Exception as error:
        print("data fetch failed")
        print(error)
        return(1,print("data is failed"),error)

    

# Close cursor and connection
