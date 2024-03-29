import tkinter as tk

# ============ Global Variables ============

range_prefix = tk.StringVar(None, "")
range_suffix = tk.StringVar(None, "")
range_start = tk.StringVar(None, "")
range_end = tk.StringVar(None, "")
printer_select = tk.StringVar(None, "LPT1")
local_print = tk.StringVar(None, "127.0.0.1")
tag_select = tk.IntVar(value=0)
asset_type = tk.StringVar(None, "Asset Tag :")
cust_quantity = tk.IntVar(None, "1")
auto_1 = tk.StringVar(None)
auto_2 = tk.StringVar(None)
device_label = tk.StringVar(None, "Device")
bg_col = str("white")
xyz = str(" ")
flag_1 = int(0)
flag_2 = str("0")
range_image = ""
qr_pos = 325 # default QR code position on the X axis
qr_mag = 2 # default QR magnification. range is 1-10
pCounter = 0
x_col = 0
y_row = 0
textmod = tk.IntVar(None, "0")
bentry1 = tk.StringVar(None)
bentry2 = tk.StringVar(None)
label_mod = tk.IntVar(None, "0") # manually set modifier to alter height that label is printed at to account for inaccurate calibration of printer
horz_label_mod = tk.IntVar(None, "0")
no_bc = tk.BooleanVar(None)
screen_row = 2
soc_row = 2
kvs_row = 2
group_row = 2
dom_row = 2
dom_col = 0
btnRow = 0
btnCol = 0
receiptCount = 0
officeCount = 0

# ============ Printer Initial Selection ============

host = str(printer_select.get())
port = 9100