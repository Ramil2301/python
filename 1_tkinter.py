from tkinter import *

import random

num_c = random.randint(-10, 10)

def enter_(out_, num_c, num_u):
	num_u = int(num_u.get())
	if (num_c % 2) == (num_u % 2):
		out_.config(text = 'Правильно')
	else:
		out_.config(text = 'Неправильно')




root = Tk()

root.title('Чет или нечет?')

text_1 = Label(root, text = 'Чет или нечет?', fg='black', font = 'Arial 20')
text_2 = Label(root, text = 'Компьютер загадал целое число', fg='black', font = 'Arial 14')
text_3 = Label(root, text = 'Какое оно - четное (введите 2) или нечетное (введите 1)?', fg='black', font = 'Arial 14')

num = StringVar()

entry_num = Entry(textvariable = num, width = 4)



out_ = Label(root,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)

root.bind('<Return>', lambda event=None: enter_(out_, num_c, entry_num))

text_1.grid()
text_2.grid()
text_3.grid()
entry_num.grid(row = 2, column = 1)
out_.grid()

root.mainloop()



