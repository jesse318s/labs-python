import pyodbc

server='3.130.26.194'
database='itse2359sp21'
username='jsitessp212359'
password='ab2VcLLhL!'

con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};SERVER='+server+
                     ';DATABASE='+database+';UID='+username+';PWD='+password)
cursor=con.cursor()
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE 'm%'")
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term = 'hardware'")
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE '%s%'")
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE '%ware%'")
query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE '%t'")

results = cursor.fetchall()
for result in results:
    print(result)
