'''
CNA Intern
Study name: Chap03 Visualizing data
Created by Eunseo Cho on 03/05/2017.
'''

import matplotlib.pyplot as plt

def make_line():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # create line
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # title
    plt.title("GDP")

    # y-axis label
    plt.ylabel("Billios of $")
    plt.show()

def make_bar():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    
    # add 0.1 the left coordinates
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    
    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.bar(xs, num_oscars)
    plt.ylabel("# of Academy Awards")
    plt.title("My Favorite Movies")
    
    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)],movies)
    plt.show()




if __name__ == "__main__":
	make_line()
	make_bar()