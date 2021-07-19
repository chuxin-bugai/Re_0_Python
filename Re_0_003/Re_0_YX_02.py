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

'''

class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]

        # read trivia data from file
        f = open(filename,'r')
        trivia_data = f.readlines()
        f.close()

        # count and clean up trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1


'''

class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        #read trivia data from file
        f = open(filename,'r')
        trivia_data = f.readlines()
        f.close()

        #count and clean up trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

    def show_question(self):
        print_text(font1, 210, 5, "TRIVIA GAME")
        print_text(font2, 190, 500-20, "Press Keys (1-4) To Answer", purple)

        print_text(font2, 530, 5, "SCORE", purple)
        print_text(font2, 550, 25, str(self.score), purple)

        #get correct answer out of data
        self.correct = (self.data[self.current+5])

        #display question
        question = self.current
        print_text(font1, 5, 80, "QUESTION" + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        #respond to correct answer
        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct - 1] = green
            print_text(font1, 230, 380, "CORRECT!", green)
            print_text(font2, 170, 420, "Press Enter For Next Question", green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wronganswer - 1] = red
            self.colors[self.correct - 1] = green
            print_text(font1, 220, 380, "INCORRECT!", red)
            print_text(font2, 170, 420, "Press Enter For Next Question", red)

        #display answer
        print_text(font1, 5, 170, "ANSWERS")
        print_text(font2, 20, 210, "1 - " + self.data[self.current+1], self.colors[0])
        print_text(font2, 20, 240, "2 - " + self.data[self.current+2], self.colors[1])
        print_text(font2, 20, 270, "3 - " + self.data[self.current+3], self.colors[2])
        print_text(font2, 20, 300, "4 - " + self.data[self.current+4], self.colors[3])

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0


#主代码
def print_text(font, x, y, text, color = (255,255,255), shadow = True):
    if shadow:
        imgText = font.render(text, True, (0,0,0))
        screen.blit(imgText, (x-2,y-2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#主程序初始化代码
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("The Trivia Game")
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0

#load the Trivia data file
trivia = Trivia("trivia_data.txt")


#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()

    #clear the screen
    screen.fill((0,0,200))

    #display trivia data
    trivia.show_question()

    #update the display
    pygame.display.update()

































