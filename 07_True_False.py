Напишите программу, принимающую на вход целое число, которая выводит True, 
если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и 
False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов. 
В задании используются полуоткрытые и открытые интервалы.

# put your python code here
a = int(input())
if a <= 12 and a > -15:
    print('True')
elif a > 14 and a < 17:
    print('True')
elif a >= 19:
    print('True')
else:
print('False')
