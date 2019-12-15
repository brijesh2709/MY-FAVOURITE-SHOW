import model
import view
import view2


class Control:
    def __init__(self):
        self.model = model.Model()
        self.view_1 = view.View()

    def choose_gui(self):
        if self.view_1.view_selection():
            self.view_1 = view2.View()
        self.run()

    def run(self):
        try:
            self.model.user_search(self.view_1.menu())
        except model.NotFoundError:
            self.view_1.error_NotFound()
            return

        self.model.select_epi = self.view_1.scrollbar(self.model.List_of_epi)
        self.model.storage()
        self.view_1.view_download()
        try:
            path = self.view_1.ac_path
            if len(path)>5:
                u = self.model.save_file(path)
                while u != 1:
                    self.view_1.error_view()
                    self.view_1.view_download()
                    try:
                        path = self.view_1.ac_path
                        u = self.model.save_file(path)
                    except:
                        exit()
        except:
            exit()

if __name__ == '__main__':
    x = Control()
    x.choose_gui()
