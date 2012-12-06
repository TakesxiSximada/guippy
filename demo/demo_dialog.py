#! /usr/bin/env python
#-*- coding: utf-8 -*-
import Tkinter
from Tkinter import Button, Label, Radiobutton, Checkbutton, OptionMenu,\
    Entry, StringVar, IntVar, BooleanVar, Frame

class DemoDialog(Tkinter.Frame):
    def __init__(self, wname='guippy', master=None):
        Tkinter.Frame.__init__(self, master)
        self.master.title(wname)
        
        self.radio_value = IntVar()
        self.radio_values = {'test1': 0,
                             'test2': 1,
                             'test3': 2,
                             }
        
        self.check_values = {'test1': BooleanVar(),
                             'test2': BooleanVar(),
                             'test3': BooleanVar(),
                             }
        
        self.option_value = StringVar()
        self.entry_value = StringVar()
        self.result_value = StringVar()
        
        # widgets
        ff = Frame(self, bg='black').pack(side=Tkinter.TOP)
        for key, val in self.radio_values.iteritems():
            _r = Radiobutton(ff, text=key, variable=self.radio_value, 
                             value=val)
            _r.pack(side=Tkinter.LEFT)

        ff = Frame(self).pack(side=Tkinter.TOP)
        for key, val in self.check_values.iteritems():
            _w = Checkbutton(ff, text=key, variable=val)
            _w.pack(side=Tkinter.LEFT, anchor=Tkinter.S)

        

    def setup(self):
        checkbox = IntVar()
        

    def _setup(self):
        self.label('LABEL')
        self.button('BUTTON')
        self.radio('RADIO')
        self.check('CHECK')
        self.entry()
        self.option_menu()

    def label(self, text):
        _l = Tkinter.Label(self, text=text)
        _l.pack(side=Tkinter.LEFT)

    def button(self, text):
        _b = Tkinter.Button(self, text=text)
        _b.pack(side=Tkinter.LEFT)

    def radio(self, text):
        _r = Tkinter.Radiobutton(self, text=text)
        _r.pack(side=Tkinter.LEFT)
        
    def check(self, text):
        _c = Tkinter.Checkbutton(self, text=text)
        _c.pack(side=Tkinter.LEFT)

    def entry(self):
        _e = Tkinter.Entry(self)
        _e.pack(side=Tkinter.LEFT)

    def pulldown(self):
        _p = Tkinter.OptionMenu(self)
        _p.pack(side=Tkinter.LEFT)

    def option_menu(self):
        var = Tkinter.StringVar()
        _b = Tkinter.OptionMenu(self, var, 'A', 'B')
        _b.pack(side=Tkinter.LEFT)

def main():
    dialog = DemoDialog()
    dialog.pack()
    dialog.mainloop()

if __name__ == '__main__':
    main()
