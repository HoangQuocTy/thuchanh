import sympy as sp
import tkinter as tk

def calculate():
    x_str = entry_variable.get()
    f_str = function_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())

    x = sp.symbols(x_str)
    f = sp.sympify(f_str)
    f_prime = sp.diff(f, x)
    integral_result = sp.integrate(f, (x, a, b))

    result_label.config(text=f"Đạo hàm của f({x_str}) = {f_prime}")
    integral_label.config(text=f"Tích phân xác định của f({x_str}) từ {a} đến {b} = {integral_result}")

# Tạo cửa sổ
window = tk.Tk()
window.title("Calculator")

# Tạo các Label và Entry cho biến và hàm
variable_label = tk.Label(window, text="Biến (ví dụ: x):")
entry_variable = tk.Entry(window, width=30)  # Thay đổi kích thước 30

function_label = tk.Label(window, text="Hàm (ví dụ: x**2 + 2*x + 1):")
function_entry = tk.Entry(window, width=90)  # Thay đổi kích thước 30

a_label = tk.Label(window, text="a (điểm bắt đầu tích phân):")
a_entry = tk.Entry(window, width=30)  # Thay đổi kích thước 30

b_label = tk.Label(window, text="b (điểm kết thúc tích phân):")
b_entry = tk.Entry(window, width=30)  # Thay đổi kích thước 30

# Tạo nút tính toán
calculate_button = tk.Button(window, text="Tính", command=calculate)

# Tạo các Label để hiển thị kết quả
result_label = tk.Label(window, text="")
integral_label = tk.Label(window, text="")

# Định vị các phần tử trên giao diện
variable_label.pack()
entry_variable.pack()
function_label.pack()
function_entry.pack()
a_label.pack()
a_entry.pack()
b_label.pack()
b_entry.pack()
calculate_button.pack()
result_label.pack()
integral_label.pack()

# Khởi chạy giao diện
window.mainloop()
