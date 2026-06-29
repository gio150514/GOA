list1=[15,23,99]
def name(list):
    sum1=[] 
    for i in list:
        sum1.append(i*i)
    return sum(sum1)
print(name(list1))