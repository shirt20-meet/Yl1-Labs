'''
#exercise one
list1 = [5, 10, 15, 20, 25]
x = list1[0]
y = list1[-1]
def a (x, y):
    print (str(x) +  ", " + str(y))
a(x,y)
'''

'''
#exrcise two
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list1:
    if i < 5:
        print(i)
'''

'''
#exercise three
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for t in b:
        if (i == t):
            c.append(i)
print(c)
'''

#exerise four
import tkinter as tk
from tkinter import simpledialog

answer = (int)(simpledialog.askstring("Input", "Your message here!", parent=tk.Tk()))
boolean = 1

for i in range(2, answer-1):
    if (answer%i == 0):
        print('Nope')
        boolean = 0
        break
    else:
        print('Maybe')
        boolean = 1

if (boolean == 1):
    print('Yep')
        
