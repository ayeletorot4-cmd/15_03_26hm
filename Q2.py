#Exercise 2 – Average grade
import  statistics
grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

def get_average_grade(grades: dict) -> float:
    '''

    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    grade_lst=[]
    for name, grade in grades.items():
        grade_lst.append(grade)
    Avg_=statistics.mean(grade_lst)
    return Avg_
print(grades)
print(get_average_grade(grades))