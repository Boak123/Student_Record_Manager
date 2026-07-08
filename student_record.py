name = input("Enter student name: ")
score = int(input("Enter student score: "))

def add_student(filename, name, score):
    with open(filename, 'a') as add_stud:
        add_stud.write(f"{name},{score}\n")

add_student('student_record.txt', name, score)

def display_students(filename):
    with open(filename, 'r') as disp_stud:
        for line in disp_stud:
            name, score = line.strip().split(',')
            score = int(score)
            print(f"{name} - {score}")

display_students('student_record.txt')

def highest_score(filename):
    with open(filename, 'r') as high_score:
        highest = 0
        for line in high_score:
            name, score = line.strip().split(',')
            score = int(score)
            if score > highest:
                highest = score
                highest_student = name
    return highest_student, highest

highest_student, highest_score = highest_score('student_record.txt')
print(f"Highest student: {highest_student} with score: {highest_score}")