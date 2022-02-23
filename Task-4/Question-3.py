student_record=[['rno.','Name','Marks'],[1,'thor',69],[2,'tony',91]]
rsp=("yes")
while rsp=="yes":
    print("Add a student and corresponding details to the record")
    std_roll=int(input("Enter the roll no."))
    std_name=input("Enter the name ")
    std_marks=input("Enter the marks")
    std_lst=[std_roll,std_name,std_marks]
    print(std_lst)
    student_record.append(std_lst)
    rsp=input("Do you want to add another students? enter yes if you want to or else no")
print("Printing the records")
for j in range(len(student_record[0])):
    print(student_record[0][j], end="  ")
print()
for i in range(1,len(student_record)):
    for j in range(len(student_record[i])):
        print(student_record[i][j],end="     ")
    print()
print("extracting second record")
for j in range(len(student_record[2])):
    print(student_record[2][j],end="   ")



