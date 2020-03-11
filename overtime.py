## OverTime.py
## Programming ITC110
## Jeremy Ward


# Using Tkinker
import tkinter as tk

root = tk.Tk()

## Making The Main Winow here
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

## Now we are putting up text yay!
label1 = tk.Label(root, text='Overtime Wage Calculator')
label1.config(font=('helvetica', 14,'bold'), anchor='center',foreground='green')
canvas1.create_window(200, 25, window=label1)

## More Text YAY!
label2 = tk.Label(root, text='Number Of Hours Worked:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label2)

## Making entry
entry1 = tk.Entry (root)
canvas1.create_window(200, 80, window=entry1)

## More labels here
label3 = tk.Label(root, text='Hourly Wage:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label3)

## Second Entry here
entry2 = tk.Entry(root)
canvas1.create_window(200, 120, window=entry2)

## Getting input values and doing calculations
## Setting overtime value to zero
def getHourlyRate ():
    over_time = 0
    x1 = float(entry1.get())
    x2 = float(entry2.get())

## If we have a number over 40 we have ovetime
    if (x1 > 40):
        over_time = x1 - 40
        x1 = x1 - over_time
        x3 = x1 * x2 + (over_time * 1.5 * x2)

    else: # otherwise not
        x3 = x1 * x2

    # label 4 here and output
    label4 = tk.Label(root, text='$' + str(x3),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

# here is button to calculate as well as creating the main window
button1 = tk.Button(text='Calculate!', command=getHourlyRate, bg='black', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 160, window=button1)

# mainloop
root.mainloop()
