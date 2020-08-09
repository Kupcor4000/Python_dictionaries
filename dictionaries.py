#functions
def print_package(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))


course = {'name':'Piter', 'surname':'Molenda', 'skill':'Beginner'}

print(course['name'])
print(course.keys())
course['name'] = 'Marek'
print(course)
course['language'] = 'English'
print(course)
del(course['language'])
print(course)
print("")
# wypisze tylko i wylacznie keys
for item in course:
    print(item)
print("")
#wypisze wartosci
for item in course:
    print(course[item])
print("")
for item in course.items():
    key,value = item
    print("{} : {}".format(key,value))

print_package(one = 12,two = 32,three = 43,four = 'okej')
