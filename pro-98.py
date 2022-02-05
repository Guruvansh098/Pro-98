def swap():
    file1=input("ENter the 1st file name")
    file2=input("Enter the 2nd file name")
    with open(file1,'r')as f:
        data_a=f.read()
    with open(file2,'r')as f2:
        data_b=f2.read()
    with open(file1,'w')as f:
        f.write(data_b)
    with open(file2,'w')as f2:
        f2.write(data_a)
swap()


