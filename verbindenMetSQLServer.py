import pyodbc  # kan gebeuren dat je :::>>   pip install pyodbc            moet doen

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-56ORDB6;'    # jouw servernaam
                      'Database=abc;'               # jouw databasenaam
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute("SELECT * FROM Shuttles")  # jouw query
for i in cursor:
    print(i)

print("einde")
