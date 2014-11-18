"""
Projektowanie i programowanie w GIS
Krzysztof Sochiera
Sparawozdanie 2
Zadanie 3
"""
import math
class complex_numbers(object):
    def __init__(self, real, unreal):
        self.real=real
        self.unreal=unreal
    def add_cn(self, a_r, a_u):
        r=self.real+a_r
        u=self.unreal+a_u
        return "%r + %ui" % (r,u)
    def substrack_cn(self,a_r,a_u):
        r=self.real-a_r
        u=self.unreal-a_u
        if u>0:
            return "%r + %ui" % (r,u)
        elif u<0:
            return "%r - %ui" % (r,-u)
        else:
            return r
    def absolute_cn(self):
        return math.sqrt(self.real**2 + self.unreal**2)
    def display_cn(self):
        if self.unreal>0:
            return "%r + %ui" % (self.real,self.unreal)
        elif self.unreal<0:
            return "%r - %ui" % (self.real,-self.unreal)
        else:
            return r
    def getReal(self):
        return self.__real
    def setReal(self,real):
        self.__real=real
    real=property(getReal,setReal)
    
liczba=complex_numbers(2,3)
print liczba.substrack_cn(4,8)
print liczba.absolute_cn()
print liczba.display_cn()
print liczba.real
liczba.real=5
print liczba.real
