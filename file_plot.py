import matplotlib.pyplot as plt
import sys
import os
def plot_from_file(fname, width=1, height=1, i=1):
    xs = []
    ys = []
    f = open(fname, 'r+')
    for line in f.readlines():
        print(line)
        x,y = list(map(float, line.split(',')))
        xs.append(x)
        ys.append(y)
    plt.subplot(width, height, i)
    plt.hist2d(xs, ys, (100, 100), cmap=plt.cm.jet)
    plt.title("%s HEATMAP" % fname.upper())

def plot_from_classes(classlist):
    j = 1
    for cls in classlist:
        path = os.path.join(os.getcwd(), cls)
        for f in os.listdir(path):
            if f.endswith('.txt'):
                plot_from_file(os.path.join(path, f), width=len(classlist), i=j) 
        j += 1

# Usage --> python3 file_plot.py C:/path/to/file.txt
plot_from_file(fname=sys.argv[1])
plot_from_classes(['cubic', 'flat', 'round'])
plt.show()
