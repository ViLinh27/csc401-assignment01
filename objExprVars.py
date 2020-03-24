#objExprVars.py

'''
see hw1.py for format for 1st assignment (other assignments will have
different format)
'''

#####IDLE  #####

'''
two modes:
    interactive shell
    file editor

Keyboard shortcuts:
    CTRL- N: new file
    CTRL- S: save file
    f5- run module
    alt-n, alt p: previous and next statement
'''

##### variables #####
'''
variables are names for obects/values
an assignment:
<variable> = <expression>

1) <expression> is calculated
2) result is stored with name <variable>

variables:
-don't exist until they are assigned to
-can be reused/reassigned
=don't care what type they hold
(but expressions do care)

variable names:
-use a...z,A...Z, 0...9, _
-cant start with digit
-names are cAse SENsitIve
-use relatively meanigful names that aren't too long
-use camelCase
-indicate data type and what's in the variable
-don't use reserved words or core language
-not suggested to use builtins

'''
##### expressions #####
'''
WE can use idle like a calculator

use these operations
(listed in precedence order)
()
**
*,/,//,%
+,-


// and % are friends

>>> #132 minutes in hours, minutes
>>> 132//60
2
>>> 132%60
12

usually use for intergers

floats tend to be approximations:
>>> 123.65 % 1
0.6500000000000057

>>> #functions
>>> abs(-5)
5
>>> max(-2,-3)
-2


>>> #convert 32 degrees farenheight
>>> #to celsius
>>> (32-32)* 5/9


dynamic typing
python doesn't check variable type until it's used in code
can be potentially problematic


>>> #farenheight to celsius
>>> f = 32
>>> c = (f-32) * 5/9
>>> c
0.0
>>>


#the vars "notebook" doesn't remember expressions but remembers what was
#was computed(the results)

>>> c = (f-32) * 5/9
>>> f = 212
>>> c = (f-32) * 5/9
>>> c
100.0


if is part of the core language
max is not. It's a function. Part of a "builtins"

when python looks for a max but max is a variable, it looks in builtins


'''

#####bool(ean) expressions ######
'''
boolean expressions
-math expressions
with results of True or False

boolean operators
==,!= : equal, not equal
<,>,<=, >=,

compount operators
and, or, not

conversions:
    from bool to int/float
    True-> 1, False-> 0

    from int/float to bool
    0-> False, everything else=> True

>>> x = 2
>>> x==3
False
>>> x !=3
True
>>> x<2
False
>>> x<=2
True
>>> import random
>>> x = random.randrange(0,100) #0..9
>>> 
>>> x%2
0
>>> #is x odd?
>>> x %2 !=0
False
>>> x
48
>>> x = random.randrange(0,100) #0..99
>>> x
27
>>> x %2 1=0
SyntaxError: invalid syntax
>>> x%2 !=0
True
>>> x
27
>>> #check whether a number is divisible by 3
>>> x%3 ==0
True
>>> 
>>> x = random.randrange(0,100)
>>> x%3 ==0
False
>>> x
31
>>> #x is divisibe by 2 or 3
>>> x = random.randrange(0,100)
>>> x%2 ==0 or x%3==0
True
>>> x
74
>>> x%2 ==0 and x%3==0
False
>>> x
74
>>> 
>>> #negation
>>> x = 5
>>> x<6
True
>>> not x<6
False
>>> #pitfall
>>> #is x one of 2,3, or 4
>>> x = 7
>>> x ==2 or 3 or 4
3
>>> #should have written
>>> x==2 or x==3 or x--4
11
>>> x==2 or x==3 or x==4
False
>>> 
'''




#####type/class of an object ######
'''
variabes don't have a type but


>> type(3)
<class 'int'>
>>> type(3.3)
<class 'float'>
>>> x = 9.3
>>> type(x)
<class 'float'>
>>> type(11//3)
<class 'int'>
>>> type ('apple')
<class 'str'>
>>> type([1,2,3])
<class 'list'>
>>> type(x==3)
<class 'bool'>
>>> 

'''


#####str(int) #####
'''
str

-0-based indexed sequence of characters

for textual data
delimit strings with '', '' '' , ''' ''',
\n is new line character

functions
len() : length
max, min

operators
in, not in
+ - concatenation
int*str, str*int - multiples
<,>, <= , >= , ==, != (al upper case less than all lower case)

indexing
s[i] - character at index i
i from 0 to len(s)-1
or backwards from -1 to -len(s)

slicing:
s[start: stop] - substring of s starting at start (inclusive) and stopping at
stop (exclusive)

start defaults to 0 stop defualts to end

s[start: stop : step]

s[::-1] - reverse of s


s = 'pear'
>>> type(s)
<class 'str'>
>>> t = "apple"
>>> t
'apple'
>>> u = "Fred's place"
>>> u - 'Fred\'s place'4
SyntaxError: invalid syntax
>>> u - 'Fred\'s place'
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    u - 'Fred\'s place'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> u = 'Fred\'s place'
>>> u
"Fred's place"
>>> s
'pear'
>>> len(s)
4
>>> #string on multiple lines
>>> sentence - "this is......................."
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    sentence - "this is......................."
NameError: name 'sentence' is not defined
>>> #right way to do it#####
>>> sentence = '''this is a sebtebce that runs onto multiple lines'''
>>> 'this is sentence \n that runs oto multiple lines\n;'
'this is sentence \n that runs oto multiple lines\n;'
>>> 
>>> #print(sentence)
>>> print(sentence)
this is a sebtebce that runs onto multiple lines
>>> 'this is sentence\n that runs oto multiple \nlines;'
'this is sentence\n that runs oto multiple \nlines;'
>>> 
>>> 
>>> hello
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> 
>>> print(hello)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined
>>> #in tests for substring
>>> 'app' in "apple"
True
>>> Apl kn 'apple''
SyntaxError: invalid syntax
>>> 
>>> 
>>> 3*(2s-t)
SyntaxError: invalid syntax
>>> 3*(2* s-t)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    3*(2* s-t)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
>>> 
>>> 
>>> 'apple' < 'pear'
True
>>> "compares dictionary order!
SyntaxError: EOL while scanning string literal
>>> #dompares dictionary order
>>> 
>>> 
>>> #indexing
>>> s
'pear'
>>> s[1]
'e'
>>> s[0]
'p'
>>> 
>>> 
>>> #empty str
>>> s = "" #not empty
>>> #empt string the right way
>>> s = ""
>>> len(s)
0
>>> 
>>> 
>>> #slicing
>>> 
>>> s = 'apple'
>>> s{1:4}
SyntaxError: invalid syntax
>>> s[1:4]
'ppl'
>>> 
>>> s[::2]
'ape'
>>>



>>> 'Ap'not in 'apple'
True
'''
