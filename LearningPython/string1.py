str = 'Hello world,Hello Hoi'

print (str[0:3])
print (str[6:-3])
print ("length(str) = ",len(str))

#thay the chuoi
newstr = str.replace('Hello', 'Bye')
print (newstr)

#tim chuoi con
ind = str.find("Hello")
print ("pos1 = ", ind)
ind = str.find("Hello",1, len(str))
print ("pos2 = ", ind)

#bo khoang trang dau va sau chuoi
str = '   cong hoa       '
print (str.strip())
#bo khoang trang phia dau
str = '   cong hoa       '
print (str.lstrip())
#bo khoang trang phia sau
str = '   cong hoa       '
print (str.rstrip())