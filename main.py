## Import libs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import random

## Declare variables & voucher
res = []
Vouchers = []

def process_output(op, voucher):
	if 'hết lượt' or 'Xin  lỗi' in op:
		return 'Hết lượt'
	else:
		if '40k' in voucher:
			return '40/200'
		elif '50k' in voucher:
			return '50/250'
		elif '60k' in voucher:
			return '60/300' 

def copy_to_clipboard(content):
    # Sao chép nội dung của Entry widget vào clipboard
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()  

def load_voucher_init():
	for index, voucher in enumerate(Vouchers):
		Label(canvas_frame, font=('Cambria', 12), text=index + 1, width=5).grid(row=index, column=0)
		Label(canvas_frame, font=('Cambria', 12), text=Vouchers[index], width=35).grid(row=index, column=1)
		Label(canvas_frame, font=('Cambria', 12), text='(Trống)', width=20).grid(row=index, column=2)
		tk.Button(canvas_frame, font=('Cambria', 12), text='Sao chép', width=10, command=lambda v=Vouchers[index]: copy_to_clipboard(v)).grid(row=index, column=3)

def check_vouchers():
	res = []
	## Check vouchers
	for voucher in Vouchers:
		voucherInput.send_keys(voucher)
		voucherBtn.click()
		voucherRes = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CLASS_NAME, 'voucher-input-message'))
	    )
		res.append(process_output(voucherRes.text, voucher))
		voucherInput.send_keys(Keys.CONTROL + "a")
		voucherInput.send_keys(Keys.DELETE)
		time.sleep(random.randint(100, 150)/100)

	## Show result
	for index, r in enumerate(res):
		Label(canvas_frame, text=r, font=('Cambria', 12), width=20).grid(row=index, column=2)

def delete_res_table():
    # Xóa tất cả các widget con trong frame
     res_table.delete(0, END)

def get_vouchers():
	vs = v.get()
	entry_vouchers.delete(0, tk.END)
	voucher = ''
	for c in vs:
		if c != ' ':
			voucher += c
		else:
			Vouchers.insert(0, voucher)
			voucher = ''
	Vouchers.insert(0, voucher)
	delete_res_table()
	load_voucher_init()

def disconnect_to_browser():
	driver.quit()
	root.destroy()

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
## Select input field of voucher
voucherInput = driver.find_element(By.ID, 'automation-voucher-input')
voucherBtn = driver.find_element(By.ID, 'automation-voucher-input-button')
time.sleep(0.5)
voucherInput.send_keys(Keys.CONTROL + 'a')
voucherInput.send_keys(Keys.DELETE)

## Create UI
root = tk.Tk()
root.configure()
root.protocol("WM_DELETE_WINDOW", disconnect_to_browser)

v = tk.StringVar()
root.title('Check voucher')
Label(root, text='Danh sách các mã hiện tại', font=('Cambria', 14, 'bold')).grid(row=0, column=0, pady=5, sticky='nsew')

# Frame containing the header
header = tk.Frame(root)
header.grid(row=1, columnspan=6)
Label(header, text='STT', font=('Cambria', 12), width=5).grid(row=0, column=0)
Label(header, text='Mã giảm giá', font=('Cambria', 12), width=35).grid(row=0, column=1)
Label(header, text='Kết quả', font=('Cambria', 12), width=20).grid(row=0, column=2)
Label(header, text='', font=('Cambria', 12), width=10).grid(row=0, column=3)

# Frame containing Listbox and Scrollbar
listbox_frame = tk.Frame(root, width=640, height=360)
listbox_frame.grid(row=2, column=0, columnspan=4, sticky='nsew')

# Listbox with a fixed height (in number of rows) and width (in characters)
res_table = Canvas(listbox_frame, width=640, bg='lightgray', height=380)  # height=10 specifies the number of visible rows
res_table.grid(row=0, column=0, sticky='ew')

# Scrollbar for the Listbox
scrollbar_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=res_table.yview)
scrollbar_y.grid(row=2, column=4, sticky='ns')

# Connect the Listbox and Scrollbar
res_table.config(yscrollcommand=scrollbar_y.set)

# Make sure the listbox_frame does not expand beyond the specified size
listbox_frame.grid_propagate(False)

canvas_frame = tk.Frame(res_table)
canvas_frame.grid(row=0, columnspan=4, sticky='nsew')

# Create a window on the res_table to contain the frame
res_table.create_window((0, 0), window=canvas_frame, anchor="nw")

def on_res_table_configure(event):
    res_table.config(scrollregion=res_table.bbox("all"))

canvas_frame.bind("<Configure>", on_res_table_configure)

# Load initial vouchers
load_voucher_init()

Label(root, text='Nhập các mã tại đây', font=('Cambria', 12)).grid(row=3, column=0, pady=5)
entry_vouchers = tk.Entry(root, textvariable=v, width=40, font=('Cambria', 12))
entry_vouchers.grid(row=3, column=1, pady=5)
Button(root, text="Thêm", font=('Cambria', 12), command=get_vouchers).grid(row=3, column=2, pady=5)

Button(root, text='LÀM MỚI', bg='#17c124', fg='white', font=('Cambria', 12,'bold'), command=check_vouchers).grid(row=4, column=0, pady=5)
Button(root, text='KIỂM TRA MÃ', bg='#c13217', fg='white', font=('Cambria', 12, 'bold'), command=check_vouchers).grid(row=4, column=1, pady=5)

root.minsize(height=520, width=680)
root.maxsize(height=520, width=680)

root.mainloop()
