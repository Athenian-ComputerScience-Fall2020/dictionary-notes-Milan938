# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  

info = {'name': 'Max', 'job': 'Teacher', 'age': '40', 'hobbies': ['biking', 'swimming']}

info['phone'] = '555-5555'
info['name'] = 'John'

info.update({'name': 'John', 'age': '49', 'job': 'Professor'})
del info['name']

job = info.pop('job')

print(info.get('phone', 'not found'))
print(info)

print(info.items())

for key, value in info.items():
    print(key, value)