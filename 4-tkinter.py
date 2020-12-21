from tkinter import *



root = Tk()
root.title("Универсальный лькулятор")

f_1 = Frame(root)
f_2 = Frame(root)
f_3 = Frame(root)

num_ = StringVar()

num_1 = 0
num_2 = 0

def func_():
	global inp_
	global num_1

	num_1 = int(inp_.get())
	inp_.delete(first = 0, last = len(str(num_1)))

	
def func_2():
	global cond
	global inp_
	global num_2

	cond = cond.get()

	num_2 = int(inp_.get())

	if cond == '+':
		inp_.delete(0,"end")
		inp_.insert(0, str(num_1 + num_2))
	if cond == '-':
		inp_.delete(0,"end")
		inp_.insert(0, str(num_1 - num_2))
	if cond == '*':
		inp_.delete(0,"end")
		inp_.insert(0, str(num_1*num_2))
	if cond == '/':
		inp_.delete(0,"end")
		inp_.insert(0, str(num_1/num_2))


	

inp_ = Entry(f_1, textvariable = num_)

butt_1 = Button(f_2, text = 'Ввести второе число', command = func_)
butt_2 = Button(root, text = '=', command = func_2)


cond = StringVar()

rr1 = Radiobutton(f_3, variable = cond,  text="Сложение", value='+')
rr2 = Radiobutton(f_3, variable = cond, text="Вычитание", value = '-')
rr3 = Radiobutton(f_3, variable = cond,  text="Умножение", value='*')
rr4 = Radiobutton(f_3, variable = cond, text="Деление", value = '/')


f_1.pack()
f_2.pack()
rr1.pack(side = LEFT)
rr2.pack(side = LEFT)
rr3.pack(side = LEFT)
rr4.pack(side = LEFT)
f_3.pack()
inp_.pack()
butt_1.pack(pady = 5)
butt_2.pack()

root.mainloop()