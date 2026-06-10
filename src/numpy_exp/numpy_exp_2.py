"""
https://www.w3schools.com/python/numpy/numpy_random.asp
"""
import os

import numpy as np
from numpy import random
import matplotlib
# matplotlib.use('agg')  # to avoid "tkinter.TclError: couldn't connect to display ..."
matplotlib.use('qtagg')     # use pyqt (pip install pyqt6) with antigrain (agg) rendering;
# - to avoid "tkinter.TclError: couldn't connect to display ...", at "plt.show()"
# - to open the figures interactively

from matplotlib import pyplot as plt
import seaborn as sns  # https://seaborn.pydata.org/api.html


OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def random_v1():

    # Random numbers generated through a generation algorithm are called pseudo random.
    # In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
    x = random.randint(100)  # int from [0,100]
    print(x)

    x = random.randint(100, size=(5)) # 1-D array of 5 ints [0,100]
    print(x)
    x = random.randint(100, size=(3, 5))  # with 2-D array
    print(x)

    x = random.rand()  # float [0., 1.]
    print(x)

    x = random.rand(5)  # 1-D array with 5 floats [0.,1.]
    print(x)
    x = random.rand(3, 5)  # with 2-D array
    print(x)

    x = random.choice([3, 5, 7, 9])  # selection from the array
    print(x)
    x = random.choice([3, 5, 7, 9], size=(3, 5))
    print(x)
    # 80
    # [27 46 68 81  3]
    # [[86 84 34 17 74]
    #  [92 90 57 79 73]
    #  [98 49 29 50 54]]
    # 0.857845557902907
    # [0.09321411 0.46904792 0.45372279 0.9469369  0.59714665]
    # [[0.51720828 0.62698881 0.89880296 0.65137399 0.20768843]
    #  [0.66047012 0.59504668 0.12538108 0.90055728 0.01596098]
    #  [0.85870903 0.32406747 0.42200292 0.00617396 0.8604998 ]]
    # 9
    # [[7 5 3 7 5]
    #  [9 7 3 3 7]
    #  [5 3 5 7 3]]


def data_distribution_v1():
    # The random module offer methods that returns randomly generated data distributions.
    # A random distribution is a set of random numbers that follow a certain probability density function.
    # Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

    x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))  # with probabilities to the choices; The sum of all probability numbers should be 1.
    print(x)
    # [[5 5 7 7 3]
    #  [7 7 7 5 7]
    #  [5 7 3 5 7]]


def permutation_v1():
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    random.shuffle(arr)  # The shuffle() method makes changes to the original array.
    print(arr)

    arr = np.array([1, 2, 3, 4, 5])
    newarr = random.permutation(arr)  # The permutation() method returns a re-arranged array (and leaves the original array un-changed).
    print(newarr)
    # [1 2 3 4 5]
    # [2 1 4 5 3]
    # [5 2 3 1 4]


def seaborn_v1():

    """

    histplot
        Plot a histogram of binned counts with optional normalization or smoothing.
    kdeplot
        Plot univariate or bivariate distributions using kernel density estimation.
    rugplot
        Plot a tick at each observation value along the x and/or y axes.
    ecdfplot
        Plot empirical cumulative distribution functions.
    jointplot
        Draw a bivariate plot with univariate marginal distributions.

    """
    sns.displot([0, 1, 2, 3, 4, 5])  # kind="hist" per default
    #plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_seaborn_v1_hist.png"))

    sns.displot([0, 1, 2, 3, 4, 5], kind="kde")  # kind="kde":
                                                # further: kind="ecdf"
    #plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_seaborn_v1_kde.png"))


def distributions_v1():

    x = random.normal(size=(2, 3))
    print(x)

    # Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2
    x = random.normal(loc=1, scale=2, size=(2, 3))
    print(x)
    # [[-0.44719889  0.91456509  0.62375875]
    #  [-0.10830654  1.02253348 -1.61078606]]
    # [[ 1.04519575 -1.49754443 -1.29239281]
    #  [ 0.95052119  0.24895882  0.60050998]]

    sns.displot(random.normal(size=1000), kind="kde", rug=True)
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_normal_kde.png"))

    # Binomial Distribution is a Discrete Distribution.
    # It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
    # It has three parameters:
    # n - number of trials.
    # p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
    # size - The shape of the returned array.
    x = random.binomial(n=10, p=0.5, size=10)
    print(x)
    # [4 4 4 5 6 5 7 7 8 6]

    sns.displot(random.binomial(n=10, p=0.5, size=1000))
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_binomial_hist.png"))

    # difference btw normal and binomial
    data = {
        "normal": random.normal(loc=50, scale=5, size=1000),
        "binomial": random.binomial(n=100, p=0.5, size=1000),
    }
    sns.displot(data, kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_normal+binomial_kde.png"))

    # Poisson Distribution is a Discrete Distribution.
    # It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
    # It has two parameters:
    # lam - rate or known number of occurrences e.g. 2 for above problem.
    # size - The shape of the returned array.

    # Generate a random 1x10 distribution for occurrence 2
    x = random.poisson(lam=2, size=10)
    print(x)
    # [2 2 1 2 5 0 2 0 5 4]

    sns.displot(random.poisson(lam=2, size=1000))
    # plt.show()
    plt.savefig(
        os.path.join(OUTPUT_DIR, "np2_distributions_v1_poisson_hist.png")
    )

    # Normal distribution is continuous whereas poisson is discrete.
    # But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.
    data = {
        "normal": random.normal(loc=50, scale=7, size=1000),
        "poisson": random.poisson(lam=50, size=1000),
    }
    sns.displot(data, kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_normal+poisson_kde.png"))

    # Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.
    # But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.
    data = {
        "binomial": random.binomial(n=1000, p=0.01, size=1000),
        "poisson": random.poisson(lam=10, size=1000),
    }
    sns.displot(data, kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_binomial+poisson_kde.png"))

    # Uniform Distribution
    # Used to describe probability where every event has equal chances of occuring.
    # E.g. Generation of random numbers.
    # It has three parameters:
    # low - lower bound - default 0.0
    # high - upper bound - default 1.0
    # size - The shape of the returned array
    x = random.uniform(size=(2, 3))
    print(x)
    # [[0.27022174 0.09267271 0.39780614]
    #  [0.17606987 0.66137292 0.67850878]]

    sns.displot(random.uniform(size=1000), kind="kde")
    # plt.show()
    plt.savefig(
        os.path.join(OUTPUT_DIR, "np2_distributions_v1_uniform_kde.png")
    )

    # Logistic Distribution is used to describe growth.
    # Used extensively in machine learning in logistic regression, neural networks etc.
    # It has three parameters:
    # loc - mean, where the peak is. Default 0.
    # scale - standard deviation, the flatness of distribution. Default 1.
    # size - The shape of the returned array.
    x = random.logistic(loc=1, scale=2, size=(2, 3))
    print(x)
    # [[ 4.83224978  3.67671731 -4.37275028]
    #  [ 3.67611806  5.77960385 11.38168189]]

    sns.displot(random.logistic(size=1000), kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_logistic_kde.png"))

    # Difference Between Logistic and Normal Distribution
    # Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
    # For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.
    data = {
      "normal": random.normal(scale=2, size=1000),
      "logistic": random.logistic(size=1000)
    }
    sns.displot(data, kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_normal+logistic_kde.png"))

    # Multinomial distribution is a generalization of binomial distribution.
    # It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
    # It has three parameters:
    # n - number of times to run the experiment.
    # pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
    # size - The shape of the returned array.
    # Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.
    # Note: As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions.
    x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    print(x)
    # [1 0 1 2 1 1]

    sns.displot(x, kind="hist")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_multinomial_hist.png"))
    sns.displot(x, kind="kde", rug=True)
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_multinomial_kde.png"))

    # Exponential distribution is used for describing time till next event e.g. failure/success etc.
    # It has two parameters:
    # scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
    # size - The shape of the returned array.
    x = random.exponential(scale=2, size=(2, 3))
    print(x)
    # [[2.15173988 0.95508508 1.26032079]
    #  [4.00858023 0.29318224 1.98332771]]

    sns.displot(random.exponential(size=1000), kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_exponential_kde.png"))

    # Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.

    # Chi Square distribution is used as a basis to verify the hypothesis.
    # It has two parameters:
    # df - (degree of freedom).
    # size - The shape of the returned array.
    x = random.chisquare(df=2, size=(2, 3))
    print(x)
    # [[0.76207702 0.07321237 0.06751783]
    #  [4.27567562 2.67835195 4.86906447]]

    sns.displot(random.chisquare(df=1, size=1000), kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_chisquare_kde.png"))

    # Rayleigh distribution is used in signal processing.
    # It has two parameters:
    # scale - (standard deviation) decides how flat the distribution will be default 1.0).
    # size - The shape of the returned array.
    x = random.rayleigh(scale=2, size=(2, 3))
    print(x)
    # [[2.2297824  2.21313172 1.75088122]
    #  [4.1714206  1.2101644  2.19657824]]

    sns.displot(random.rayleigh(size=1000), kind="kde")
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_rayleigh_kde.png"))

    # Similarity Between Rayleigh and Chi Square Distribution
    # At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions.
    data = {
        "rayleigh": random.rayleigh(scale=1, size=1000),  # ?? EMM trial, but not the same...
        "chisquare": random.chisquare(df=2, size=1000),
    }
    sns.displot(data, kind="kde")
    # plt.show()
    plt.savefig(
        os.path.join(OUTPUT_DIR, "np2_distributions_v1_chisquare+rayleigh_kde.png")
    )

    # A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
    # It has two parameter:
    # a - shape parameter.
    # size - The shape of the returned array.
    x = random.pareto(a=2, size=(2, 3))
    print(x)
    # [[1.40162426 2.01195938 1.60163987]
    #  [0.09263711 0.06982944 0.69499583]]

    sns.displot(random.pareto(a=2, size=1000))
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_pareto_hist.png"))

    # Zipf distributions are used to sample data based on zipf's law.
    # Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
    # It has two parameters:
    # a - distribution parameter.
    # size - The shape of the returned array.
    x = random.zipf(a=2, size=(2, 3))
    print(x)
    # [[ 1 17  3]
    #  [ 4  1  1]]

    x = random.zipf(a=2, size=1000)
    sns.displot(x[x < 10])  # Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.
    # plt.show()
    plt.savefig(os.path.join(OUTPUT_DIR, "np2_distributions_v1_zipf_hist.png"))


if __name__ == "__main__":
    # random_v1()
    # data_distribution_v1()
    # permutation_v1()
    # seaborn_v1()
    distributions_v1()
