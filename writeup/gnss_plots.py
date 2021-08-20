import numpy as np
import pylab

from crover_challenge.gnss import RollingMean
from crover_challenge.core import interpolate_points, reduce
from analysis import *


def show_smoothened(n):
    """Calculate, plot and evaluate the effect of rolling average smoothing on
    GNSS data.
    """
    mean = RollingMean(n)

    # Stream the values into the rolling mean. Log the means.
    points = np.empty((len(gnss), 2))
    for (i, xy) in enumerate(gnss[:, [1, 2]]):
        points[i] = mean.new_value(xy)

    error = position_error(points, gnss[:, 0])

    if n:
        pylab.title(
            f'GNSS position, "last {n}" rolling average. '
            f'Mean error: {error:.3f}')
        path(points, color="r", label="GNSS")
    else:
        pylab.title(f"Raw GNSS position vs real position. "
                    f"Mean error: {error:.3f}")
        path(points, color="r", label="GNSS")
    path(ground_truth[:, [1, 2]], label="Ground Truth", color="c")

    pylab.legend()
    pylab.xlabel("$x$")
    pylab.ylabel("$y$")

    pylab.show()