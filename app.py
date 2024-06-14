from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_upper_body_workout():
    upper_body_exercises = {
        "1st Exercise": ["Flat Bench press", "Flat Dumbbell press", "Incline Bench Press", "Incline Dumbbell Press"],
        "2nd Exercise": ["Weighted Pull-ups", "Lat pulldowns"],
        "3rd Exercise": ["DB Shoulder press", "OHP", "Machine Shoulder Press", "DB Rear Delt Fly / DB Side Lateral Raise Superset"],
        "4th Exercise": ["Push-ups", "Chest flys", "Dips"],
        "5th Exercise": ["Barbell Rows", "Machine Rows", "Cable Rows"],
        "6th Exercise": ["DB curls", "DB Hammer curls", "Cable Curls", "Barbell Curls"],
        "7th Exercise": ["V-Bar Pushdown", "EZ Bar pushdowns", "DB Skull crushers", "Skull crushers", "Overhead tricep extension"]
    }

    upper_body_workout = []

    for muscle_group, exercises in upper_body_exercises.items():
        exercise = random.choice(exercises)
        upper_body_workout.append((muscle_group, exercise))

    return upper_body_workout

def generate_lower_body_workout():
    lower_body_exercises = {
        "Exercise 1": ["Barbell Squats", "Hack Squats", "Smith Machine Squats"],
        "Exercise 2": ["Leg press", "Lunges", "RDLs"],
        "Exercise 3": ["Lying leg curls", "Seated Leg Curls"],
        "Exercise 4": ["Leg Extension", "Goblet Squat (Feet Close Together)"],
        "Exercise 5": ["Calf raises", "Standing calf raises", "Seated calf raises"]
    }

    lower_body_workout = []

    for muscle_group, exercises in lower_body_exercises.items():
        exercise = random.choice(exercises)
        lower_body_workout.append((muscle_group, exercise))

    return lower_body_workout

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/workout', methods=['POST'])
def workout():
    choice = request.form['choice'].strip().lower()
    if choice == "upper":
        workout = generate_upper_body_workout()
        workout_type = "Upper Body Workout"
    elif choice == "lower":
        workout = generate_lower_body_workout()
        workout_type = "Lower Body Workout"
    else:
        return "Invalid choice. Please enter 'upper' or 'lower'."

    return render_template('workout.html', workout_type=workout_type, workout=workout)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')