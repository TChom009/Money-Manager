# basicsqlite3.py

import sqlite3 

# สร้าง database
conn = sqlite3.connect('expense.sqlite3')
# สร้างตัวดำเนินการ (อยากได้อะไรใช้ตัวนี้ได้เลย)
c = conn.cursor()

# สร้างtable ด้วยภาษา SQL
'''
'Transection ID(transaction) TEXT',
'Date-Time(datetime)' TEXT,
'List'(title) TEXT,
'Price(expense) REAL (float)',
'Quantity(quantity)' INTEGER,
'Total(total) REAL'
'''
c.execute("""CREATE TABLE IF NOT EXISTS expenselist (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				transactionid TEXT,
				datetime TEXT,
				title TEXT,
				expense REAL,
				quantity INTEGER,
				total REAL
			)""")

def insert_expense(transectionid,datetime,title,expense,quantity,total):
	ID = None
	with conn: #คำสั่ง close database โดยอัตโนมัติ
		c.execute("""INSERT INTO expenselist VALUES (?,?,?,?,?,?,?)""",
			(ID,transectionid,datetime,title,expense,quantity,total))
		conn.commit() #การบันทึกข้อมูลลงในฐานข้อมูล ถ้าไม่รันตัวนี้จะไม่บันทึก หรือเรียกว่าคำสั่งsaveนั่นเอง
		print('Insert Success!')
  
def show_expense():
	with conn:
		c.execute("SELECT * FROM expenselist")
		expense = c.fetchall() # คำสั่งให้ดึงข้อมูลเข้ามา
		print(expense)

	return expense

def update_expense(transectionid,title,expense,quantity,total):
	with conn:
		c.execute("""UPDATE expenselist SET title=?, expense=?, quantity=?, total=? WHERE transactionid=?""",
			([title,expense,quantity,total,transectionid]))
	conn.commit()
	print('Data Updated!')

# def delete_expense(transectionid):
# 	with conn:
# 		c.execute("DELETE FROM expenselist WHERE transactionid=?",([transectionid]))
# 	conn.commit()
# 	print('Data has been deleted successfully')

# insert_expense('49374994902','Saturday 2021-08-01','Hotel',5000,7,35000)
# update_expense('49374994395','Brakfast',250,2,500)
# delete_expense('49374994396')
show_expense()




print('Success!')



