# StarlingCycle-GUI
GUI developed in python and Tkinter. Generate Graphics, fit data to functions and use machine learning algorithms

This is a GUI developed in python and Tkinter where you can plot any functions you want. This GUI counts with 3 main functionalities:
1. Plotter
2. Fit equation
3. Machine learning algorithm

# Requirements

- python 3.7 or later
- install numpy 
- install csv
- install pandas 
- install re 
- install matplotlib 

**To run the application, run the MainExe.py file in the console.**

# Plotter Instruction
To open the plotter main window press the first button on the button bar. It will show you the following work window

![Image text](example1.png)

On the left side, you will find the fields to complete. The first entry  corresponds to the equation you want to plot.
Remember the following rules when you introduce an equation:
1. Always use x as variable
2. If there is an exponential, sin or cos, please always write the argument of the function between parenthesis, no matter its complexity. For example: e^(x) or sin(2x+5)
3. Please check how to write the different mathematical expressions in the next table.

![Image text](table.png)

The xi, xf, yi, yf fields allow you to set the extreme values of the axes of your plot. If you don't complete them, the default values will be from 0 to 100.
The frec field represents the number of samples to generate in the range [xi,xf]. The default value will be 100. 

In the style label frame you can configure the style plot (scatter or lineal), the color line and the name of the function. The default style plot is lineal and the default label is the equation. The color line doesn't have a default value, it will take a random color if you don't define it.
Using the button "save", you can save any functions you want and then plot them all together in a single graph using the "graph" button. The following picture shows you an example.

![Image text](example2.png)







