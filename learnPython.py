def addSeparator():
	return "\n==============================================================\n"
def add(firstNumber, secondNumber):
	return firstNumber + secondNumber

def subtract(firstNumber, secondNumber):
	return firstNumber - secondNumber

def multiply(firstNumber, secondNumber):
	return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
	return firstNumber / secondNumber

print(add(2,4))
print(subtract(2,4))
print(multiply(2,4))
print(divide(2,4))

print(addSeparator())

str = 'This is some random string'
print (len(str)) # get string length
print(addSeparator())
str = 'this string is small case. please captilize'
print (str.title()) # this will upper case for each word
print (str.capitalize()) # Capitalizes first letter of string
print(str.find('case')) # find appearance of string in a string, at which position
print(str.replace('case', 'mess')) # replace a string with a string in a string
print(str[21:25]) # this will return 'case' from the string. Just another way.
print(addSeparator())
var1 = 'Hello'
var2 = 'World'
print (var1 + var2)
print(var1*2)
print('H' in var1)
print('h' in var1)


print "My name is %s and weight is %d kg!" % ('Milan', 65)

print(addSeparator())
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str
print(addSeparator())
# below will 2 slashes
print r'C:\\nowhere'

# this will slow one slash
print 'C:\\nowhere'

print(addSeparator())
str = "milan";
print "str.center(40, 'a') : ", str.center(15, 'a')

print(addSeparator())
Str = "this is string example....wow!!!";
Str = Str.encode('base64','strict');
print "Encoded String: " + Str
print "Decoded String: " + Str.decode('base64','strict')

print(addSeparator())
str = "this is\tstring example....wow!!!";
print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(16)

print(addSeparator())
str1 = "this is string example!!!";
str2 = "exam";
print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 0, len(str1))

print(addSeparator())
str = "this2009";  # No space in this string
print str.isalnum()
print str.isalpha()
str = "this is string example....wow!!!";
print str.isalnum()
str1 = "MILAN"
str2 = "Milan"
str3 = "milan"
print str1.islower()
print str2.islower()
print str3.islower()
print str1.isupper()

print(addSeparator())
s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

str = "   Milan"
print str;
print str.lstrip()

str = "Using Swapcase. this is typed in lowercase. but output would be upper case";
print str.swapcase()