
# Student Grade Management System

# Function to evaluate student performance
def evaluate_student(score, attendance):
    print("\n--- Student Evaluation ---")
    
    # Check if inputs are valid
    if score < 0 or score > 100 or attendance < 0 or attendance > 100:
        return "Invalid input! Score and attendance must be between 0 and 100."
    
    # Main condition to evaluate grade
    if score >= 90 and attendance >= 85:
        grade = "A"
        feedback = "Excellent performance! Keep it up."
    elif score >= 80 and attendance >= 80:
        grade = "B"
        feedback = "Good job, but ensure consistent attendance."
    elif score >= 70 and attendance >= 75:
        grade = "C"
        # Nested condition for additional feedback
        if attendance >= 80:
            feedback = "Decent score, great attendance!"
        else:
            feedback = "Passing, but improve your attendance."
    elif score >= 60:
        grade = "D"
        feedback = "Barely passing. Work harder on your studies."
    else:
        grade = "F"
        # Nested condition for failure reasons
        if attendance < 70:
            feedback = "Failed due to low score and poor attendance."
        else:
            feedback = "Failed due to low score. Attendance is okay."

    # Additional feedback using logical operators
    if not (score >= 60 and attendance >= 75):
        warning = "Warning: You are at risk of failing the course."
    else:
        warning = ""

    # Return formatted result
    return f"Grade: {grade}\nFeedback: {feedback}\n{warning}"

# Main program
def main():
    print("Welcome to the Student Grade Management System")
    
    # Get user input
    try:
        score = float(input("Enter student's score (0-100): "))
        attendance = float(input("Enter student's attendance percentage (0-100): "))
        
        # Call evaluation function and display result
        result = evaluate_student(score, attendance)
        print(result)
        
    except ValueError:
        print("Error: Please enter valid numeric values.")

# Run the program
if __name__ == "__main__":
    main()
