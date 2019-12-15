from tkinter import *
from tkinter import messagebox
import os.path


class View:

    def __init__(self):
        self.Menu = None
        self.Selection = None
        self.user_inp = ''
        self.select = []

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

    def add_value(self):
        w = self.total_list.get(ACTIVE)
        self.mylist.insert(END, w)
        self.total_list.delete(ACTIVE)

    def remove_value(self):
        y = self.mylist.get(ACTIVE)
        self.total_list.insert(END, y)
        self.mylist.delete(ACTIVE)

    def scrollbar(self, List_of_epi):
        self.Selection = Tk()

        scrollbar = Scrollbar(self.Selection)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.total_list = Listbox(self.Selection, bg='linen',
                                  yscrollcommand=scrollbar.set, width=70)
        self.total_list.pack(side=LEFT, expand=1, fill=X)
        select = Button(self.Selection, text = 'Select', bg='gold',
                        command=self.select_choose)
        select.pack(side=RIGHT, fill=Y)
        self.mylist = Listbox(self.Selection, width=70, bg='linen')
        self.mylist.pack(side=RIGHT, expand=1, fill=X)
        Button(self.Selection, text='Remove', bg='red',
               command=self.remove_value).pack(side=RIGHT, fill=BOTH)
        Button(self.Selection, text='Select Episode', bg='green3',
               command=self.add_value).pack(side=RIGHT, fill=BOTH)

        for i in List_of_epi:
            string = 'Season: %s, Episode: %s, Title: %s'\
                     % (i['Season'], i['Episodes'], i['Title'])
            self.total_list.insert(END, string)
            self.total_list.pack()

        scrollbar.config(command=self.total_list.yview)

        self.Selection.mainloop()

        return self.select

    def select_choose(self):
        self.select = self.mylist.get(0, END)
        self.Selection.destroy()

    def save_choose(self):
        lis = []
        for i in rage(len(self.select)):
            if self.total_list[i].get() == 1:
                lis.append(i)
        c.Check_correct_selection(lis)
        self.Selection.destroy()

    def search(self):
        self.user_inp = self.user_inp.get()
        self.Menu.destroy()

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
        self.ac_path = os.path.join(str(path), str(filename)+'.csv')
        self.Dwindow.destroy()

    def error_view(self):
        self.Ewindow =Tk()
        label_1 = Label(self.Ewindow, text='Path is incorrect'
                        'Try again')
        label_1.pack()

        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

if __name__ == '__main__':
    x = View()
    x.error_NotFound()

        
