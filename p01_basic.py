# This is an annotation.

import time

# Show current time in milliseconds
print('Current time: ' + str(time.time()))

# A simple example, use 4 spaces for code indent
if 10 - 9 > 0:
    print("10 is greater than 9")

# Calculate download speed
bandwidth = 100
ratio = 8
print('For %d Mbps bandwidth, your maximum download speed is %d MB/s. ' % (bandwidth, bandwidth / ratio))

# Access elements in sequence
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
print('First four Chinese zodiacs: ' + chinese_zodiac[0:4])
print('Last Chinese zodiac: ' + chinese_zodiac[-1])
now_year = 2020
print(now_year % 12 - 4)
print('This year is year of ' + chinese_zodiac[now_year % 12 - 4])
print('猪' not in chinese_zodiac)
print(chinese_zodiac + 'test')
print(chinese_zodiac * 2)

# Figure out zodiac according to the birthday you entered
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (12, 26)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])

# Manipulate list
a_list = ['abc', 'xyz']
a_list.append('zzz')
a_list.remove('xyz')
print(a_list)

# Conditions and loop
test_num = int(input('Please enter a number: '))
if test_num < 0:
    print('You entered a negative number.')
elif 0 <= test_num < 100:
    print('You entered a positive number.')
else:
    print('You entered a big number.')

for year in range(2010, 2021):
    print('%s is year of %s' % (year, chinese_zodiac[year % 12 - 4]))

temp_num = 0
while True:
    temp_num += 1
    if temp_num == 3:
        continue
    if temp_num > 5:
        break
    print('Counting %d' % temp_num)
    time.sleep(1)

# Nested loop
birth_month = int(input('Enter the month of your birthday: '))
birth_day = int(input('Enter the day of your birthday: '))
print('Calculating zodiac by FOR nested loop...')
for zd_num in range(len(zodiac_days)):                      # Loop 12 zodiacs
    if zodiac_days[zd_num] >= (birth_month, birth_day):     # Compare input date with each zodiac
        print('Your zodiac is: ' + zodiac_name[zd_num])
        break
    elif birth_month == 12 and birth_day > 23:              # Capricornus
        print('Your zodiac is: ' + zodiac_name[0])
        break

zd_num = 0
print('Calculating zodiac by WHILE nested loop...')
while zodiac_days[zd_num] < (birth_month, birth_day):
    if birth_month == 12 and birth_day > 23:
        break
    zd_num += 1
print('Your zodiac is: ' + zodiac_name[zd_num])

# Use dictionary to show distribution of zodiacs
count_chinese_zodiac = {}
count_zodiac = {}
for i in chinese_zodiac:
    count_chinese_zodiac[i] = 0
for i in zodiac_name:
    count_zodiac[i] = 0
count_num = 0
while True:
    birth_year = int(input('Please enter the year of your birthday: '))
    birth_month = int(input('Please enter the month of your birthday: '))
    birth_day = int(input('Please enter the day of your birthday: '))
    cz_name = chinese_zodiac[birth_year % 12 - 4]
    count_chinese_zodiac[cz_name] += 1
    zodiac_day = filter(lambda x: x <= (birth_month, birth_day), zodiac_days)
    zodiac_len = len(list(zodiac_day)) % 12
    z_name = zodiac_name[zodiac_len]
    count_zodiac[z_name] += 1
    count_num += 1
    for each_key in count_chinese_zodiac.keys():
        print('There\'s %d people has Chinese zodiac of %s.' % (count_chinese_zodiac[each_key], each_key))
    for each_key in count_zodiac.keys():
        print('There\'s %d people has the sign of %s.' % (count_zodiac[each_key], each_key))
    if count_num == 3:
        break

# Comprehensions (another solution instead of FOR statements)
a_list = []
for i in range(1, 11):
    if i % 2 == 0:
        a_list.append(i * i)
print(a_list)

b_list = [i * i for i in range(1, 11) if i % 2 == 0]
print(b_list)

count_zodiac = {}
for i in zodiac_name:
    count_zodiac[i] = 0
count_zodiac = {i: 0 for i in zodiac_name}
print(count_zodiac)
