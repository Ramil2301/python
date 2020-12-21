from tkinter import *
 
countries = ["Russia", "Ukraine", "Belarus", "USA"]

cities = ["Moscow", "Kiyv", "Minsk", "Vashington"]

root = Tk()
root.title("Страна и столица")

f_1 = Frame(root)
f_2 = Frame(root)
f_3 = Frame(root)
 
scrollbar = Scrollbar(f_1)
scrollbar.pack(side=RIGHT, fill=Y)
 
languages_listbox = Listbox(f_1, yscrollcommand=scrollbar.set, width=40)
 
for country in countries:
    languages_listbox.insert(END, country)
 
languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)

out_ = Label(f_3,
         borderwidth = 1,
         relief="sunken",
         bg = 'white',
         font = 'Arial 10',
         width = 15)


def f():
	global languages_listbox
	global out_
	out_['text'] = cities[languages_listbox.curselection()[0]]

butt = Button(f_2, text = 'Определить столицу', command = f)
f_1.pack()
f_2.pack()
f_3.pack()
out_.pack(pady = 5)
butt.pack(pady = 5)

root.mainloop()