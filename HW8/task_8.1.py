# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

import random as r
import statistics as s

def Medium_Grades (gr):
    mean_grades = []
    for grades_in_group in gr:
        mean_grades.append(s.mean(grades_in_group))   
    return mean_grades

groups = r.randint(2,5)
grades = [0]*groups

for i in range(len(grades)):
    grades[i] = list(r.randint(2,5) for s in range(r.randint(20,30)))

mean = Medium_Grades (grades)
print (f'среднии оценки групп -> {mean}')
max_mean=max(mean)
group_number = mean.index(max_mean)
print(f'У группы {group_number+1} наилучший средний балл? равный {max_mean}')