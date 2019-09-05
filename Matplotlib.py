'''
@author Suraj Dakua
Matplotlib library is used for data visualization in Python
The name is inspired from MATLAB. 
'''
import matplotlib
import matplotlib.pyplot as plt   #plt is an alias to the library just to increase the efficiency of writing code.
matplotlib.pyplot.subplots_adjust(left=0.125, bottom=0.2, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.subplot(321)
plt.plot([1,2,3,4,5,68,7,9,11,10])
plt.ylabel('Numbers')
'''
Note here we haven't assigned any values for X-axis so it holds the value
of indices of the numbers of an array
'''
plt.xlabel('Indicies')
plt.title('My first Maplotlib Figure.')

'''
Plot the cube of the numbers.
Here we have two list the first list is X-axis and 
second list is the Y-axis.
'''
plt.subplot(322)
plt.plot([1,2,3,4,5],[1,8,27,64,125])
plt.xlabel('Numbers')
plt.ylabel('Cube of the Numbers')
plt.title('MyPlot with grid.')
'''
Grid makes it easier for the visitor to navigate through information.
'''
plt.grid()  #grid on.
# plt.show()

'''
View the same plot using dots instead of using the line.
This can be done simply shown below.
'''
#bo means blue dots of o "shaped".
plt.subplot(323)
plt.plot([1,2,3,4,5],[1,8,27,64,125], 'bo')  
plt.xlabel('Numbers')
plt.ylabel('Cube of the Numbers')
plt.title('MyPlot with grid and Blue Dots.')
plt.grid()
# plt.show()

'''
Matplotlib is fairly limited to working with lists so it is not great to work with numeric proccessing.
Using numpy we will generate array. 
Now lets plot different types of shapes.
And also show the index using the legend function of matplotlib.
Linewidth function to increase the width of line.
'''
import numpy as np 
numArr = np.arange(1,5, 0.3)
plt.subplot(324)
plt.plot(numArr, numArr**2, 'r--', label = '^2', linewidth = 4.0)  #r-- means red dash lines.
plt.plot(numArr,numArr**2.1, 'g^', label = '^2.1',linewidth = 5.0 )   #p^ means red triangle lines.
plt.plot(numArr,numArr**2.4, 'bs', label = '^2.4', linewidth = 3.0)   #bs means blue lines of square.
plt.title('Myplot with linewidth')
plt.xlabel('Numbers')
plt.ylabel('Exponent values.')
plt.grid()
plt.legend()   #add legend on lines labels.
# plt.show()

'''
Plot two plots in one plot i.e. x1,y1 and x2,y2
Lets see how it si done.
'''
x1 = [1,2,3,4]
y1 = [1,4,9,16]
x2 = [1,2,3,4]
y2 = [1,4,6,8]
plt.subplot(325)
lines = plt.plot(x1,y1,x2,y2)
plt.setp(lines[0], color='r',linewidth=3.0)
'''
In MATLAB way using pair values.
'''
plt.setp(lines[1], 'color','b', 'linewidth', 4.0)
plt.xlabel('Numbers')
plt.ylabel('Lines of Two axes')
plt.title('MyPlot with grid.')
plt.grid()
plt.show()  #Display the figure using the show() function.