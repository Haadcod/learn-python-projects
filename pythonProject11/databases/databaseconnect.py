#import the required libraries
import mysql.connector
dataBase=mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password"
)
print(dataBase)
#disconnecting from the server
dataBase.close()
