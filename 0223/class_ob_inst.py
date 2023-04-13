클래스 : 똑같은 무엇인가를 만들 수 있는 설계 도면
객체 : 클래스로 만든 피조물
인스턴스 : 클래스로 만든 객체
*객체(a)와 인스턴스의 차이 : 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용
(예시) a는 객체, a는 클래스의 인스턴스


#클래스 정의
class Human:
    pass

#인스턴스 생성
class Human:
    pass

areum = Human()

#클래스 생성
>>> class Human:
    def __init__(inst,name, age, gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
        
>>
>>> areum = Human("아름", 25, "여자")
print(areum.name)
아름
>>> print(f'이름:{areum.name}, 나이:{areum.age}, 성별:{areum.gender}')
이름:아름, 나이:25, 성별:여자

#클래스 메소드

>>> class Human:
    def __init__(inst,name, age, gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def who(inst):
        print(f'이름:{inst.name}, 나이:{inst.age}, 성별:{inst.gender}')
        
>>> areum=Human('아름',25,'여자')
>>> areum.who()
이름:아름, 나이:25, 성별:여자
#클래스 메소드 _ setinfo
>>> class Human:
    def __init__(inst,name, age, gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def who(inst):
        print(f'이름:{inst.name}, 나이:{inst.age}, 성별:{inst.gender}')
    def setInfo(inst,name,age,gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
        
>>> areum = Human("모름", 0, "모름")
>>> areum.who()
이름:모름, 나이:0, 성별:모름
>>> areum.setInfo("아름", 25, "여자")
>>> areum.who()
이름:아름, 나이:25, 성별:여자

#클래스 소멸자
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)

#Stock 클래스 생성
>>> class Human:
    def __init__(inst,name, age, gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def who(inst):
        print(f'이름:{inst.name}, 나이:{inst.age}, 성별:{inst.gender}')
    def setInfo(inst,name,age,gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def __del__(inst):
        print('나의 죽음을 알리지 말라')
        
>>> areum=Human("아름", 25, "여자")
>>> areum.who()
이름:아름, 나이:25, 성별:여자
>>> del areum
>>> 
>>> class Human:
    def __init__(inst,name, age, gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def who(inst):
        print(f'이름:{inst.name}, 나이:{inst.age}, 성별:{inst.gender}')
    def setInfo(inst,name,age,gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def __del__(inst):
        print('나의 죽음을 알리지 말라')
        
>>> 
>>> areum = Human("아름", 25, "여자")
del(areum)
나의 죽음을 알리지 말라
>>> 
#객체 생성
>>> class Stock:
    def __init__(inst,name,code,PER,PBR,배당수익률):
        inst.name=name
        inst.code=code
        inst.PER=float(PER)
        inst.PBR=float(PBR)
        inst.배당수익률=float(배당수익률)
        
>>> stock=Stock("삼성전자", "005930", 15.79, 1.33, 2.83)



class Stock:
    def __init__(inst,name,code,PER,PBR,배당수익률):
        inst.name=name
        inst.code=code
        inst.PER=float(PER)
        inst.PBR=float(PBR)
        inst.배당수익률=float(배당수익률)
    def set_per(inst,PER):
        inst.PER=PER
    def set_pbr(inst,PBR):
        inst.PBR=PBR
    def set_dividend(inst,DIV):
        inst.배당수익률=DIV
        
>>> stock=Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
>>> stock.PER
15.79
>>> stock.set_per(12.75)
>>> stock.PER
12.75
>>> samsung=Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
>>> hyundai=Stock("현대차","005380", 8.70, 0.35, 4.27)
>>> lg=Stock("LG전자", "066570", 317.34, 0.69, 1.37)
>>> stocks=[samsung,hyundai,lg]
>>> for stock in stocks:
    stock.code, stock.PER
    
('005930', 15.79)
('005380', 8.7)
('066570', 317.34)
>>> 
