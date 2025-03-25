import tkinter as tk # importing this for GUI elements
from tkinter import messagebox # importing this for pop-up dialogs
import datetime

# global list to store workout sessions and available exercises
workout_history = []
exercises = ["Bench Press", "Squat", "Deadlift", "Overhead Press"]


# Step 1: Create the main application window
root = tk.Tk()
# this line of code initializes the main window(root window) for the application

root.title("Workout Tracker")
# this sets the title of the window which appears in the title bar

root.geometry("400x300")
# this defines the size of the window (width x height in pixels)
# this helps make sure that the winsow appears at a reasonable size

# Step 2: Create the log workout window
def log_workout_window():
    #create a new top-level window
    log_win = tk.Toplevel(root)
    log_win.title("Log Workout")
    log_win.geometry("400x400")
    
    # workout data
    tk.Label(log_win, text="Workout Date (YYY-MM-DD): ").pack(pady=5)
    date_entry = tk.Entry(log_win)
    date_entry.pack(pady=5)
    # set the default value to today's date
    date_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
    
    # exercise selection
    tk.Label(log_win, text="Select Exercse: ").pack(pady=5)
    exercise_var = tk.StringVar(log_win)
    exercise_var.set(exercises[0]) # default is the first exercise
    exercise_menu = tk.OptionMenu(log_win, exercise_var, *exercises)
    exercise_menu.pack(pady=5)
    
    # reps input
    tk.Label(log_win, text="Reps: ").pack(pady=5)
    reps_entry = tk.Entry(log_win)
    reps_entry.pack(pady=5)
    
    # weight input (required)
    tk.Label(log_win, text="Weight (lbs): ").pack(pady=5)
    weight_entry = tk.Entry(log_win)
    weight_entry.pack(pady=5)
    
    #RPE input (optional)
    tk.Label(log_win, text="RPE 1-10 (optional): ").pack(pady=5)
    rpe_entry = tk.Entry(log_win)
    rpe_entry.pack(pady=5)
    
    # submit button functionality
    def submit_workout():
        # retrieve data from the field
        date = date_entry.get()
        exercise = exercise_var.get()
        try:
            reps = int(reps_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for reps.")
            return
        try:
            weight = float(weight_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for weight")
            return
        
        # rpe is optional
        rpe_value = rpe_entry.get()
        if rpe_value:
            try:
                rpe = float(rpe_value)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for RPE.")
                return
        else:
            rpe = None
            
        # creates a session dictionary with the input details
        session = {
            "date": date,
            "exercises": [
                {"exercise": exercise, "sets": [{"reps": reps, "weight": weight, "rpe": rpe}]}
            ]
        }
        workout_history.append(session)
        messagebox.showinfo("Success", "Workout logged successfully!")
        log_win.destroy()
        
    submit_button = tk.Button(log_win, text="Submit Workout", command=submit_workout)
    submit_button.pack(pady=10)
    
# End of log workout window code

def view_history_window():
    # create a new top-level window for viewing history
    history_win = tk.Toplevel(root)
    history_win.title("View Workout History")
    history_win.geometry("500x400")
    
    # create a text widget with a vertical scrollbar to display history
    text_frame = tk.Frame(history_win)
    text_frame.pack(expand=True, fill='both')
    
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side='right', fill='y')
    
    history_text = tk.Text(text_frame, wrap='word', yscrollcommand=scrollbar.set)
    history_text.pack(expand=True, fill='both')
    scrollbar.config(command=history_text.yview)
    
    # check if there is any workout logged
    if not workout_history:
        history_text.insert(tk.END, "No workouts logged yet\n")
    else:
        # iterate through each workout session and display details
        for session in workout_history:
            history_text.insert(tk.END, f"Date: {session['date']}\n")
            for exercise_entry in session["exercises"]:
                history_text.insert(tk.END, f"  Exercise: {exercise_entry['exercise']}\n")
                for idx, set_data in enumerate(exercise_entry["sets"]):
                    reps = set_data["reps"]
                    weight = set_data["weight"]
                    rpe = set_data["rpe"]
                    set_info = f"   Set {idx+1}: {reps} reps, {weight} lbs"
                    if rpe is not None:
                        set_info += f", RPE {rpe}"
                    history_text.insert(tk.END, set_info + "\n")
                history_text.insert(tk.END, "\n")
            history_text.insert(tk.END, "-"*40 + "\n")

# Step 2: Add a greeting label
greeting_label = tk.Label(root, text="Welcome to the Workout Tracker", font=("Helvetica", 14))
# this creates a Label widget as a child of 'root'
# the label displays a welcome message in the specified font and size

greeting_label.pack(pady=20)
# 'pack()' adds the label to the window
# 'pady=20' adds a vertical padding around the label for better spacing

# Step 3: Add a "Log Workout" button
log_workout_button = tk.Button(root, text="Log Workout", command=log_workout_window)
# this creates a Button widget
# the 'command' parameter defines what function to clal when the button is clicked
# here, it shows an informational pop-up as a placeholder

log_workout_button.pack(pady=10)
# this adds the button to the window with some padding

# Step 4: Add a "View History" button
view_history_button = tk.Button(root, text="View History", command=view_history_window)
# similar to the Log Workout button, this button is a placeholder for viewing logged workouts

view_history_button.pack(pady=10)


# Step 5: Add an "Add Exercise" button
add_exercise_button = tk.Button(root, text="Add Exercise", command=lambda: messagebox.showinfo("Add Exercse", "Add Exercise functionality will go here!"))
# this is a placeholder for adding a new exercise

add_exercise_button.pack(pady=10)

# Step 6: Add an "Exit" button to close the application
exit_button = tk.Button(root, text="Exit", command=root.destroy)
# 'root.destory' is claled when the buytton is pressed, which closes the window

exit_button.pack(pady=10)

# Step 7: Run the Tkinter main loop
root.mainloop()
# 'mainloop()' starts the GUI event loop, waiting for events (like button clicks) and keeps the window open until the user closes it