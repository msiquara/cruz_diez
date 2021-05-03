import aggdraw
from PIL import Image
import random
import Tkinter

def cor():
    n = []
    for i in range(3):
        n += [random.randint(0, 255)]
    cor = (n[0], n[1], n[2])
    
    return cor


root = Tkinter.Tk()

size = 2000, 2000
linhas = 5

# create a Dib surface
img = Image.new("RGB", size, "black")
draw = aggdraw.Draw(img)
#"aggdraw.Dib("RGB", (1000, 1000), "black")

'''
##### 4 QUADRADOS #####

random_colorQ1 = cor()
random_colorQ2 = cor()
random_colorQ3 = cor()
random_colorQ4 = cor()

random_colorQ5 = cor()
random_colorQ6 = cor()
random_colorQ7 = cor()
random_colorQ8 = cor()

random_colorQ9 = cor()
random_colorQ10 = cor()
random_colorQ11 = cor()
random_colorQ12 = cor()

random_colorQ13 = cor()
random_colorQ14 = cor()
random_colorQ15 = cor()
random_colorQ16 = cor()

i = 0
while i < 500:
    draw.line((i, 0, (i+4), 500), aggdraw.Pen(random_colorQ1,4))
    draw.line(((i+8), 0, (i+12), 500), aggdraw.Pen(random_colorQ2,4))
    draw.line(((i+4), 0,(i+8), 500), aggdraw.Pen(random_colorQ3,4))
    draw.line((i, 0, i, 500), aggdraw.Pen(random_colorQ4,4))
    i += 12
    
i = 500
while i < 1000:
    draw.line((i, 0, (i+4), 500), aggdraw.Pen(random_colorQ5,4))
    draw.line(((i+8), 0, (i+12), 500), aggdraw.Pen(random_colorQ6,4))
    draw.line(((i+4), 0,(i+8), 500), aggdraw.Pen(random_colorQ7,4))
    draw.line((i, 0, i, 500), aggdraw.Pen(random_colorQ8,4))
    i += 12

i=0
while i < 500:
    draw.line((i, 500, (i+4), 1000), aggdraw.Pen(random_colorQ9, 4))
    draw.line(((i+8), 500, (i+12), 1000), aggdraw.Pen(random_colorQ10, 4))
    draw.line(((i+4), 500,(i+8), 1000), aggdraw.Pen(random_colorQ11, 4))
    draw.line((i, 500, i, 1000), aggdraw.Pen(random_colorQ12,4))
    i += 12
    
i = 500
while i < 1000:
    draw.line((i, 500, (i+4), 1000), aggdraw.Pen(random_colorQ13,4))
    draw.line(((i+8), 500, (i+12), 1000), aggdraw.Pen(random_colorQ14,4))
    draw.line(((i+4), 500,(i+8), 1000), aggdraw.Pen(random_colorQ15,4))
    draw.line((i, 500, i, 1000), aggdraw.Pen(random_colorQ16,4))
    i += 12

##### QUADRADO 45o #####

random_colorQ1 = cor()
random_colorQ2 = cor()
random_colorQ3 = cor()
random_colorQ4 = cor()

i = 0
while i < 1000:
    draw.line((i, 0, (i+3), 1000), aggdraw.Pen(random_colorQ1, 3))
    draw.line(((i+6), 0, (i+9), 1000), aggdraw.Pen(random_colorQ2, 3))
    draw.line(((i+3), 0,(i+6), 1000), aggdraw.Pen(random_colorQ3, 3))
    draw.line((i, 0, i, 1000), aggdraw.Pen(random_colorQ4, 3))
    i += 9

i = 500
j = 2
k = 2
l = 500
random_colorQ5 = cor()

while i < 1000:
    draw.line((i, j, k, l), aggdraw.Pen(random_colorQ5, 10))
    #draw.line(((i+6), 0, (i+9), 1000), aggdraw.Pen(random_colorQ6, 3))
    #draw.line(((i+3), 0,(i+6), 1000), aggdraw.Pen(random_colorQ7, 3))
    #draw.line((i, 0, i, 1000), aggdraw.Pen(random_colorQ8, 3))
    i += 25
    j += 25
    k += 25
    l += 25
'''

##### 3 RETANGULOS #####

random_colorQ1 = cor()
random_colorQ2 = cor()
random_colorQ3 = cor()
#grena (120,30,42)

i = (size[0] * 0.27)
j = (size[1] * 0.09)
while i < (size[0] * 0.675):
    draw.line((i, 0, j, size[1]), aggdraw.Pen(random_colorQ1, linhas))
    i += 15
    j += 15

i = (size[0] * 0.422)
j = (size[1] * 0.278)
while i < (size[0] * 0.785):
    draw.line((i, (size[1] * 0.1), j, (size[1] * 0.9)), aggdraw.Pen(random_colorQ2, linhas))
    i += 15
    j += 15

i = (size[0] * 0.544)
j = (size[1] * 0.436)
while i < (size[0]* 0.910):
    draw.line((i, (size[1] * 0.2), j, (size[1] * 0.8)), aggdraw.Pen(random_colorQ3, linhas))
    i += 15
    j += 15
'''   
# display the image
frame = Tkinter.Frame(root, width=1000, height=1000, bg="")
frame.bind("<Expose>", lambda e: draw.expose(hwnd=e.widget.winfo_id()))
frame.pack()


frame.mainloop()
'''

draw.flush()
img.save("cruzdiez.png", "PNG")
img.show("cruzdiez.png")
