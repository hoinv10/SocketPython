def plus(a,b):
    return a+b
    
# có thể gán giá trị trước, khi gọi hàm không cần đặt tham số b
def fn(a, b = 10):
    print ("a=",a)
    return a+b

def main():
    print (plus(1,2))
    print (fn(b=3,a=4)) # có thể đổi chỗ tham số truyền vào

main()