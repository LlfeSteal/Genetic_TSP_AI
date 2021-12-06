import sys

sys.path.append("C:/Users/dorian/PycharmProjects/genetictsp_ia")
from GeneticTSP import GeneticTSP


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    genetic_tsp = GeneticTSP(200, 1000, 30)
    for i in range(100):
        genetic_tsp.generate_new_population()
    genetic_tsp.display_population_status()
    print("best : ", str(genetic_tsp.get_best_subjects(1)))
    genetic_tsp.display_graph()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
