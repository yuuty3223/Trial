import math

result = math.sqrt(25)
print(result)

print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',', end='.\n')


print(2 + 2)

print('hello')
print("hello")
print('I don\'t know')
print("say \"I don't know\"")
print(r'C:\name\name')

print("##################")
print ("""\
line1
line2
line3\
""")
print("##################")

print('Hi.' * 3 + 'Mike.')
print('Py' + 'thon')
print('Py''thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print("##################")
print(word[:5])
print("##################")
print(word[2:])
print("##################")
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)


print("##################")

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('y')
print(is_start)

print("####################")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

a = 'a'
print(f'a is {a}')
 
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
 
name = 'Sarunonamae'
family = 'Saru'
print(f'My name is {name} {family}. Watashi ha {family} {name}')


r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3,3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)

r.reverse()
print(r)

s = 'My name is Mike'
to_spit = s.split(' ')
print(to_spit)

x = ' #### '.join(to_spit)
print(x)  

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i=', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =',x)

t = (1, 2, 3, 4, 1, 2)
print(t)
print(t.index(1))
print(t.index(1,1))
print(t.count(1))

#print(help(tuple))
print(type(t))


i = 1
print(type(i))

j = 1,
print(type(j))

num_taple = (10, 20)
print(num_taple)

x,y = num_taple
print(x,y)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i,j)

a = 100
b = 200
print(a,b)

a,b = b,a
print(a,b)

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])

d['x'] =100
print(d)

d[1] = 10000
print(d)

print(d.keys())
print(d.values())

d2 = {'x': 1000, 'j':500}

d.update(d2)
print(d)

print(d['x'])
print(d.get('x'))

d.pop('x')
print(d)

del d['y']
print(d)

print('a' in d)

fruits = {
    'apple' : 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])

a = {1, 2, 3, 4, 4, 4, 5, 6}
print(a)

b = {2, 3, 3, 6, 7}
print(b)

print( b - a )



my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D','E','F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple']
kind = set(f)
print(kind)


x = 10 
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')