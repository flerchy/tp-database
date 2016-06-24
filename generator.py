#/usr/bin/python

name = ['marina', 'anna', 'artem', 'martin', 'polina', 'sasha']
username = ['flerchy', 'terehova', 'puhovity', 'nitram', 'kristeldi', 'html_sanek']
about = ['zaebalas', 'hidronautics', 'loves maths', 'top frontend', 'nyashka', 'vse dauni']
email = ['flerchy@mail.ru', 'tereha@bmstu.ru', 'viebgo@martin.ru', 'dezi2004@rambler.ru', 'htmlnek@mail.ru']
letters = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j', 'k','l','m','n','o','p','1','2','3','4']

res = email
count = 6
for i in email:
    for j in letters:
        res.append(j+i)
        count += 1
        if (count == 7000):
            break
    if (count == 7000):
        break
for i in range (0, 6000):
    name.append(name[i%6])
    username.append(username[i % 6])
    about.append(about[i % 6])
#    print name[i]
for i in range(1,6000):
    str = 'insert into User(username, about, isAnonymous, name, email) values("' 
    str += username[i] +'","'+about[i]+'", '+"false" + ', "'+ name[i] + '", "'+ res[i] + '");'
    print str
