from tkinter import *

from math import ceil

root = Tk()

root.title('Шифр Бофорта')

f_1 = Frame(root)
f_2 = Frame(root)
f_3 = Frame(root)


word_en = StringVar()
key_en = StringVar()

start_text = Label(root, text = 'Шифр Бофорта', fg='black', font = 'Arial 26')


word_text = Label(f_1, text = 'Введите слово: ', fg='black', font = 'Arial 14')
enter_word = Entry(f_1, textvariable = word_en)


key_text = Label(f_2, text = 'Введите ключ: ', fg='black', font = 'Arial 14')
key_word = Entry(f_2, textvariable = key_en)




output = Label(root,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 20)

crypt = ''



def func_():
	global word 
	global key 
	global crypt
	global output

	word = word_en.get()
	key = key_en.get()

	square_A = [[''] * 26 for i in range(26)]
	square_a = [[''] * 26 for i in range(26)]

	for i in range(26):
		for k in range(26):
			square_A[i][k] = chr(90 - (k + i)%26)

	for i in range(26):
		for k in range(26):
			square_a[i][k] = chr(122 - (k + i)%26)  

	arr_ = []

	crypt = ''

	k = 0


	for i in range(len(word)):

		if word[i].isupper() == False: 
			square, ml = square_a, 97

		else: 
			square, ml = square_A, 65
		mk = ord(key[k % len(key)].upper()) - 65 

		crypt += square[ord(word[i]) - ml][mk] 
		k += 1

	output['text'] = crypt



butt_ = Button(f_3, text = 'Зашифровать слово', fg = 'black', font = 'Arial 8', command = func_)



start_text.pack(pady = 20)

f_1.pack()
f_2.pack()
f_3.pack()

word_text.pack(side = LEFT, pady = 10)
enter_word.pack(side = LEFT, pady = 10)

key_text.pack(side = LEFT, pady= 5)
key_word.pack(side = RIGHT, pady = 5)

butt_.pack(pady = 10)
output.pack(pady = 5)

print('Зашифрованное слово: ' + crypt)

root.mainloop()





