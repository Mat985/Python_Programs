import tkinter as tk
HEIGHT = 510 
WIDTH = 510

permx = None
permy = None
counter=0
window = tk.Tk()
canvas = tk.Canvas(width = WIDTH, height = HEIGHT, bg = 'white')
canvas.pack()

def game_map():
    x=5
    y=5
    for i in range(10):
        for i in range(10):
            canvas.create_rectangle(x,y,x+50,y+50)
            x+=50
        x=5
        y+=50
        
def level(coordinates):
    global permx, permy,counter
    if 5<coordinates.x<505 and 5<coordinates.y<505:
        if counter==0:
            x=((-5+coordinates.x)//50)*50+5
            permx = x
            y=((-5+coordinates.y)//50)*50+5
            permy = y
            canvas.create_rectangle(x,y,x+50,y+50, fill = 'blue')
            counter+=1        
        elif counter==1:
            counter=0
            y=((-5+coordinates.y)//50)*50+5
            x=((-5+coordinates.x)//50)*50+5
            if y>permy and x==permx:
                canvas.create_rectangle(x,permy,x+50,y+50, fill = 'blue')
            elif y<permy and x==permx:
                canvas.create_rectangle(x,permy,x+50,y, fill = 'blue')
            elif x>permx and y==permy:
                canvas.create_rectangle(permx,y,x+50,y+50, fill = 'blue')
            elif x<permx and y==permy:
                canvas.create_rectangle(permx,y,x,y+50, fill = 'blue')
            else:
                canvas.create_rectangle(permx,permy,permx+50,permy+50, fill = 'white')
        game_map()#we know how terrible this solution is we are just desperate thanks fo understanding (Matus and Timka, suppor team Radko) )
game_map()
canvas.bind('<Button-1>',level)
def export_canvas():
    canvas.postscript(file='canvas_image.ps', colormode='color')
export_button = tk.Button(window, text='Export Canvas', command=export_canvas)
export_button.pack()
window.mainloop()