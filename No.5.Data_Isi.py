import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tugas_uas"
)

cursor = db.cursor()
sql = "INSERT INTO peserta (name, address) VALUES (%s, %s)"
values = [
  ("Ardy", "Tangerang"),
  ("Vira", "Jakarta"),
  ("Haydar", "Ciamis"),
  ("Retno", "Medan")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))
