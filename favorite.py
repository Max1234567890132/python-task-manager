grades = {1:"good",2:"bad" }
def grade_text(grade):
    return grades.get(grade,"Неверная оценка")

grade = int(input("text"))
print(grade_text(grade))