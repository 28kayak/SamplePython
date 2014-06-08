print 'python-izm' 
print "python-izm"

test_str = """
test 1 
test 2
test 3
test 4 ....
"""
print test_str
#by using 3 quo, can write a string statement for multi-lines.

test1_str = "Pyhton"
test1_str = test1_str + ' Hello'
test1_str = test1_str + "World"

print test1_str

#using replace function
test_str = "python-izm"
print test_str.replace("izm","ism")

#using split function
test_str = "python-izm"
print test_str.split("-")
test = "Plastic Wrap"
print test.split(" ")
"""
    split function returns an array which is defined with String type
    
"""

#using rjust function
test_str = "1234"
print test_str.rjust(10,"0")
print test_str.rjust(15,"*")
"""
    identically rjust function also returns an array
    whose the length is defined by 1st parameter and 
    which fill up with a letter that is provided by 2nd paramter.
"""
