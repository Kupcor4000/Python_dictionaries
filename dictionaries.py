course = {'name':'Piter', 'surname':'Molenda', 'skill':'Beginner'}
print(course['name'])
print(course.keys())
course['name'] = 'Marek'
print(course)
course['language'] = 'English'
print(course)
del(course['language'])
print(course)