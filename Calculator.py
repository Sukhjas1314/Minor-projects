from tkinter import *
import re

def love():
    class Calculator:
        def __init__(self,master):
            self.master = master
            master.title("Python Calculator")
            master.configure(bg = '#cb464e')

            self.screen = Text(master,state = 'disabled',width = 60,height = 3,background = '#fcfcec',foreground = '#cb464e',font = ("times",16,"bold"))

            self.screen.grid(row = 0,column = 0,columnspan = 4,padx = 5,pady = 5)
            self.screen.configure(state = 'normal')

            self.equation = ''

            b1 = self.createButton(7)
            b2 = self.createButton(8)
            b3 = self.createButton(9)
            b4 = self.createButton(u'\u232B',write = None)
            b5 = self.createButton(4)
            b6 = self.createButton(5)
            b7 = self.createButton(6)
            b8 = self.createButton(u'\u00F7')
            b9 = self.createButton(1)
            b10 = self.createButton(2)
            b11 = self.createButton(3)
            b12 = self.createButton('*')
            b13 = self.createButton('.')
            b14 = self.createButton(0)
            b15 = self.createButton('+')
            b16 = self.createButton('-')

            buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]

            count = 0
            for row in range(1,5):
                for column in range(4):
                    buttons[count].grid(row = row,column = column,padx = 2,pady = 2)
                    count += 1 

            equals_button = self.createButton('=',write = None,width = 34)
            equals_button.grid(row = 5,column = 0,columnspan = 4,padx = 2,pady = 5)

            self.master.bind('<Key>',self.key_input)
            self.master.focus_set()

        def createButton(self,val,write = True,width = 7):
            return Button(self.master,text = val,command = lambda: self.click(val,write),width = width,height = 2,background = '#4b7fa4',foreground = '#fcfcec',font = ("times",20))

        def click(self,text,write):
            if write is None:
                if text == '=' and self.equation:
                    self.equation = re.sub(u'\u00F7','/',self.equation)
                    try:
                        answer = str(eval(self.equation))
                        self.clear_screen()
                        self.insert_screen(answer,newline = True)
                    except Exception:
                        self.clear_screen()
                        self.insert_screen("Error",newline = True)
                elif text == u'\u232B':
                    self.clear_screen()

            else:
                self.insert_screen(text)

        def clear_screen(self):
            self.equation = ''
            self.screen.configure(state = 'normal')
            self.screen.delete('1.0',END)
            self.screen.configure(state = 'disabled')
        
        def insert_screen(self,value,newline = False):
            self.screen.configure(state = 'normal')
            self.screen.insert(END,str(value) + ('\n' if newline else ''))
            self.screen.configure(state = 'disabled')
            self.equation += str(value)

        def key_input(self,event):
            key = event.keysym
            if event.char in '0123456789.+-*/':
                self.insert_screen(event.char)
            elif key in ['Return','KP_Enter']:                       # Enter
                self.click('=',write = None)
            elif key == 'BackSpace':                     # Backspace
                self.backspace_last_char()

        def backspace_last_char(self):
            if self.equation:
                self.equation = self.equation[:-1]
                self.screen.configure(state='normal')
                self.screen.delete('1.0', END)
                self.screen.insert(END, self.equation)
                self.screen.configure(state='disabled')
                
    root = Tk()
    Calculator(root)
    root.mainloop()

love()
