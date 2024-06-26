import sys

from entities.SubjectCalculator import SubjectCalculator

sys.path.append("C:/Users/dorian/PycharmProjects/genetictsp_ia")
from GeneticTSP import GeneticTSP


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sum = 0
    for y in range(100):
        print("test : ", y)
        genetic_tsp = GeneticTSP(50, 50, 30, 1, 13, "test")
        for i in range(100):
            #print("generation : ", i)
            genetic_tsp.generate_new_population()
            #print("best : ", str(genetic_tsp.get_best_subjects(1)),
                  #SubjectCalculator.evaluate(genetic_tsp.get_best_subjects(1)))
        genetic_tsp.display_population_status()
        #print("-----------------------------------------------------------")
        genetic_tsp.display_population_score()
        best_score = SubjectCalculator.evaluate(genetic_tsp.get_best_subjects(1))
        #print("best : ", str(genetic_tsp.get_best_subjects(1)),
              #best_score)
        sum += best_score
        genetic_tsp.display_graph(genetic_tsp.get_best_subjects(1))
    print("sum test : ", sum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
