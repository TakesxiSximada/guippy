#! /usr/bin/env python
#-*- coding: utf-8 -*-
import Tkinter
from Tkinter import Button, Label, Radiobutton, Checkbutton, OptionMenu,\
    Entry, StringVar, IntVar, BooleanVar, Frame, LabelFrame

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
        
        self.radio_entry = StringVar()
        self.check_entry = StringVar()

        # widgets
        kwds = {'padx':3, 'pady': 3, 'side': Tkinter.LEFT}
        ff = Frame(self)
        ff.pack(side=Tkinter.TOP, anchor='w')
        Button(ff, text='apply  ', command=self.apply).pack(**kwds)
        Button(ff, text='reapply').pack(**kwds)


        ff = Frame(self)
        ff.pack(side=Tkinter.TOP, anchor='w')
        for key, val in sorted(self.radio_values.items()):
            _r = Radiobutton(ff, text=key, variable=self.radio_value, value=val)
            _r.pack(**kwds)
        Entry(ff, textvariable=self.radio_entry).pack(**kwds)

        ff = Frame(self)
        ff.pack(side=Tkinter.TOP, anchor='c')
        for key, val in sorted(self.check_values.items()):
            _w = Checkbutton(ff, text=key, variable=val)
            _w.pack(**kwds)
        Entry(ff, textvariable=self.check_entry).pack(**kwds)
        
    def apply(self):
        radio_val = self.radio_value.get()
        for key, value in self.radio_values.iteritems():
            if value == radio_val:
                self.radio_entry.set(key)

        words = [key for key, value in sorted(self.check_values.items())
                 if value.get()]
        line = ', '.join(words)
        self.check_entry.set(line+'a')

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
