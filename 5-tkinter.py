from tkinter import *

import random

popitok = 0
prav = 0
neprav = 0


root = Tk()

num_c = random.randint(-10, 10)

f_top = Frame(root)
f_bot = Frame(root)
f_bot2 = Frame(root)
f_3 = Frame(root)
f_33 = Frame(root)
f_4 = Frame(root)
f_5 = Frame(root)
f_6 = Frame(root)


root.title('Чет или нечет?')

text_1 = Label(f_top, text = 'Чет или нечет?', fg='black', font = 'Arial 20',)
text_2 = Label(f_top, text = 'Компьютер загадал целое число', fg='black', font = 'Arial 14')
text_3 = Label(f_top, text = 'Какое оно - четное или нечетное? (отметьте переключатель)', fg='black', font = 'Arial 14')

num = StringVar()

#entry_num = Entry(textvariable = num, width = 4)

var_ = IntVar()

rr1 = Radiobutton(f_bot, variable = var_,  text="Чётное", value=2)
rr2 = Radiobutton(f_bot, variable = var_, text="Нечётное", value = 1)

out_ = Label(f_33,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)

def f(var):
	global popitok
	global prav
	global num_c
	global neprav

	if (var.get() % 2) == (num_c % 2):
		out_.config(text = 'Правильно')
		prav += 1
	else:
		out_.config(text = 'Неправильно')
		neprav += 1

	popitok += 1

	nums_popitok['text'] = str(popitok)
	pravs['text'] = str(prav)
	nepravs['text'] = str(neprav)

	num_c = random.randint(-10, 10)	


def f33():
	global popitok
	global prav
	global neprav

	popitok, prav, neprav = 0, 0, 0

	nums_popitok['text'] = ''
	pravs['text'] = ''
	nepravs['text'] = ''
	out_['text'] = ''




butt_ = Button(f_3, text = 'Проверить ответ', command = lambda event=None: f(var_))
butt_2 = Button(root, text = 'Сыграть еще раз', command = lambda event=None: f33())

nums_popitok = Label(f_4,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)
pravs = Label(f_5,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)
nepravs = Label(f_6,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)

text_4 = Label(f_4, text = 'Общее число попыток', fg='black', font = 'Arial 8')
text_5 = Label(f_5, text = 'Из них правильных ответов', fg='black', font = 'Arial 8')
text_6 = Label(f_6, text = 'Неправильных', fg='black', font = 'Arial 8')

f_top.pack()
f_bot.pack()
f_bot2.pack()
f_3.pack()
f_4.pack()
f_5.pack()
f_6.pack()
f_33.pack()



text_1.pack()
text_2.pack()
text_3.pack()

butt_2.pack()

rr1.pack(side = LEFT)
rr2.pack(side = RIGHT)

butt_.pack(pady = 3)

out_.pack()

nums_popitok.pack(side = RIGHT)
pravs.pack(side = RIGHT)
nepravs.pack(side = RIGHT)

text_4.pack(side = LEFT)
text_5.pack(side = LEFT)
text_6.pack(side = LEFT)




root.mainloop()



