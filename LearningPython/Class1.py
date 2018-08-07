class hcn:
    dai = 0;
    rong = 0;
    # constructor
    def	__init__(self,	dai	=0 ,	rong=	0):
        self.dai = dai
        self.rong = rong
    def dientich(self):
        return self.dai*self.rong
    def chuvi(self):
        return (self.dai + self.rong)*2


#ke thua
class hinhhop(hcn):
    cao = 0;
    # chồng chất hàm tạo
    def	__init__(self,	dai	=0 ,	rong=	0, cao = 0):
        self.dai = dai
        self.rong = rong
        self.cao = cao

myhcn = hinhhop(3,4,5)
print ("dai =" , myhcn.dai, " rong = " , myhcn.rong)
print ("dien tich =", myhcn.dientich())
print ("chuvi = ", myhcn.chuvi())
    