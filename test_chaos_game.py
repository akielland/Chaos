import numpy as np 
import matplotlib.pyplot as plt 
import os
import chaos_game

def test_generate_ngon():

    test_instance = chaos_game.ChaosGame(8)
    plt.scatter(*zip(*test_instance._corners))
    plt.axis("equal")
    plt.show()


def test_starting_point():

    test_pick_starting_point = chaos_game.ChaosGame(5)
    N = 10000  # number of staring points in test

    X = np.empty((N, 2))
    for i in range(N):
        test_pick_starting_point._starting_point()
        X[i] = test_pick_starting_point.start_value
        
    plt.scatter(*zip(*X), s=0.2, marker=".")
    plt.axis("equal")
    plt.axis("off")
    plt.show()

def test_plot():
   # plot n-gons with 3 to 8 corners
    for n in range(3, 9):
        test_plot_ngon = chaos_game.ChaosGame(n)
        plt.subplot(3,2,n-2)
        test_plot_ngon.plot_ngon()
        plt.title(f"{n}-gon")
    plt.subplots_adjust(hspace = 1)
    plt.show()
 
def test_gradient_color():
    test = chaos_game.ChaosGame()
    test.iterate(100_000)
    test.show(True)

def test_savepng():
    test = chaos_game.ChaosGame()
    test.iterate(100_000)

    try:
        test.savepng("test fig.jpeg", True)
    except NameError:
        print("program recognize un-accepted file extension")

    try:
        test.savepng("test fig", True)
    except:
        print("not good")
    print("program add .png")

    try:
        test.savepng("test fig.png", True)
    except:
        print("not good")
    print("program recognize .png")


if __name__ == "__main__":
    # test_generate_ngon()
    # test_starting_point()
    # test_plot()
    # test_gradient_color()
    test_savepng()
    