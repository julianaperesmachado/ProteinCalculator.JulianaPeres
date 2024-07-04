import tkinter
from tkinter import ttk
from tkinter import messagebox

# creating an object
root = tkinter.Tk()

# setting title and geometry
root.title("Protein Intake Calculator")
root.geometry("470x580+300+200")

# background color for window
root.config(bg="floralwhite")

# RMR Calculation
def rmr_calculator():
    try:
        Height = float(h.get())
        Weight = float(w.get())
        Age = int(a.get())
        Gender = str(g.get())

        # RMR calculation
        if Gender.lower() == 'male':
            rmr_value = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        else:
            rmr_value = (10 * Weight) + (6.25 * Height) - (5 * Age) - 161

        # Protein intake recommendation (1.6 grams per kg of body weight)
        protein_intake = 1.6 * Weight

        with open("rmr_data.txt", "a") as file:
            file.write(f"{Height},{Weight},{Age},{Gender},{rmr_value:.2f}\n")

        result.set(f"RMR: {rmr_value:.2f} kcal/day\nRecommended Protein Intake: {protein_intake:.2f} grams/day")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for height, weight, and age.")

# Heading label
top = tkinter.Label(root, text="PROTEIN CALCULATOR", font=("calibri", 25, "bold"), width=30, bd=5, fg="tomato4", bg="peachpuff3")
top.place(x=0, y=0)

# Entry widgets
heightlabel = tkinter.Label(root, text="Height (cm):", fg="lightsalmon4", bg="floralwhite", font=("calibri", 12, "bold"))
heightlabel.place(x=50, y=70)
h = tkinter.Entry(root, width=10, font=("calibri", 12))
h.place(x=200, y=70)

weightlabel = tkinter.Label(root, text="Weight (kg):", fg="lightsalmon4", bg="floralwhite", font=("calibri", 12, "bold"))
weightlabel.place(x=50, y=120)
w = tkinter.Entry(root, width=10, font=("calibri", 12))
w.place(x=200, y=120)

agelabel = tkinter.Label(root, text="Age:", fg="lightsalmon4", bg="floralwhite", font=("calibri", 12, "bold"))
agelabel.place(x=50, y=170)
a = tkinter.Spinbox(root, from_=15, to=80)
a.place(x=200, y=170)

genderlabel = tkinter.Label(root, text="Gender:", fg="lightsalmon4", bg="floralwhite", font=("calibri", 12, "bold"))
genderlabel.place(x=50, y=220)
g = ttk.Combobox(root, values=['male', 'female'])
g.place(x=200, y=220)

# Calculate button
calculatebtn = tkinter.Button(root, text="Calculate", fg="orange4", bg="moccasin", font=("calibri", 12, "bold"), command=rmr_calculator)
calculatebtn.place(x=350, y=270)

# Result label
result = tkinter.StringVar()
resultlabel = tkinter.Label(root, textvariable=result, bg="floralwhite", font=("calibri", 12))
resultlabel.place(x=50, y=320)

root.mainloop()
