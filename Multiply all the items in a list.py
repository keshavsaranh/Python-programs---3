def my_list(list1):
    x=1
    for i in list1:
        x=x*i
    return x

y=input("Enter your list spces in between:")
list1=list(map(int,y.split()))
print("List: ", list1)
print(my_list(list1))
