from menu import *
from student_info import *

def main():
    infos = [] 
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            # 显示学生信息:
            output_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_student(infos)
        elif s == '5':
            output_student_by_score_desc(infos)  # 降序
        elif s == '6':
            output_student_by_score_asc(infos)  # 升序
        elif s == '7':
            output_student_by_age_desc(infos)  # 降序
        elif s == '8':
            output_student_by_age_asc(infos)  # 升序
        
        elif s == 'q':
            break

main()