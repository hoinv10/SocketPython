dic = {
    'a' : 1,
    'b' : 3,
    'c' : 2
}

#them phan tu moi vao dictionary
dic['d'] = 5;
print (dic)

#gan dic1 = dic, khi thay doi dic1 thi dic cung thay doi theo => can ham copy
dic1 = dic
dic1['d'] = 1000
print (dic)
dic2 = dic.copy()
dic2['d'] = 1111
print(dic)

#fromkey => copy key cua dic ra, gan tat ca cac value = 2
fk = dict.fromkeys(dic,2)
print (fk)

#tra ve mot mang chua key or value
print (dic.keys())
print (dic.values())
