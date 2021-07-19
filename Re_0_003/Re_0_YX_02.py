import struct
import sys
import pygame
from pygame.locals import *

'''

print('MAD LIB GAME')
print('Enter answers to the following prompts\n')

guy = input('Name of a famous man: ')
girl = input('Name of a famous woman: ')
food = input('Your favorite food(plural): ')
ship = input('Name of a space ship: ')
job = input('Name of a profession(plural): ')
planet = input('Name of a planet: ')
drink = input('Your favorite drink: ')
number = input('A number from 1 to 10: ')

story = '\nA famous married cuople, GUY and GIRL, went on\n' + \
        'vacation to the planet PLANET1. It took NUMBER\n' + \
        'weeks to get there tracelling by SHIP. They\n' + \
        'enjoyed a luxurious candlelight dinner over-\n' + \
        'looking a DRINK ocean while eating FOOD. But,\n' + \
        'since they were both JOB, they had to cau their\n' + \
        'vacatin short.'

story = story.replace('GUY',guy)
story = story.replace('GIRL',girl)
story = story.replace('FOOD',food)
story = story.replace('SHIP',ship)
story = story.replace('JOB',job)
story = story.replace('PLANET',planet)
story = story.replace('DRINK',drink)
story = story.replace('NUMBER',number)

print(story)

''' # MAD LIB GAME

'''

file = open("data.txt",'w')
file.write('Sample file writing\n')
file.write('This is line 2\n')
file.close()    # 单行 写入


text_line = [
    'Chapter 3\n',
    'Sample text data file\n',
    'This is the third line of text\n',
    'The fourth line looks like this\n',
    'Edit the file with any text editor\n'
]

file = open('data.txt','w')
file.writelines(text_line)
file.close() # 一次性写入 多条信息   

# 这种写入不是 在已有的数据后面 继续写入 而是清空原有数据 只写入本次代码里要显示的数据
''' # 写入 文件

'''

file = open('data.txt','r')
# char = file.read(10)
# all_char = file.read()
# print(char)
# print(all_char)

# one_line = file.readline()
# print(one_line)

one_line_2 = file.readlines()
print(one_line_2)

print('Lines: ',len(one_line_2))
for line in one_line_2:
    print(line.strip())

''' # 读取 文件

'''

file = open('data.txt','wb')
for n in range(1000):
    data = (struct.pack('i',n))
    file.write(data)
file.close()

''' # 写入 二进制文件

'''

file = open('data.txt','rb')
size = struct.calcsize('i')
print(size)

bytes_read = file.read(size)
while bytes_read:
    value = struct.unpack('i',bytes_read)
    value = value[0]
    print(value,end=' ')
    bytes_read=file.read(size)
    print(bytes_read)
file.close()

''' # 读取 二进制文件

class Trivia(object):
    def _init_(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]

































