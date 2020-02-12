import cx_Oracle

conn_str = u'pankaj_kumar4/Radhey@12345@fgraci31-scan.qa.spratingsvpc.com:1521/rrdwqa.world'
conn = cx_Oracle.connect(conn_str)# Establish the connection between python programm and Oracle database by using connect() function.
c = conn.cursor() # Create a new object for executing the SQL statement.
c.execute(u'select * from aar2.base' )
col_names = [row[0] for row in c.description]
print(col_names)
list1=col_names
print(list1)
print(list1[0],list1[1])
for row in c:
     #print(row[0], "-", row[1])
   print (row)
conn.close