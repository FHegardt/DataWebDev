import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageChops, ImageFont
import io
from ast import literal_eval

df = pd.read_csv('path.csv')
# Create the lists of locations for the two methods
l1, l2 = literal_eval(df.CheminOr.values[0]), literal_eval(df.CheminInit.values[0])
# Path using Algorithm 2: OR Tools by Google
x1, y1 = [i[0] for i in l1], [i[1] for i in l1]
# Path using the Algorithm 1 (Initial): Next closest location
x2, y2 = [i[0] for i in l2], [i[1] for i in l2]



# Plot
fig, ax = plt.subplots(2, figsize=(15,6))
ax[0].scatter(x1, y1, s=100, linewidths=3, c= 'orange')
ax[0].plot(x1, y1,'--', color = 'black')
for t, txt in enumerate(l1[:-1]):
    ax[0].annotate(t +1, (x1[t], y1[t]), size = 10, color = 'black')
ax[0].set(title = 'OR-Tool TSP Optimization Solution Route')

ax[1].scatter(x2, y2, s=100, linewidths=3, c= 'yellow')
ax[1].plot(x2, y2,'--', color = 'black')
for t, txt in enumerate(l2[:-1]):
    ax[1].annotate(t +1, (x2[t], y2[t]), size = 10, color = 'black')
ax[1].set(title = 'Next Closest Location Solution Route')
plt.show()


def fig2img(fig):
    # Convert a Matplotlib figure to a PIL Image and return it
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

list_gif = []

for step in range(len(l1)):
    # Chemin OR
    x1s, y1s = [i[0] for i in l1[:step]], [i[1] for i in l1[:step]]
    # Chemin Init
    x2s, y2s = [i[0] for i in l2[:step]], [i[1] for i in l2[:step]]

    # First method
    fig, ax = plt.subplots(2, figsize=(15,6))
    ax[0].scatter(x1, y1, s=100, linewidths=3, c= 'orange')
    ax[0].plot(x1s, y1s,'--', color = 'black')
    for t, txt in enumerate(l1[:-1]):
        ax[0].annotate(t +1, (x1[t], y1[t]), size = 10, color = 'black')
    ax[0].set(title = 'OR-Tool TSP Optimization Solution Route')
    ax[0].set_yticklabels([])
    ax[0].set_xticklabels([])
    
    # Second method
    ax[1].scatter(x2, y2, s=100, linewidths=3, c= 'yellow')
    ax[1].plot(x2s, y2s,'--', color = 'black')
    for t, txt in enumerate(l2[:-1]):
        ax[1].annotate(t +1, (x2[t], y2[t]), size = 10, color = 'black')
    ax[1].set(title = 'Next Closest Location Solution Route')
    ax[1].set_yticklabels([])
    ax[1].set_xticklabels([])
    # plt.show()

    img = fig2img(fig)
    list_gif.append(img)

list_gif[0].save('pages/image.gif',
           save_all=True, append_images=list_gif[1:], optimize=False, duration=500, loop=1)