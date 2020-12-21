from tkinter import *

import random


root = Tk()
root.title('Игра в кубик')

f_names1 = Frame(root)
f_names2 = Frame(root)
f_kubik1 = Frame(root)
f_kubik2 = Frame(root)
f_bot = Frame(root)


num_1 = 0
num_2 = 0

def rnd(num):
	global num_1
	global num_2
	global out_1
	global out_2

	if num == 'num_1':
		num_1 = random.randint(1, 6)
		out_1['text'] = str(num_1)
	elif num == 'num_2':
		num_2 = random.randint(1, 6)
		out_2['text'] = str(num_2)

def f():
	global out_3
	global name_1
	global name_2
	if num_1 > num_2:
		out_3['text'] = f'Выиграл {name_1.get()}'

	elif num_1 < num_2:
		out_3['text'] = f'Выиграл {name_2.get()}'

	else:
		out_3['text'] = 'Выиграла дружба'

name_1 = StringVar()
name_2 = StringVar()

entry1 = Entry(f_names1, textvariable = name_1, borderwidth = 1,
         relief="sunken")
entry2 = Entry(f_names2, textvariable = name_2, borderwidth = 1,
         relief="sunken")

n1 = Label(f_names1, text = 'Имя первого игрока:', font = 'Arial 8', fg = 'black')
n2 = Label(f_names2, text = 'Имя второго игрока:', font = 'Arial 8', fg = 'black')


kubik1 = Button(f_kubik1, text = 'Бросает 1-й играющий', font = 'Arial 8', fg = 'black', command = lambda event=None: rnd('num_1'))
kubik2 = Button(f_kubik2, text = 'Бросает 1-й играющий', font = 'Arial 8', fg = 'black', command = lambda event=None: rnd('num_2'))

text_1 = Label(f_kubik1, text = 'Выпало:', font = 'Arial 8', fg = 'black')
text_2 = Label(f_kubik2, text = 'Выпало:', font = 'Arial 8', fg = 'black')



out_1 = Label(f_kubik1,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 5)

out_2 = Label(f_kubik2,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 5) 

out_3 = Label(root,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 17)  

result = Button(root, text = 'Определить результат игры', font = 'Arial 8', fg = 'black', command = lambda event=None: f())


f_names1.pack()
f_names2.pack()
f_kubik1.pack()
f_kubik2.pack()
f_bot.pack()

n1.pack(side = LEFT)

entry1.pack(side = RIGHT)

n2.pack(side = LEFT)

entry2.pack(side = RIGHT)

kubik1.pack(side = LEFT)
text_1.pack(side = LEFT)
out_1.pack(side = RIGHT)
kubik2.pack(side = LEFT)
text_2.pack(side = LEFT)
out_2.pack(side = RIGHT)
result.pack()
out_3.pack()






root.mainloop()