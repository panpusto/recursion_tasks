from tkinter import *

window = Tk()
window.title('Squares')
window.geometry("800x600+500+100")
window.geometry("800x600+500+100")

paramN, paramLg, paramX, paramY = 6, 250, 15, 15

labelN = Label(window, text='N=')
labelN.grid(column=0, row=1, padx=5, pady=5)
editN = Entry(window, width=6)
editN.insert(END, '6')
editN.grid(column=1, row=1)

labelLg = Label(window, text='Lg=')
labelLg.grid(column=0, row=2, padx=5, pady=5)
editLg = Entry(window, width=6)
editLg.insert(END, '250')
editLg.grid(column=1, row=2, padx=5, pady=5)

labelX = Label(window, text='x=')
labelX.grid(column=3, row=1)
editX = Entry(window, width=6)
editX.insert(END, '15')
editX.grid(column=4, row=1, padx=5, pady=5)

labelY = Label(window, text='y=')
labelY.grid(column=3, row=2)
editY = Entry(window, width=6)
editY.insert(END, '15')
editY.grid(column=4, row=2, padx=5, pady=5)

canva = Canvas(bg='white', width=300, height=300)

def clear():
    editN.delete(0, END)
    editLg.delete(0, END)
    editX.delete(0, END)
    editY.delete(0, END)

clearBtn = Button(window, text=' Clear ', command=clear)
clearBtn.grid(column=1, row=0, padx=5, pady=5)

def squares(paramN, paramLg, x, y):
    if paramN > 0:
        canva.create_line(x, y, x + paramLg, y)
        canva.create_line(x + paramLg, y, x + paramLg, y + paramLg)
        canva.create_line(x + paramLg, y + paramLg, x, y + paramLg)
        canva.create_line(x, y + paramLg, x, y)

        canva.create_line(x, y + paramLg / 2, x + paramLg / 2, y + paramLg)
        canva.create_line(x + paramLg / 2, y + paramLg, x + paramLg, y + paramLg / 2)
        canva.create_line(x + paramLg, y + paramLg / 2, x + paramLg / 2, y)
        canva.create_line(x + paramLg / 2, y, x, y + paramLg / 2)
        
        squares(paramN - 1, paramLg / 2, x + paramLg / 4, y + paramLg / 4)
        
    canva.grid(column=5, row=3,padx=5, pady=5)

def draw():
    canva.delete('all')
    paramN = int(editN.get())
    paramLg = int(editLg.get())
    paramX = int(editX.get())
    paramY = int(editY.get())

    print(paramN, paramLg, paramX, paramY)
    squares(paramN, paramLg, paramX, paramY)

drawButton = Button(window, text=' Draw ', command=draw)
drawButton.grid(column=0, row=0)

window.mainloop()
