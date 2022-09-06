from multiprocessing.connection import wait
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

def display_map(map, map_name): #, pieces):

  x = len(map)
  y = len(map[0])

  colors = []
  for i in range(0, len(map)):
    col_row=[]
    for p in map[i]:
      if len(p) == 0: 
        #print("open")
        #c_text = 
        c_color = "white"
      if 0 in p: 
        #print("wall")
        #c_text = 
        c_color = "black"
      if 1 in p: 
        #print("unit 1")
        #c_text = 
        c_color = "blue"
      if 2 in p: 
        #print("unit 2")
        #c_text = 
        c_color = "red"
      col_row.append(c_color)
    colors.append(col_row)

  #cell_text = [["John", "23", "98", "234"], ["James", "24", "90", "239"]]

  fig, ax = plt.subplots()

  the_table = ax.table(
    #rowLabels= #Letters
    #colLabels= #Numbers
    #cellText=cell_text,
    colWidths = [0.05 for i in range(x)],
    cellColours = colors,
    loc = 'center')
  ax.axis('off')

  plt.rcParams["figure.figsize"] = [4.50, 4.50]
  plt.rcParams["figure.autolayout"] = True
  plt.xticks([])
  plt.yticks([])
  plt.title(map_name) 
  plt.pause(3)

def close_map():
  plt.close('all')

if __name__ == "__main__":
  
  example_map = [
    [[],[],[0],[0], [2]],
    [[],[0],[0],[0], []],
    [[],[],[],[], []],
    [[0],[],[0],[0], []],
    [[0],[],[],[0], [1]]
  ]

  display_map(map=example_map, map_name="Example")
  
  print("Closing in 6 sec")
  sleep(6)

  close_map()

