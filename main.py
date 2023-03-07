from functions import sorting_methods as sm
from complexity import executionTime as et
import matplotlib.pyplot as mlt
import numpy as np

if __name__ == "__main__":
    array = et.take_execution_time(1000, 10000, 500, 5)
    xpoints = []
    ypoints = []
    for row in array:
        print(row)
        xpoints += [row[3]]
        ypoints += [row[0]]

    mlt.plot(xpoints, ypoints)
    mlt.show()
