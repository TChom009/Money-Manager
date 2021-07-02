# GUIBasic2-Expense.py

from tkinter import*
from tkinter import ttk, messagebox  # ttk คือthemeของ Tk
import csv
from datetime import datetime # ttk is theme of Tk
# command+B สั่งให้ run program 

GUI = Tk() # สร้าง GUI ขึ้นแล้วดึงฟังก์ชันของ Tk() T capital, k lowercap
GUI.title('Daily Budget & Expense Tracker by Bluvoyage')
GUI.geometry('900x800+250+200') # กำหนดขนาดของหน้าต่าง

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50, ipady=20)
# .pack() คือคำสั่งติดปุ่มเข้ากับ GUI หลัก, ipadx,ipady คือการกำหนดระยะแกนx,y ของปุ่ม
# .place(x,y) คือคำสั่งเอาปุ่มไปวางตามlocationที่เราต้องการ

#############MENU####################
menubar = Menu(GUI)
GUI.config(menu=menubar) # สร้าง menubar ติดกับ GUI

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import Photo')
filemenu.add_command(label='Export to Googlesheet')

# Help
def About():
	print('About Menu')
	messagebox.showinfo('About','Take Control of Your Money\nLets Track!')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')

# Donation
def Donate():
	messagebox.showinfo('Donation','Helping Homeless Pets\nVolunteer or Donate Pet Food & Supplies', 'Bank Account: 999-99999-99\nPomtpay 080-9999-9999')
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donation',menu=donatemenu)


####################################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab) 
T2 = Frame(Tab)
#T1 = Frame(Tab,width=400,height=400)
#T2 = Frame(Tab,width=400)
Tab.pack(fill=BOTH, expand=50)

icon_t1 = PhotoImage(file='t1_expense.png')
icon_t2 = PhotoImage(file='t2_expense.png')


Tab.add(T1, text=f'{"Add Expense":^{20}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"Total Expense":^{20}}',image=icon_t2,compound='top')

F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'Monday',
		'Tue':'Tueday',
		'Wed':'Wednesday',
		'Thu':'Thursday',
		'Fri':'Friday',
		'Sat':'Saturday',
		'Sun':'Sunday'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()


	if expense == '':
		print('No Data')
		messagebox.showwarning('Error','Do not leave "List of Expense" blank. Please input your data.')
		return
	elif price == '':
		print('No Data')
		messagebox.showwarning('Error','Do not leave "Price" blank. Please input your data.')
		return
	elif quantity == '':
		# หรือ quantity = 1 คือการตั้งค่า default ให้ quantity เท่ากับ 1 โดยอัตโนมัติ 
		print('No Data')
		messagebox.showwarning('Error','Do not leave "Quantity" blank. Please input your data.')
		return


	try: # คือฟังก์ชันหาจุด error
		total = float(price) * float(quantity)
		# total = int(price) * int(quantity) คูณเลขเต็มจำนวณ ไม่มีทศนิยม
		# total = float(price) * float(quantity) ถ้าต้องการคูณทศนิยม
		# .get() คือดึงค่ามาจาก v_expense = StringVar()
		print('List of Expense: {} price: {}'.format(expense,price))
		print('Number: {} Total: {} THB'.format(quantity,total))
		text = 'List of Expense: price:{}\n'.format(expense,price)
		text = text + 'Quantity: {} Total: {} THB'.format(quantity,total)
		v_result.set(text)
		# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		# .set คือการดึง

		# บันทึกข้อมูล csv อย่าลืม import csv
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		print(today)
		stamp = datetime.now()
		dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
		transectionid = stamp.strftime('%Y%m%d%H%M%f')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with คือคำสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) # สร้างฟังก์ชันสำหรับเขียนข้อมูล
			data = [transectionid,dt,expense,price,quantity,total]
			fw.writerow(data)

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		update_table() 
	except:
		print('ERROR')
		messagebox.showerror('Error','You have entered an invalid number. Please try again.')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#messagebox.showwanring('Error','You have entered an invalid number. Please try again.')
		#messagebox.showeinfo('Error','You have entered an invalid number. Please try again.')

	
# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = ('Adobe Gurmukhi',20) # คำสั่งประกาศ font
# None เปลี่ยนเป็นฟร้อนตาม MS word ได้เลย

#---------image------------
main_icon = PhotoImage(file='icon_map.png')

mainicon = Label(F1,image=main_icon)
mainicon.pack()


#----------text1-----------
L = Label(F1,text='List of Expenses',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลในGUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#--------------------------

#----------text2-----------
L = Label(F1,text='Price (THB)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลในGUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------------

#----------text3----------
L = Label(F1,text='Quantity',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลในGUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------------

icon_b1 = PhotoImage(file='b_save.png')

B2 = ttk.Button(F1,text='Save', image=icon_b1, compound='left',command=Save)
B2.pack(ipadx=5, ipady=5, pady=15)

v_result = StringVar()
v_result.set('-----------Result----------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='blue')
# esult = ttk.Label(F1, textvariable=v_result,front=FONT1,fg='blue')
result.pack(pady=20)


###########TAB2#############

# ตัวอย่าง & concept
# rs = [] เป็นglobal
# def read_csv():
	# global rs
	# with open('savedata.csv',newline='',encoding='utf-8') as f:
		# fr = csv.reader(f)
		# data = list(fr)
		#rs = data
		#print(rs)
	# return data
		# print(data)
		# print('------')
		# print(data[0][0])
		# for a,b,c,d,e in data:
			# print(b)
#rs = read_csv()
#print(rs)

#read_csv()

	# old method
	# f = open('savedata.csv',newline='',encoding='utf-8')
	# fr = csv.reader(f)
	# f.close()

def read_csv(): #ฟังก์ชันอ่านข้อมูล
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data

# table

L = ttk.Label(T2,text='Overview',font=FONT1).pack(pady=20)

header = ['Transection ID','Date-Time','List','Price','Quantity','Total']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=20)
resulttable.pack()

# การ run for loop วิธีที่ 1
# for i in range(len(header)):
	#resulttable.heading(header[i],text=header[i])

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [175,230,120,90,70,90] #การปรับความกว้างของแต่ละ column
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)
	
# การ insert data manual ครั้งละ  1 ชิ้น
# resulttable.insert('',0,value=['Mon','Food',30,5,150])
# ฟังก์ชัน 0 คือการใส่ข้อมูลอันดับแรก/บรรทัดแรก
# resulttable.insert('','end',value=['Tue','Beaverage',30,5,150]) 
# ฟังก์ชัน end คือการใส่ข้อมูลด้านล่างสุด

alltransection = {}

def UpdateCSV():
	with open('savedata.csv','w',newline='',encoding='utf-8') as f: # เพิ่ม w เพื่อสั่งให้เขียนทับ
		fw = csv.writer(f)# เตรียมข้อมูลให้กลายเป็น list
		data = list(alltransection.values())
		fw.writerows(data) # การเขียนแบบ multiple line from nested list บรรทัดซ้อนบรรทัด [[],[],[]]
		print('Table was updated')
		update_table() # เพื่อให้ข้อมูลในตารางหายไป เวลากดปุ่ม delete  

def DeleteRecord(event=None):
	check = messagebox.askyesno('Confirm?','Do you want to delete this data?')
	print('YES/NO:',check) # ฟังก์ชันยืนยันก่อนทำการลบ

	if check == True:
		print('delete')
		select = resulttable.selection()
		# print(select)
		data = resulttable.item(select)
		data = data['values']
		transectionid = data[0]
		# print(transectionid)
		# print(type(transectionid))
		del alltransection[str(transectionid)] # delete data in dict
		# print(alltransection)
		UpdateCSV()
		update_table()

	else:
		print('cancel')

BDelete = ttk.Button(T2,text='Delete',command=DeleteRecord)
BDelete.place(x=50,y=520)

resulttable.bind('<Delete>',DeleteRecord) 

# การ insert data ทีละ  1 ชุด  
def update_table():
	resulttable.delete(*resulttable.get_children()) # * คือการสั้ง delete อัตโนมัติ
	# for c in resulttable.get_children():
	# 	resulttable.heading(header[i],text-header[i])
	try: # ฟังก์ชันดักจับ error เวลาไม่มีข้อมูล เพื่อให้ program มัน run ได้
		data = read_csv()
		for d in data:
			# creat transection data
			alltransection[d[0]] = d # d[0]=transectionid
			resulttable.insert('',0,value=d)
		print(alltransection)
	except: # ฟังก์ชันดักจับ error เวลาไม่มีข้อมูล เพื่อให้ program มัน run ได้
		print('No Data')

#resulttable.column('Date-Time',width=10)
#การใส่colum
# resulttable.heading(header[0],text=header[0])
# resulttable.heading(header[1],text=header[1])
# resulttable.heading(header[2],text=header[2])
# resulttable.heading(header[3],text=header[3])
# resulttable.heading(header[4],text=header[4])

update_table()
print('GET CHILD:',resulttable.get_children())
GUI.bind('<Tab>', lambda x: E2.focus())
GUI.mainloop() # เพื่อให้โปรแกรม run ตลอดเวลา

