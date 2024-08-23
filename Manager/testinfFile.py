import sqlite3  
  
conn = sqlite3.connect('./Storage/storeManagementSystem.db')  

print ("Opened database successfully")


conn.execute("INSERT INTO productsData(SKU, name, brand, quantity) \
VALUES('s001', 'bike','hero', 12)")

print("Recoed cratred")
conn.close()