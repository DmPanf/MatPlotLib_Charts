#@title Plotting colors 
import matplotlib.pyplot as plt      # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
import matplotlib.colors as mcolors  # https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.html
import numpy as np                   # https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
import math                          # https://docs.python.org/3/library/math.html 


# Plotting a color palette in a square grid 
def plot_optimized_color_palette():
    # create a dictionary of color names and their hex values 
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    sorted_colors = {name: color for name, color in sorted(colors.items(), key=lambda x: x[0])}
    n = len(sorted_colors)
    print(f'\nSorted colors: {n}\n')  

    # calculate number of rows and columns 
    # ncols = math.ceil(math.sqrt(n))
    ncols = 9
    nrows = math.ceil(n / ncols)  # calculate the number of rows based on the number of colors

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols*4, nrows),
                             subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
    
    axes = axes.flatten() # flatten the axes array to make it easier to iterate over 
    
    for ax, (name, color) in zip(axes, sorted_colors.items()):
        ax.add_patch(plt.Rectangle([0, 0], 1, 1, color=color))
        ax.annotate(name, xy=(0.5, 0.5), color='black' if name not in ['black', 'navy'] else 'white',
                    weight='bold', size=20, ha='center', va='center')
        
    plt.tight_layout()  # adjust the spacing between subplots 
    plt.savefig(f"colors_{n}.png", facecolor=fig.get_facecolor()) # save the figure
    plt.show()

plot_optimized_color_palette()
