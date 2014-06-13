test_str = "100" #def as String 
print int(test_str) + 50 # calc as int 

test = 56
print test + 10
print test - 10
print test * 10
print test / 10


import datetime 
if __name__ == "__main__":
    today = datetime.date.today()
    #today's date 
    print today
    #tomorrow's date
    print today + datetime.timedelta(days=1)
    newyear = datetime.datetime(2010,1,1)
    
    #7days after 2010/1/1 
    print newyear + datetime.timedelta(days = 7)
    # number of days from 2010/1/1/ to today
    #calc = today - newyear
    #print calc.days
    
def myfunction(name): #void myfunction(String name)
    return 'Hello, ' + name
print myfunction('Kaya')

def maths():
    return "This is the maths function"
print maths()

testString = maths()