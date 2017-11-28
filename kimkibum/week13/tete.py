s = 'a s d f'
s = s.split(' ')
del s[1]
s.insert(1,'z')
a= ''
for i in s:
    a += i
print(s)
print(a)