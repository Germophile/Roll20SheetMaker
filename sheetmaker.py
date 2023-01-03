import tkinter as tk
import tksvg
from tkhtmlview import HTMLLabel as HL

root = tk.Tk()
root.title('Sheetmaker')
root.geometry("1200x800")

frame_left = tk.Frame(root)
frame_left.grid(row=0,column=0, sticky=tk.W)
frame_right = tk.Frame(root)
frame_right.grid(row=0,column=1)
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=1,column=0)
frame_bottom = tk.Frame(root)
frame_bottom.grid(row=2,column=0)

left_rows = []

class Section:
    def __init__(self,name):
        self.name = name
        self.frame = tk.Frame(frame_left)
        self.frame.grid(row=len(left_rows),column=0, sticky=tk.W)
        self.header_label = tk.Label(self.frame, text=self.name,font=("Arial",20))
        self.header_label.grid(row=0,column=0, sticky=tk.W)

def enterButton():
    global section_name_entry
    global enter_button
    global left_rows
    header_text = section_name_entry.get()
    section_name_entry.delete(0,'end')
    section_name_entry.grid_forget()
    enter_button.grid_forget()
    left_rows.append(Section(header_text))

def sectionButton():
    global section_name_entry
    global enter_button
    section_name_entry.grid(column=0,row=102)
    enter_button.grid(column=0,row=103)

section_name_entry = tk.Entry(frame_bottom)
enter_button = tk.Button(frame_bottom,text="Add", command=enterButton)

options = [tk.Button(frame_buttons,text="Section",command=sectionButton),
    tk.Button(frame_buttons,text="Attribute"),
    tk.Button(frame_buttons,text="Text Field")]
for x in range(len(options)):
    options[x].grid(column=x,row=0)


root.mainloop()

'''add_button_image = tksvg.SvgImage(file="Images\Add.svg")
add_button_image.configure(scale=0.35)

add_button_active = False
def add(add_button_active):
    if(add_button_active):
        add_button_active = False
    else:
        add_button_active = True
        options = [tk.Button(root,text="Section").grid(column=0,row=101),
            tk.Button(root,text="Attribute").grid(column=1,row=101),
            tk.Button(root,text="Text Field").grid(column=2,row=101)]
        

add_button = tk.Button(root,image=add_button_image,highlightthickness = 0, bd = 0, command=lambda: add(add_button_active))
add_button.grid(column=1,row=100)'''