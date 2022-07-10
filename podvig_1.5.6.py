class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show is False:
            print("Отображение данных закрыто")
        else:
            print(*self.data)

    def show_graph(self):
        if self.is_show is False:
            print("Отображение данных закрыто")
        else:
            # str_data = ''
            # for i in self.data:
            #     str_data += str(i)
            #     str_data += ' '
            print('Графическое отображение данных:', *self.data)

    def show_bar(self):
        if self.is_show is False:
            print("Отображение данных закрыто")
        else:
            print('Столбчатая диаграмма:', *self.data)

    def set_show(self, fl_show=False):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = [8, 11, 10, -32, 0, 7, 18]

gr = Graph(data_graph)

gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()