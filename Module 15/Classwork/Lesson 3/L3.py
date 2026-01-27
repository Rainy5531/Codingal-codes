import matplotlib.pyplot as plt

# Student Data
student_names = ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

# Calculate percentae (assuming total marks = 50)
marks_perc = [(marks / 50) * 100 for marks in students_marks]

# Line chart for raw marks
def marks_line_chart():
    plt.plot(student_names, students_marks, marker='.', linestyle='-', color='blue', ms=20, mec='r', linewidth='5') # linestyle='dotted', linestyle='dashed'
    plt.title("Students Marks Graph")
    plt.xlabel("Stdents Names")
    plt.ylabel("Marks out of 50")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Bar chart for percentage
def percentage_bar_chart():
    plt.bar(student_names, marks_perc, color='green')
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

# Run both charts
marks_line_chart()
percentage_bar_chart()