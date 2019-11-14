import numpy as np 
import matplotlib.pyplot as plt 

class ChaosGame:
    """ Calculating fractal distributions of points based on n-gons and
        returning them as color coded scatter plots

        Parameters
        ----------
        n: size of n-gon (3 or above)
        r: ratio between previous point in a iterative manner to selected n-gon corner 
           default value: 0.5; range: (0, 1)


        Output
        ------
        fig.png

    """
    def __init__(self, n=3, r=0.5):
        self.n = n
        self.r = r
        

        # litt pussig error raise (2x)
        if r < 0 or 1 < r:
            raise ValueError(f"r must be between 0 and 1; r is {r}")

        if n <= 3:
            raise ValueError(f"n must be above at least 3; n is {n}")

        if not isinstance(n, int):
            raise TypeError(f"n must be of type integer; n is {type(n)}")

        
            




if __name__ == "__main__":
    test = ChaosGame()

