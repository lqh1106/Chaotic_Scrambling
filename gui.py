import tkinter as tk
import pyperclip
import scrambling

def calculate_result():
	# 获取输入值
	message = message_entry.get()
	way = way_var.get()
	key = float(key_entry.get())
	operation = operation_var.get()

	# 根据用户选择调用相应的函数
	if operation == "Encode":
		if way == "Logistic":
			result = scrambling.encode(message,0,key)
		elif way == "Circle":
			result = scrambling.encode(message,1,key)
		elif way == "Chebyshev":
			result = scrambling.encode(message,2,key)
		else:
			result = "Invalid way"
	elif operation == "Decode":
		if way == "Logistic":
			result = scrambling.decode(message, 0, key)
		elif way == "Circle":
			result = scrambling.decode(message, 1, key)
		elif way == "Chebyshev":
			result = scrambling.decode(message, 2, key)
		else:
			result = "Invalid way"
	else:
		result = "Invalid operation"

	# 将结果复制到剪切板
	pyperclip.copy(result)

	# 更新结果标签
	result_label.config(text=f"Result: {result} (Copied to clipboard)")


# 创建主窗口
root = tk.Tk()
root.title("Message Encoder/Decoder")

# 创建输入框和标签
message_label = tk.Label(root, text="Message:")
message_label.grid(row=0, column=0, padx=5, pady=5)
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

way_label = tk.Label(root, text="Way:")
way_label.grid(row=1, column=0, padx=5, pady=5)
way_var = tk.StringVar(root)
way_var.set("Logistic")  # 默认选择Logistic
way_radios = [("Logistic", "Logistic"), ("Circle", "Circle"), ("Chebyshev", "Chebyshev")]
for i, (text, value) in enumerate(way_radios):
	tk.Radiobutton(root, text=text, variable=way_var, value=value).grid(row=1, column=i + 1, padx=5, pady=5)

key_label = tk.Label(root, text="Key:")
key_label.grid(row=2, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=3, column=0, padx=5, pady=5)
operation_var = tk.StringVar(root)
operation_var.set("Encode")  # 默认选择Encode
operation_radios = [("Encode", "Encode"), ("Decode", "Decode")]
for i, (text, value) in enumerate(operation_radios):
	tk.Radiobutton(root, text=text, variable=operation_var, value=value).grid(row=3, column=i + 1, padx=5, pady=5)

# 创建计算按钮
calculate_button = tk.Button(root, text="Calculate", command=calculate_result)
calculate_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# 创建结果标签
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
