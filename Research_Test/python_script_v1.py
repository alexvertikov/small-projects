import tkinter as tk
import csv

global line_number
line_number = 0




#We first want to create the visualization of the lines, using a list
#Each line is a dictionary (hashmap) which is an element of the list
#The key will be which intercept and the value is the ordered pair (which i think is a tuple?)

line_equations = [
    {"x-cept": (50, 0), "y-cept": (0, 70)},
    {"x-cept": (100, 0), "y-cept": (0, 80)},
    {"x-cept": (60, 0), "y-cept": (0, 60)}
]

#We want to have 3 rows (one for each question) and two columns (x and y intercept)

#We open the csv file that will serve as our excel spreadsheet of record

#file = open("excel.csv", mode="w", newline="")
 #I copied the following line from the csv documentation
#coordwriter = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#coordwriter.writerow(["Question", "x-coordinate", "y-coord"])

FILE_PATH = "/Users/alexvertikov/Desktop/Personal-Projects/Research_Test/"
with open(FILE_PATH + "excel.csv", mode = "w", newline="") as file:
    coordwriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    coordwriter.writerow(["Question", "x-coordinate", "y-coord"])


#We now want to determine how to allow the user to click on the line

#We want to limit their ability to click to be somewhere on the line,
#We also want to allow the use of arrow keys (based on the handout) to make more precise movements
def reaches_line():
    return True


####
#NOW WE FOCUS ON CREATING THE WINDOW WITH THE GRAPHS, WHERE WE WILL CLICK
####


#In tkinter, the main window of the application is below, which we instantiate
window = tk.Tk()

#Now we create the "canvas" in our window, which is what we can actually draw on
#We have width 1000 pixels, height 800 pixels, white background
canvas = tk.Canvas(window, width=500, height=500, bg="white")
#Not super sure what this does but it wasn't drawing without it
canvas.pack()

def draw_graph(graph_number):

    #We first want to wipe the canvas clean (like if there were previous graphs)
    canvas.delete("all")

    #We need to access each specific line (from our list line_equations)
    #For this, we access the line_number (0,1,2) which is an input to our function
    line = line_equations[graph_number]

    #In each line, we access the values for the x and y intercepts
    #Start at y intercept
    x1, y1 = line["y-cept"]
    x2, y2 = line["x-cept"]

    #now that we have these coordinates, we want to draw the line on the canvas
    ##Y-Coordinates are inverted (in pixels you count from top left)
    canvas.create_line(5*x1, (500-5*y1), 5*x2, 500-5*y2, fill="blue", width=2)

    canvas.bind("<Button-1>", lambda event: on_click(event, canvas, graph_number, coordwriter, file))


draw_graph(line_number)


# need to work on this to handle the mouse clicks
def on_click(event, canvas, graph_number, coordwriter, file):
    global line_number

    x, y = event.x, event.y

    #If the click is on the line, we record to the csv file
    if reaches_line():
        with open(FILE_PATH + "excel.csv", mode = "a", newline = "") as file:
            coordwriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            coordwriter.writerow([line_number + 1, x, 500-y])

        #We also want to increase the line_number and draw the next graph

        if line_number < 2:
            line_number += line_number
            draw_graph(line_number)
        else:
            print("You have made a choice for 3 lines, please see excel file")




window.mainloop()







    