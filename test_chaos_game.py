import numpy as np 
import matplotlib.pyplot as plt 
import os
import chaos_game

def test_generate_ngon():
    """ Test if n-gon is created correctly (her: 8-gon)."""
    test_instance = chaos_game.ChaosGame(8)
    plt.scatter(*zip(*test_instance._corners))
    plt.axis("equal")
    plt.show()


def test_starting_point():
    """ Test if starting points is randomely selectetd within the specified  n-gon (her: 5-gon)."""
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
    """ Plot n-gons with 3 to 8 corners."""
    for n in range(3, 9):
        test_plot_ngon = chaos_game.ChaosGame(n)
        test_plot_ngon.iterate(100_000)
        plt.subplot(3,2,n-2)
        test_plot_ngon.plot(True)
        plt.title(f"{n}-gon")
    plt.subplots_adjust(hspace = 1)
    plt.show()
 
def test_gradient_color():
    test = chaos_game.ChaosGame()
    test.iterate(100_000)
    test.show(True)


def test_savepng():
    """ Test if only png files can be generated."""
    test = chaos_game.ChaosGame()
    test.iterate(100_000)

    try:
        test.savepng("test fig.jpeg", True)
    except NameError:
        print("program recognize un-accepted file extension")

    try:
        test.savepng("test fig", True)
    except:
        print("the program should have handeld this by adding .png extension")
    print("program add .png correctely")

    try:
        test.savepng("test fig.png", True)
    except:
        print("the program should have recognized the .png extension")
    print("program recognize .png, as it should")


if __name__ == "__main__":
    # test_generate_ngon()
    # test_starting_point()
    # test_plot()
    # test_gradient_color()
    # test_savepng()
    pass