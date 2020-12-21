from tkinter import *

import random




root = Tk()

num_c = random.randint(-10, 10)

f_top = Frame(root)
f_bot = Frame(root)
f_bot2 = Frame(root)


root.title('Чет или нечет?')

text_1 = Label(f_top, text = 'Чет или нечет?', fg='black', font = 'Arial 20',)
text_2 = Label(f_top, text = 'Компьютер загадал целое число', fg='black', font = 'Arial 14')
text_3 = Label(f_top, text = 'Какое оно - четное или нечетное? (отметьте переключатель)', fg='black', font = 'Arial 14')

num = StringVar()

#entry_num = Entry(textvariable = num, width = 4)

var_ = IntVar()

rr1 = Radiobutton(f_bot, variable = var_,  text="Чётное", value=2)
rr2 = Radiobutton(f_bot, variable = var_, text="Нечётное", value = 1)

out_ = Label(root,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)

def f(var, num_c):
	if (var.get() % 2) == (num_c % 2):
		out_.config(text = 'Правильно')
	else:
		out_.config(text = 'Неправильно')



butt_ = Button(text = 'Проверить ответ', command = lambda event=None: f(var_, num_c))

f_top.pack()
f_bot.pack()
f_bot2.pack()

text_1.pack()
text_2.pack()
text_3.pack()

rr1.pack(side = LEFT)
rr2.pack(side = RIGHT)

butt_.pack()

out_.pack()


root.mainloop()



