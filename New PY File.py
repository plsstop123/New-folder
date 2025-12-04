x = float(input("Nhap so thu nhat:"))
y = float(input("Nhap so thu hai:"))
def multiply(x, y) :
  """Function calculate multiply of 2 numbers"""
  return x * y

# Gọi hàm sử dụng và truyền tham số
mul = multiply(x, y)

# In kết quả => 40
print(mul)
