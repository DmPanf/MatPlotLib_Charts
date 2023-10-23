#@title Seaborn Color Palettes
import seaborn as sns
import matplotlib.pyplot as plt
# https://seaborn.pydata.org/generated/seaborn.color_palette.html

palettes = ["deep", "muted", "bright", "pastel", "dark", "colorblind", "husl", "coolwarm", "RdBu", "viridis"]

fig, axes = plt.subplots(len(palettes), 1, figsize=(10, len(palettes)))
rect_height = 1

for ax, pal in zip(axes, palettes):
    palette = sns.color_palette(pal, 18)

    for i, color in enumerate(palette):
        rect = plt.Rectangle((i, 0.5 - rect_height / 2), 1, rect_height, facecolor=color)
        ax.add_patch(rect)

    ax.set_xlim(0, len(palette))
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(-2, 0.5, f"Palette: {pal}", verticalalignment='center')

plt.tight_layout(pad=0.2)
plt.show()
