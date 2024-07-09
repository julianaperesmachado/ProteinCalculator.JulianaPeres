import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime

# Initialize tkinter
root = tk.Tk()
root.title("BMR and Protein Intake Recommendation")
root.geometry("800x600+300+100")
root.configure(bg="floralwhite")

# Initialize protein intake history dictionary globally
protein_intake_history = {}

# Load the images using Pillow (after tkinter has been initialized)
log_image = Image.open("C:\\Users\\gomes\\Desktop\\JULIANA\\C-Women\\Python - Rawan\\protein1.jpg")
log_image = log_image.resize((500, 400), Image.LANCZOS)  # Resize log image
tk_log_image = ImageTk.PhotoImage(log_image)

# Function to calculate recommended protein intake based on BMR
def calculate_protein_intake():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_combobox.get()

        if gender.lower() == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        # Assuming a protein ratio of 0.3 for maintenance
        recommended_protein_intake = bmr * 0.3 / 4  # Convert calories to grams
        global recommended_protein_goal
        recommended_protein_goal = recommended_protein_intake  # Update global variable

        # Update result labels
        result_label.config(text=f"BMR: {bmr:.2f} kcal/day")
        recommended_protein_label.config(text=f"Recommended Protein Intake: {recommended_protein_intake:.2f} grams/day")

        # Show result frame
        result_frame.place(x=50, y=400)

        # Prompt user to log protein intake
        log_protein_prompt()

        # Save data to file
        save_data_to_file(name_entry.get(), weight, height, age, gender, bmr, recommended_protein_intake)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight, height, and age.")

def save_data_to_file(user_name, weight, height, age, gender, bmr, recommended_protein_intake):
    today = datetime.date.today().isoformat()

    with open("bmr_data.txt", "a") as file:
        file.write(f"Date: {today}\n")
        file.write(f"User: {user_name}\n")
        file.write(f"Weight: {weight} kg\n")
        file.write(f"Height: {height} cm\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"BMR: {bmr:.2f} kcal/day\n")
        file.write(f"Recommended Protein Intake: {recommended_protein_intake:.2f} grams/day\n\n")

# Function to prompt user to log daily protein intake
def log_protein_prompt():
    if messagebox.askyesno("Log Protein Intake", "Would you like to log your daily protein intake?"):
        open_log_intake_window()

# Function to open the log protein intake window
def open_log_intake_window():
    user_name = name_entry.get()

    # Create a new window for logging protein intake
    log_window = tk.Toplevel(root)
    log_window.title("Protein Intake Calculator")
    log_window.geometry("600x700+400+150")

    # Title for the log window
    log_window_title = tk.Label(log_window, text="PROTEIN INTAKE CALCULATOR", font=("calibri", 20, "bold"), fg="tomato4", bg="peachpuff3")
    log_window_title.pack(fill=tk.X, pady=10)

    # User name display
    user_name_label = tk.Label(log_window, text=f"User: {user_name}", font=("calibri", 16, "bold"), bg="floralwhite")
    user_name_label.pack(pady=10)

    # Create a HistoryWindow instance within the new window
    history_frame = HistoryWindow(log_window, user_name)
    history_frame.pack(padx=20, pady=20)

# History Display Window
class HistoryWindow(tk.Frame):
    def __init__(self, parent, user_name):
        super().__init__(parent, bg="floralwhite")

        self.user_name = user_name
        self.total_protein_intake = 0  # Initialize cumulative total
        self.recommended_goal = recommended_protein_goal

        # Display the log image
        self.image_label = tk.Label(self, image=tk_log_image)
        self.image_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.protein_label = tk.Label(self, text="Log Protein Intake (grams):", font=("calibri", 12, "bold"), bg="floralwhite")
        self.protein_label.grid(row=1, column=0, padx=20, pady=10)

        self.protein_entry = tk.Entry(self, width=10, font=("calibri", 12))
        self.protein_entry.grid(row=1, column=1, padx=20, pady=10)

        self.log_protein_btn = tk.Button(self, text="Enter", font=("calibri", 12), bg="moccasin", command=self.log_daily_protein_intake)
        self.log_protein_btn.grid(row=1, column=2, padx=20, pady=10)

        self.history_label = tk.Label(self, text="Protein Intake History:", font=("calibri", 14, "bold"), bg="floralwhite")
        self.history_label.grid(row=2, column=0, columnspan=3, padx=20, pady=10)

        self.history_text = tk.Text(self, width=80, height=15, font=("calibri", 12), wrap=tk.WORD)
        self.history_text.grid(row=3, column=0, columnspan=3, padx=20, pady=10)
        self.history_text.config(state=tk.DISABLED)

        self.update_protein_history_display()

    def log_daily_protein_intake(self):
        try:
            protein_intake = float(self.protein_entry.get())
            today = datetime.date.today().isoformat()

            if self.user_name in protein_intake_history:
                if today in protein_intake_history[self.user_name]:
                    protein_intake_history[self.user_name][today].append(protein_intake)
                else:
                    protein_intake_history[self.user_name][today] = [protein_intake]
            else:
                protein_intake_history[self.user_name] = {today: [protein_intake]}

            self.total_protein_intake += protein_intake  # Update cumulative total

            self.update_protein_history_display()

            # Clear protein entry field after logging
            self.protein_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for protein intake.")

    def update_protein_history_display(self):
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete('1.0', tk.END)

        total_protein = 0

        if self.user_name in protein_intake_history:
            for date, entries in protein_intake_history[self.user_name].items():
                self.history_text.insert(tk.END, f"Date: {date}\n")
                self.history_text.insert(tk.END, f"Recommended Protein Intake Goal: {self.recommended_goal:.2f} grams/day\n\n")

                for i, intake in enumerate(entries, start=1):
                    self.history_text.insert(tk.END, f"Entry {i}: {intake:.2f} grams\n")

                self.history_text.insert(tk.END, f"Cumulative Protein Intake: {sum(entries):.2f} grams\n")
                self.history_text.insert(tk.END, f"Remaining Protein Intake Goal: {max(0, self.recommended_goal - sum(entries)):.2f} grams\n\n")

        self.history_text.config(state=tk.DISABLED)

# Title for the main window
main_window_title = tk.Label(root, text="BMR AND PROTEIN INTAKE RECOMMENDATION", font=("calibri", 20, "bold"), fg="tomato4", bg="peachpuff3")
main_window_title.pack(fill=tk.X, pady=10)

# Labels and Entries for BMR calculation
name_label = tk.Label(root, text="Name:", font=("calibri", 12, "bold"), bg="floralwhite")
name_label.place(x=50, y=80)
name_entry = tk.Entry(root, width=20, font=("calibri", 12))
name_entry.place(x=200, y=80)

weight_label = tk.Label(root, text="Weight (kg):", font=("calibri", 12, "bold"), bg="floralwhite")
weight_label.place(x=50, y=130)
weight_entry = tk.Entry(root, width=20, font=("calibri", 12))
weight_entry.place(x=200, y=130)

height_label = tk.Label(root, text="Height (cm):", font=("calibri", 12, "bold"), bg="floralwhite")
height_label.place(x=50, y=180)
height_entry = tk.Entry(root, width=20, font=("calibri", 12))
height_entry.place(x=200, y=180)

age_label = tk.Label(root, text="Age:", font=("calibri", 12, "bold"), bg="floralwhite")
age_entry = tk.Entry(root, width=20, font=("calibri", 12))
age_label.place(x=50, y=230)
age_entry.place(x=200, y=230)

gender_label = tk.Label(root, text="Gender:", font=("calibri", 12, "bold"), bg="floralwhite")
gender_label.place(x=50, y=280)
gender_combobox = ttk.Combobox(root, values=['Male', 'Female'], width=18, font=("calibri", 12))
gender_combobox.place(x=200, y=280)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", font=("calibri", 12), bg="moccasin", command=calculate_protein_intake)
calculate_button.place(x=50, y=330)

# Result frame
result_frame = tk.Frame(root, bg="floralwhite")
result_label = tk.Label(result_frame, text="", font=("calibri", 14, "bold"), bg="floralwhite")
result_label.grid(row=0, column=0, padx=20, pady=10)

recommended_protein_label = tk.Label(result_frame, text="", font=("calibri", 14, "bold"), bg="floralwhite")
recommended_protein_label.grid(row=1, column=0, padx=20, pady=10)

# Main loop
root.mainloop()
