"""
This script generates a plot of
some triangles.
"""

import matplotlib.pyplot as plt

def plot_triangle(points, ax=None):
    if ax is None:
        ax = plt.gca()
    else:
        fig, ax = plt.subplots()
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    patch = plt.Polygon(points)
    ax.add_patch(patch)

    for pt in points:
        x, y = pt
        ax.text(x, y, '({}, {})'.format(x, y))

if __name__ == "__main__":

    plot_triangle([
        (0.2, 0.2),
        (0.2, 0.6),
        (0.4, 0.4)
    ])

    plot_triangle([
        (0.6, 0.8),
        (0.8, 0.8),
        (0.5, 0.5)
    ])

    plot_triangle([
        (0.6, 0.1),
        (0.7, 0.3),
        (0.9, 0.2)
    ])

    plt.savefig('../docs/images/triangle.png', transparent=True)
