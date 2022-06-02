class A:

    def __init__(self,name):
        self.name = name

class B(A):

    def __init__(self, personName, personAge):

        self.age = personAge
        A.name = personName

    def __str__(self):
        return'Person(name='+self.name+',Age:'+str(self.age)+')'
        b.B("",21)
        print(b.__init__.__str__())
