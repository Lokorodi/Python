writer = input('What if your age')
try:
    me = int(writer)
except:
    me = -1

if me > 0:
    print('Lovely')
else:
    print('Not a number')

print('end')
 
