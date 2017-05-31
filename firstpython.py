import MySQLdb
import MySQLdb.cursors as cursors

db = MySQLdb.connect("localhost","root","admin","recommendations",cursorclass=cursors.SSDictCursor)

cursor = db.cursor()
cursor.execute('select * from  places')

data = cursor.fetchall()

print (data)




        


        
    
