class calc:
    def __init__ (self , name):
        print (f'welcome {name}')

    def sum (self,x,y):
        print (x+y)

class sincalc (calc):
    def __init__ (self , name):
        super (sincalc , self).__init__(name)
        print ('Test Mahmoud')

    def power (self,x,y):
        print (x*y)

t = sincalc ('mahmoud')
t.sum(2,3)
t.power(5,6)
