from matplotlib import markers
import pandas as pd
import random
from path_algo import main
from PIL import Image, ImageDraw, ImageChops, ImageFont
import matplotlib.pyplot as plt

def randomize_x_y(amount_coord):
    x = [random.randint(1, 20) for n in range(amount_coord)]
    y = [random.randint(1, 20) for n in range(amount_coord)]
    return x,y



def create_list_of_coord(x,y):
    l1 = []
    for i in range(len(x)):
        l1.append([x[i],y[i]])
        

    x1, y1 = [i[0] for i in l1], [i[1] for i in l1]
    
    return l1,x1,y1




def create_dataset(x,y, l1):
    no = [i for i in range(len(l1))]
    df = pd.DataFrame(columns=["no", "x", "y"])
    df["no"] = no
    df["x"] = x
    df["y"] = y
    return df



def get_new_x_y(dataset, x1, y1):
    arraye = main(dataset)    
    #create_new_x_y():
    new_x1 = []
    new_y1 = []

    for i in range(len(x1)):
        new_x1.append(x1[arraye[i]-1])
        new_y1.append(y1[arraye[i]-1])
    l5 = []
    for i in range(len(new_x1)):
        l5.append([new_x1[i],new_y1[i]])
    return new_x1, new_y1, l5

def fig2img(fig):
    # Convert a Matplotlib figure to a PIL Image and return it
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

def create_list_gif(x1,y1,new_x1,new_y1,l1):

    list_gif_both = []

    for step in range(len(l1)+1):
        x5s, y5s = [i[0] for i in l1[:step]], [i[1] for i in l1[:step]]
        fig, ax = plt.subplots(1, figsize=(15,7))
        ax.scatter(x1, y1, s=200, linewidths=5,  c= 'grey', alpha=0.7, marker="x")

        # First method
        ax.plot(x5s, y5s,'--', color = 'purple')
        for t, txt in enumerate(l1[:step]):
            ax.annotate(t +1, (new_x1[t], new_y1[t]), size = 20, color = 'purple')
        #ax.set_title(label = 'Shortest path algorithm', fontdict = {'fontsize' : 23})
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.axis('off')
        

        img = fig2img(fig)
        list_gif_both.append(img)
    return list_gif_both