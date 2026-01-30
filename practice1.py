class a:
    def function1(self):
        return 'i am fucntion 1'


class b:
    def function2(self,a):
        print(a.function1())
        return 'i am fucntion 2'


obja = a()
objb = b()

print(objb.function2(obja))