def gradingStudents(grades):
    for i in grades:
        if(i<38):
            print(i)
        else:
            x = i%5
            if(x>2):
                print(i + (5-x))
            else:
                print(i)

print(gradingStudents([29,84,81,79,55,63]))

