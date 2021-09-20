# 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
# 딕셔너리의 Key값으로 리스트는 불가능, 튜플은 가능

a = {1:'a',1:'b'} # 1이라는 Key값이 중복으로 사용
print(a)

a = {(1,2):'hi'}
print(a)

# Key 리스트 만들기(keys)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))

# Value 리스트 만들기(values)
print(a.values())

# Key, Value 쌍 얻기(items)
print(a.items())

for i,j in a.items():
    print(i,j)

# Key:Value 쌍 모두 지우기(clear)
a.clear()
print(a)

# Key로 Value 얻기(get)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name')) # == a['name']
print(a.get('phone')) # == a['phone']

# 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값')을 사용하면 편리하다.
print(a.get('foo','bar'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
check = 'name' in a
print(check)

check = 'email' in a
print(check)
