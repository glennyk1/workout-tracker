import datetime

exercises = ["Bench Press", "Squat", "Deadlift", "Overhead Press"]

workout_history = []

def display_menu():
    """Display the main menu options"""
    print("Select an option:")
    print("1. Log a new workout")
    print("2. View workout history")
    print("3. Add a new exercise")
    print("4. Exit")
    
def get_valid_float(prompt):
    """Prompt until a valid float is entered."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def log_workout():
    """
    Logs a new workout session.
    The user can select exercises, record the number of sets,
    the reps per set, and optionally the RPE for each set
    """
    date_input = input("Enter the workout date (YYYY-MM-DD) or press Enter for today: ")
    if date_input.strip() == "":
        date_input = datetime.datetime.now().strftime("%Y-%m-%d")
        
    session = {"date": date_input, "exercises": []}
    
    while True:
        print("\nAvailable exercises: ")
        for i, ex in enumerate(exercises):
            print(f"{i+1}. {ex}")
        print(f"{len(exercises)+1}. Done logging exercises") # additional option at end of list
        
        choice = input("Select an exercise by number: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == len(exercises) + 1:
            break
        elif 1 <= choice <= len(exercises):
            ex_name = exercises[choice - 1]
            exercise_entry = {"exercise": ex_name, "sets": []}
            
            try:
                num_sets = int(input(f"How many sets for {ex_name}? "))
            except ValueError:
                print("Please enter a valid number of sets.")
                continue
            
            for s in range(num_sets):
                try:
                    reps = int(input(f"Enter for reps for set {s+1}: "))
                except ValueError:
                    print("Please enter a valid number of reps.")
                    reps = 0
                    
                weight = get_valid_float(f"Enter weight for set {s+1}: ")
                    
                rpe = None
                rpe_input = input("Would you like to enter RPE for this set? (y/n): ").lower()
                if rpe_input == "y":
                    try:
                        rpe = float(input("Enter RPE: "))
                    except ValueError:
                        print("Invalid RPE, skipping")
                        
                exercise_entry["sets"].append({"reps": reps, "weight": weight, "rpe": rpe})
            
            session["exercises"].append(exercise_entry)
        else:
            print("Invalid choice. Please try again.")
    workout_history.append(session)
    print("Workout logged successfully!")
    
def view_history():
    """Displays all logged workout sessions"""
    if not workout_history:
        print("No workouts logged yet.")
        return
    for session in workout_history:
        print(f"\nDate: {session['date']}")
        for entry in session['exercises']:
            print(f"  Exercise: {entry['exercise']}")
            for idx, set_data in enumerate(entry['sets']):
                reps = set_data['reps']
                weight = set_data["weight"]
                rpe = set_data['rpe']
                set_info = f"    Set {idx+1}: {reps} reps, {weight}lbs"
                if rpe is not None:
                    set_info += f" with RPE {rpe}"
                print(set_info)
        print("-" * 30)
        
def add_exercise():
    """Allows the user to add a new exercise to the list"""
    new_ex = input("Enter the name of the new exericse: ")
    if new_ex.strip():
        exercises.append(new_ex)
        print(f"{new_ex} added to the exercise list.")
    else:
        print("No exercise entered.")

def main():
    """Main loop for the application."""
    while True:
        print("\n--- Hypertrophy Tracker ---")
        display_menu()
        option = input("Select an option: ")
        if option == "1":
            log_workout()
        elif option == "2":
            view_history()
        elif option == "3":
            add_exercise()
        elif option == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()