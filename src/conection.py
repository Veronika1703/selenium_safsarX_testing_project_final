import pyodbc
connection_string=(
    "DRIVER={SQL Server};"
    "PORT=1433;"
    "SERVER=VERONIKA-PC;"
    "DATABASE=NORTHWND;"
    "Trusted_Connection=yes;")
connection = pyodbc.connect(connection_string)
my_cursur=connection.cursor()
my_cursur.execute("select * from customers")
result=my_cursur.fetchall()
for i in result:
    print(i)