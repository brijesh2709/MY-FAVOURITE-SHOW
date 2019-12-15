from tkinter import *
from tkinter import messagebox
import os.path


class View:
    def __init__(self):
        self.view_sel = None
        self.Menu = None
        self.Selection = None
        self.user_inp = ''
        self.select =[]
        self.view_1 = None

    def view_selection(self):
        self.view_sel = Tk()
        Label(self.view_sel, text='Select your prefer type of GUI').pack()

        Button(self.view_sel, text='GUI 1',
               command=self.gui_1).pack()
        Button(self.view_sel, text='GUI 2',
               command=self.gui_2).pack()

        self.view_sel.mainloop()
        return  self.view_1

    def gui_1(self):
        self.view_1 = False
        self.view_sel.destroy()

    def gui_2(self):
        self.view_1 = True
        self.view_sel.destroy()

    def menu(self):
        self.Menu = Tk()
        self.Menu.title('TV SHOW SEARCH')
        message = Label(self.Menu, text='Enter the search series:')
        self.user_inp = Entry(self.Menu)
        search_button = Button(self.Menu, text='Search', command=self.search)


        message.grid(row=0, column=0)
        self.user_inp.grid(row=0, column=1)
        search_button.grid(row=1, column=0)

        self.Menu.mainloop()

        return self.user_inp

    def search(self):
        self.user_inp = self.user_inp.get()
        self.Menu.destroy()

    def scrollbar(self, List_of_epi):
        self.Selection = Tk()

        scrollbar = Scrollbar(self.Selection)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.select = Listbox(self.Selection, selectmode=MULTIPLE,
                              yscrollcommand=scrollbar.set, width=70)
        

        for i in List_of_epi:
            string = 'Season: %s, Episode: %s, Title: %s'\
                     % (i['Season'], i['Episodes'], i['Title'])
            self.select.insert(END, string)
            self.select.pack()

        scrollbar.config(command=self.select.yview)
        select = Button(self.Selection, text='Select',
                        command=self.select_choose)
        select.pack()
        self.Selection.mainloop()

        return self.select

    def select_choose(self):
        selection = self.select.curselection()
        self.select = [self.select.get(i) for i in selection]
        self.Selection.destroy()

    def error_NotFound(self):
        window = Tk()
        window.withdraw()
        messagebox.showinfo('Error', 'Title either broad or not in database')

    def view_download(self):
        self.Dwindow = Tk()
        label_1 = Label(self.Dwindow, text = 'Filename')
        label_1.grid(row=1, column=0)
        self.filename = Entry(self.Dwindow, width = 60)
        self.filename.grid(row=1, column=1)
        label_2 = Label(self.Dwindow, text = 'Path')
        label_2.grid(row=2, column=0)
        self.path = Entry(self.Dwindow, width=60)
        self.path.grid(row=2, column=1)

        s_button = Button(self.Dwindow, text='Submit', command=self.get_path)
        s_button.grid(row=3, column=0)

        q_button = Button(self.Dwindow, text='Quit', command=self.Dwindow.destroy)
        q_button.grid(row=3, column=1)
        self.Dwindow.mainloop()

    def get_path(self):
        path = self.path.get()
        filename = self.filename.get()
        self.ac_path = os.path.join(str(path), str(filename)+'.txt')
        self.Dwindow.destroy()

    def error_view(self):
        self.Ewindow = Tk()
        label_1 = Label(self.Ewindow, text='Path is incorrect'
                        'Try again')
        label_1.pack()

        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

if __name__ == '__main__':
    x = View()
    x.view_selection()       
