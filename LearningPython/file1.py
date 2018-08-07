filepath = "test.txt";
mode = 'r'
# r  :	mở	để	đọc	nội	dung	(mặc	định)
# w  :	mở	để	ghi	nội	dung
# a  :	mở	để	ghi	thêm	nội	dung	vào	cuối	file.r+ :	mở	để	đọc	và	ghi.	Con	trỏ	nằm	ở	đầu	file.
# w+ :	mở	để	đọc	và	ghi.	Ghi	đè	nếu	file	đã	tồn	tại,	nếufile	chưa	tồn	tại	thì	tạo	file	mới	để	ghi.
# a+ :	mở	để	đọc	và	thêm	vào	cuối	file.	Con	trỏ	nằm	ở cuối	file.	Nếu	file	chưa	tồn	tại	thì	tạo	file	mới	để	ghi.
fh	=	open(filepath,	mode)
data = fh.read()
print (data)
fh.close()

fw = open(filepath, 'a+')
fw.write("\n dong3: xxxx")
fw.close

import	os
#doi ten file
os.rename('txtfile.txt','test.txt')
#xoa file
os.remove('txtfile.txt')