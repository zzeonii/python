class FourCal:
    def setdata(inst,first,second):
        inst.first=first
        inst.second=second

>>> a=FourCal()
>>> b=FourCal()
>>> a.setdata(4,2) #setdata를 해줘야 속성 추가~~~~
>>> b.setdata(3,7)
>>> id(a.first)
2141215064400
>>> id(b.first)
2141215064368