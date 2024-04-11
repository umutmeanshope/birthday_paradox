import random
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def main():

    MIN_PEOPLE = 2
    MAX_PEOPLE = 60
    TRIALS = 100000


    def generate_random_birthday():
        return random.randint(0, 365)


    def generate_n_birthdays(n):
        return [generate_random_birthday() for _ in range(n)]


    def compare(birthdays):
        unique_birthdays = set(birthdays)

        num_birthdays = len(birthdays)
        num_unique_birthdays = len(unique_birthdays)

        has_match = (num_birthdays != num_unique_birthdays)

        return has_match


    def calculate_probability(n):
        num_match = 0
        for _ in range(TRIALS):
            birthdays = generate_n_birthdays(n)
            has_match = compare(birthdays)
            if has_match:
                num_match += 1

        probability = num_match / TRIALS
        return probability

    def calculate_probability_for_range(n_list):
        n_probabilities = []
        for n in n_list:
            probability = calculate_probability(n)
            n_probabilities.append(probability)

        return n_probabilities


    ns = range(MIN_PEOPLE, MAX_PEOPLE + 1)
    n_probabilities = calculate_probability_for_range(ns)

    fig, ax = plt.subplots()
    ax.plot(ns, n_probabilities)

    y_range = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    plt.yticks(y_range)

    plt.xlabel("Number of People")
    plt.ylabel("Probability")

    plt.show()



if __name__ == '__main__':
    main()
