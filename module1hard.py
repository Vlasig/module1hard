grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
print(students_sort)
# average_score = [sum(grades[0])/len(grades[0]),
#                  sum(grades[1])/len(grades[1]),
#                  sum(grades[2])/len(grades[2]),
#                  sum(grades[3])/len(grades[3]),
#                  sum(grades[4])/len(grades[4])]
average_score = [sum(sub_list) / len(sub_list) for sub_list in grades]
print(average_score)
my_dict = dict(zip(students_sort, average_score))
print(my_dict)




