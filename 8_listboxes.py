from tkinter import *

# Functions

def submit():
    foods = []
    for item in listbox.curselection():
        foods.append(listbox.get(item))

    print("You have ordered:")

    for i, food in enumerate(foods):
        print(f"{i+1}. {food}")

def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())

def delete():
    for items in reversed(listbox.curselection()):
        listbox.delete(items)
    listbox.config(height=listbox.size())

# GUI

window = Tk()
window.title('Listboxes')
window.config(pady=10,
              padx=10
              )
# Widgets
listbox = Listbox(window,
                  font=('futura',20),
                  selectmode=MULTIPLE,
                  bg='#dce0bc'

                  )
food_list = ['Pizza', 'Burger', 'Fries', 'Salad', 'Nuggets']  #Inserting items into food list
for item in range(len(food_list)):
    listbox.insert(item, food_list[item])
listbox.config(height=listbox.size())

entry = Entry(window,
              font=('futura', 20)
              )
submit_btn = Button(window,
                text='Submit',
                command=submit,
                font=('futura', 12, 'bold'),
                width=20,
                fg='#16f048'

                )
add_btn = Button(window,
                text='Add',
                command=add,
                font=('futura', 12, 'bold'),
                width=20,
                fg='#328ae3'
                )
delete_btn = Button(window,
                text='Delete',
                command=delete,
                font=('futura', 12, 'bold'),
                width=20,
                fg='red'
                )




# Packing
listbox.pack()
entry.pack()
submit_btn.pack()
add_btn.pack()
delete_btn.pack()

window.mainloop()