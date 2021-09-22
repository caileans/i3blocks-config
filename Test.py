from tkinter import *
from tkinter.ttk import Combobox
import gi

window=Toplevel()
window.config(bg='red')
# window.attributes('-type', '')
# window.focusmodel('active')
# window.tk.call('wm', 'attributes', window._w, '-disabled', 'true')
window.geometry("200x100+100+100")
# window.attributes('-fullscreen', 0)
# window.overrideredirect(1)
window.wm_state("normal")
# window.focus_set()
# window.focus_force()
# window.focus_set()

# window.update_idletasks()
# window.withdraw()
# window.forget(window)

def getTLPCurrent(modes):
    return 0
otherInFocus = False
def otherFocusIn (event):
    otherInFocus = True
    # print("Other in focus")
    print(window.focus_get())

def otherFocusOut (event): 
    otherInFocus = False
    # print("Other out focus")
    print(window.focus_get())


TLPModes = ("on (BAT)", "on (AC)", "off")
combo_TLPMode=Combobox(window, values=TLPModes)
combo_TLPMode.current(getTLPCurrent(TLPModes))
combo_TLPMode.place(x=0, y=50)
# window.bind("<Enter>", otherFocusIn)
# window.bind("<Leave>", otherFocusOut)
# window.tk.call('tk_focusFollowsMouse')

# window.focus_force()
# window.focus_set()

def onFocusOut(event):
    if event.widget is window:
        w = window.tk.call('focus')
        print(w)
        window.config(bg='orange')
        if w is None:
            window.config(bg='red')
    else:
        print("focus_forced")
def onFocusIn (event):
    window.config(bg="blue")
# window.bind("<FocusIn>", onFocusIn)
# window.bind("<FocusOut>", onFocusOut)

# print(window.focus_get())


# window.bind("<Enter>", lambda event: event.widget.config(bg="navy"))
# window.bind("<Leave>", lambda event: window.destroy())

# lb=Listbox(window, height=5, selectmode='multiple')
# for num in data:
#     lb.insert(END,num)
# lb.place(x=250, y=150)

# v0=IntVar()
# v0.set(1)
# r1=Radiobutton(window, text="male", variable=v0,value=1)
# r2=Radiobutton(window, text="female", variable=v0,value=2)
# r1.place(x=100,y=50)
# r2.place(x=180, y=50)
                
# v1 = IntVar()
# v2 = IntVar()
# C1 = Checkbutton(window, text = "Cricket", variable = v1)
# C2 = Checkbutton(window, text = "Tennis", variable = v2)
# C1.place(x=100, y=100)
# C2.place(x=180, y=100)

# window.title('Hello Python')
# window.geometry("200x100+100+100")

# window.withdraw()
# window.deiconify()
# window.lift()

window.mainloop()