class Ass:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self,a):
        self.__a=a

    def print(self):
        print(self.__a+self.__b)
