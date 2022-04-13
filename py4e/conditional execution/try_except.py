astr = 'Hello Bob'
try:
    astr = int(astr)
except:
    astr = -1
print('First ', astr)

astr = '123'
try:
    astr = int(astr)
except:
    astr = -1
print('Second ', astr)
