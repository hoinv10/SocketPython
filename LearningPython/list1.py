#list la mang trong C/C++

ln = [1,2,3,4]
ls = ["hung", "hoi", "duong","Vu", "nhom"]

#simple call
print ("ln[0] =", ln[0])
print ("ls[1] =", ls[1])
print ("len ls = ", len(ls))

#pass error
index = 5;
try:
	ln[index] == 1 
except	IndexError:
	print (index)

# cong hai mang
print (ln + ls)

#them phan tu vao mang
ln.append(5)
print(ln)

#lay phan tu cuoi cung cua mang
ln.pop()
ln.pop(0)
print (ln)

# tim index trong mang
ind = ls.index("hoi")
print("index = ", ind)

#dao nguoc mang
ls.reverse()
print ("ls revert = ", ls)

#sap xep
ls.sort()
print("ls after sort =",ls)