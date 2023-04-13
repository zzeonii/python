>>> class FourCal:
    def __init__(inst,first,second):
        inst.first=first
        inst.second=second
    def add(inst):
        result=inst.first+inst.second
        return result
    def mul(inst):
        result=inst.first*inst.second
        return result
    def sub(inst):
        result=inst.first-inst.second
        return result
    def div(inst):
        result=inst.first/inst.second
        return result
#클래스 상속
class MoreFourCal(FourCal):
    pass
