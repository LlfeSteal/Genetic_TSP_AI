import matplotlib.pyplot as plt


class GraphGenerator:

    def __init__(self, cities, max_distance=900):
        self.cities = cities
        self.max_distance = max_distance
        self.x_vector = []
        self.y_vector = []
        self.label_vector = []

    def create_graph(self):
        self.x_vector = []
        self.y_vector = []
        self.label_vector = []
        for city in self.cities:
            self.x_vector.append(city.get_x())
            self.y_vector.append(city.get_y())
            self.label_vector.append(str(city.get_name()))

    def display(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.max_distance)
        ax.set_ylim(0, self.max_distance)
        scatter = ax.scatter(self.x_vector, self.y_vector)
        for i, txt in enumerate(self.label_vector):
            ax.annotate(txt, (self.x_vector[i], self.y_vector[i]))
        plt.show()
