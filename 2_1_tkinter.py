from tkinter import *

import random


root = Tk()
root.title('Игра в кубик')


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
	if num_1 > num_2:
		out_3['text'] = 'Выиграл 1-й играющий'

	elif num_1 < num_2:
		out_3['text'] = 'Выиграл 2-й играющий'

	else:
		out_3['text'] = 'Выиграла дружба'



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


f_kubik1.pack()
f_kubik2.pack()
f_bot.pack()

kubik1.pack(side = LEFT)
text_1.pack(side = LEFT)
out_1.pack(side = RIGHT)
kubik2.pack(side = LEFT)
text_2.pack(side = LEFT)
out_2.pack(side = RIGHT)
result.pack()
out_3.pack()






root.mainloop()





