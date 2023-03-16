from tkinter import *

window = Tk()
window.title('Drawing a spiral')
window.geometry('800x600+500+100')

# default values
paramAlpha = 20
paramLg = 180

labelAlpha = Label(window, text=' alpha =')
labelAlpha.grid(column=0, row=1, padx=5, pady=5)
editAlpha = Entry(window, width=6)
editAlpha.insert(END, '20')
editAlpha.grid(column=1, row = 1)

labelLg = Label(window, text=' lg =')
labelLg.grid(column=0, row=2)
editLg = Entry(window, width=6)
editLg.insert(END, '180')
editLg.grid(column=1, row=2, padx=5, pady=5)

canvas = Canvas(width=500, height=500)

def clean():
    editAlpha.delete(0, END)
    editLg.delete(0, END)
    canvas.delete('all')

cleanBtn = Button(window, text=' Clean ', command=clean)
cleanBtn.grid(column=1, row=0, padx=5, pady=5)

def draw_spiral(paramAlpha, paramLg, x, y):
    if (paramLg > 0 and paramLg > paramAlpha and paramLg < 498):
        canvas.create_line(x, y, x + paramLg, y)
        canvas.create_line(x + paramLg, y, x + paramLg, y + paramLg)
        canvas.create_line(x + paramLg, y + paramLg, x + paramAlpha, y + paramLg)
        canvas.create_line(x + paramAlpha, y + paramLg, x + paramAlpha, y + paramAlpha)
        draw_spiral(paramAlpha, paramLg - 2*paramAlpha, x + paramAlpha, y + paramAlpha)
    canvas.grid(column=2, row=2, padx=1, pady=1)

def draw():
    canvas.delete('all')
    paramAlpha=int(editAlpha.get())
    paramLg=int(editLg.get())
    print(paramLg, paramAlpha)
    draw_spiral(paramAlpha, paramLg, 5, 5)

drawBtn = Button(window, text=' Draw ', command=draw)
drawBtn.grid(column=0, row=0)
window.mainloop()