import tkinter as tk
import csv

global line_number
line_number = 0

#Each line is a dictionary (hashmap) which is an element of the list
#The key will be which intercept and the value is the ordered pair (a tuple)
line_equations = [
    {"x-cept": (50, 0), "y-cept": (0, 70)},
    {"x-cept": (100, 0), "y-cept": (0, 80)},
    {"x-cept": (60, 0), "y-cept": (0, 60)}
]

FILE_PATH = "/Users/alexvertikov/Desktop/Personal-Projects/Research_Test/"

#We open the csv file that will serve as our excel spreadsheet of record
with open(FILE_PATH + "excel.csv", mode = "w", newline="") as file:

    coordwriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    coordwriter.writerow(["Question", "x-coordinate", "y-coordinate"])



def reaches_line():
    """Currently this is just a placeholder, but the purpose of this function
    would be to ensure that only clicks which are on the line are recorded. This 
    would ensure that the values recorded in the excel spreadsheet are valid ordered 
    pairs for that linear equation."""
    return True


####
#NOW WE FOCUS ON CREATING THE WINDOW WITH THE GRAPHS, WHERE WE WILL CLICK
####


#In tkinter, we must instantiate the main window of the application
window = tk.Tk()

#Now we create the "canvas" in our window, which is what we can actually draw on
#We have width 1000 pixels, height 800 pixels, white background
canvas = tk.Canvas(window, width=500, height=500, bg="white")
#Adding the canvas widget to its parent window
canvas.pack()

def draw_graph(graph_number):
    """This function draws each graph using tkinter on the necessary window using 
    the intercepts provided."""

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



def on_click(event, canvas, graph_number, coordwriter, file):
    """This function allows us to click on the window and properly record the 
    data in our csv file as well as moving on to the next graph"""

    #We change the global variable, so we define again as global
    global line_number

    x, y = event.x, event.y

    #If the click is on the line, we record to the csv file
    if reaches_line():
        if line_number < 3:
            with open(FILE_PATH + "excel.csv", mode = "a", newline = "") as file:
                coordwriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                coordwriter.writerow([line_number + 1, x/5, (500-y)/5])

        #We also want to increase the line_number and draw the next graph
            line_number = line_number + 1
            print(line_number)
            if line_number < 3:
                draw_graph(line_number)
        else:
            #In the else case, we want to make sure we do not write anymore to the excel file
            print("You have made a choice for 3 lines, please see excel file")




#This starts the loop for tkinter
window.mainloop()







    


