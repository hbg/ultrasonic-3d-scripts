import matplotlib.pyplot as plt
import numpy as np
import os
ultrasonic_std_dev = 15
rounded_object = lambda x: 0.16*(x-50)**2
flat_object = lambda y: 400
cubic = lambda x: 0.002*(x-25)*(x-50)*(x-75) + 200
sin = lambda x: 100*np.sin(1/10*np.pi*x) + 400
fig = plt.figure()
axes = fig.subplots(nrows=2, ncols=2)
plt.xlabel("X Distance (cm)")
plt.ylabel("Y Distance (cm)")

def plot(functions, names, width, height):
    if len(functions) != len(names) or len(names) != width*height:
        # To prevent errors in subplotting
        raise Exception("Fix the dimensions of the subplots to match the number of functions and names.")
    for i in range(1, width*height+1):
        x, y = gen_points(functions[i-1], names[i-1]) 
        plt.subplot(width, height, i)
        plt.hist2d(x, y, (100, 100), cmap=plt.cm.jet)
        plt.title("%s HEATMAP" % names[i-1].upper())

def gen_points(func, folder, g=0):
    points = []
    points_x = []
    coords = []
    dx = 1
    for x in range(0, 100, dx):
        y = func(x)
        distribution = np.random.normal(y, ultrasonic_std_dev, 5000).tolist()
        points.extend(list(map(int, distribution)))
        points_x.extend([x for i in range(0, 5000)])
        coords.extend([[x, distribution[i]]for i in range(0, 5000)])
    fpath = os.path.join(os.getcwd(),folder,'%s.txt' % g)
    f = open(fpath, 'w+')
    c_s = list(map(lambda a: ','.join(list(map(str, a))), coords))
    f.write(str('\n'.join(c_s)))
    f.close()
    return points_x, points

plot_from_file('coords.txt')
# plot(functions=[rounded_object, flat_object, cubic, sin], names=["round","flat", "cubic", "sin"], width=2, height=2)
plt.show()
