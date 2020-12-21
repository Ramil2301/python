from tkinter import *

import random

pops = 0
w1 = 0
w2 = 0
wn = 0

root = Tk()
root.title('Игра в кубик')


f_kubik1 = Frame(root)
f_kubik2 = Frame(root)
f_bot = Frame(root)
f_4 = Frame(root)
f_5 = Frame(root)
f_6 = Frame(root)
f_7 = Frame(root)


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
	global pops
	global w1
	global w2
	global wn
	if num_1 > num_2:
		out_3['text'] = 'Выиграл 1-й играющий'
		w1 += 1
		w1_l['text'] = str(w1)
	elif num_1 < num_2:
		out_3['text'] = 'Выиграл 2-й играющий'
		w2 += 1
		w2_l['text'] = str(w2)
	else:
		out_3['text'] = 'Выиграла дружба'
		wn += 1
		nichi['text'] = str(wn)
	pops += 1
	wn_l['text'] = str(pops)




kubik1 = Button(f_kubik1, text = 'Бросает 1-й играющий', font = 'Arial 8', fg = 'black', command = lambda event=None: rnd('num_1'))
kubik2 = Button(f_kubik2, text = 'Бросает 2-й играющий', font = 'Arial 8', fg = 'black', command = lambda event=None: rnd('num_2'))

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

num_pops = Label(f_4,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)
w1_l = Label(f_5,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)
w2_l = Label(f_6,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)
wn_l = Label(f_4,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)

nichi = Label(f_7,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 14)


text_4 = Label(f_4, text = 'Общее число попыток', fg='black', font = 'Arial 8')
text_5 = Label(f_5, text = 'Из них 1-й играющий выиграл', fg='black', font = 'Arial 8')
text_6 = Label(f_6, text = 'Из них 2-й играющий выиграл', fg='black', font = 'Arial 8')
text_7 = Label(f_7, text = 'Ничьих', fg='black', font = 'Arial 8')

def new():
	global w1
	global w2
	global wn
	global num_pops

	w1, pops, wn, w2 = 0, 0, 0, 0

	num_pops['text'] = ''
	w1_l['text'] = ''
	w2_l['text'] = ''
	wn_l['text'] = ''
	nichi['text'] = ''
	out_3['text'] = ''


butt_new = Button(text = 'Сыграть еще раз', command = new)



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
out_3.pack(pady = 5)
f_4.pack()
f_5.pack()
f_6.pack()
f_7.pack()


text_4.pack(side = LEFT)
text_5.pack(side = LEFT)
text_6.pack(side = LEFT)
text_7.pack(side = LEFT)
nichi.pack(side = RIGHT)
w1_l.pack(side = RIGHT)
w2_l.pack(side = RIGHT)
wn_l.pack(side = RIGHT)

butt_new.pack()






root.mainloop()





