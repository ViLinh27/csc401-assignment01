#hw1.py, Vi-Linh Dat Nguyen-collaborators: Vi-Anh Dat Nguyen, Joe Zaksheske

#2.11
listnum = [-7,-6,-5,-4,-3,-2,-1]
print(sum(listnum))

kidAge = [17,9,24,10,21,11,27,12]
print(sum(kidAge)/len(kidAge))

print(2**-20)

print(4356//61)

print(4356%61)


#2.12
s1 = '-'

s2 = '+'

s1+s2
s1+s2+s1
s2+s1*2
2*(s2+s1*2)
10*(s2+s1*2)+s2
5*(s2+s1+3*s2+2*s1)

#2.14
s = 'goodbye'
s.index('g')==0
      
s.index('g')==6
      
s[0]=='g' and s[1]=='a'
      
(len(s)-1)=='x'
      
s[len(s)//2]=='d'

s[0]==s[-1]
    
s[-5:-1]=='tion'
      


#2.15
s1 = "counterintuitive"
s2 = "anachronistically"
len(s2)==len(s1)+1

'misinterpretation'< 'misrepresentation'

'e' in "floccinaucinihilipilification"

len("counterrevolution")==(len("counter")+len("resolution"))


#2.16
a = 6
b = 7

c = (a+b)/2

inventory = ['paper','staples','pencils']

first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'

fullname = first+' '+middle+' '+last


#2.18
flowers = [ 'rose','bougainvillea','yucca', 'marigold', 'dailylilly',
            'lilly of the valley']

'potato' not in flowers


thorny = flowers[0:3]

poisonous = [flowers[-1]]

dangerous = thorny + poisonous


#2.19
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
numYes = answers.count('Y')

numNo = answers.count('N')

percentYes = (numYes/len(answers))*100

answers.sort()

f = answers.index('Y')


#2.20
s = 'say'
print(s[::-1])#the cheap method


#2.26
#radius 10
#center is (0,0)
import math
#(0,0)
x=0
y=0
dbR=10
(x**2+y**2)**0.5<10
#(10,10)
x = 10
y = 10
(x**2+y**2)**0.5<10
#(6,-6)
x= 6
y = -6
(x**2+(y)**2)**0.5<10
#(-7,8)
x = -7
y = 8
(x**2+(y)**2)**0.5<10



if __name__=='__main__':
    import doctest
    print( doctest.testfile('hwnTEST.py'))

