# importing module
import cx_Oracle
global cursor

# Create a table in Oracle database
try:

    con = cx_Oracle.connect('pankaj_kumar4/Service123@fgraci31-scan.qa.spratingsvpc.com:1521/rrdwqa.world')

    # Now execute the sqlquery
    cursor = con.cursor()

    # Creating a table srollno heading which is number
    cursor.execute("select * from AAR2.base")

    print("Table Created successful")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
       cursor.close()
    if con:
     con.close()
      # print("This is finally ")
