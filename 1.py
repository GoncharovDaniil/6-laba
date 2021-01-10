if __name__ == '__main__':
    lst = [-2, 3, -4, 5, 4, 6, -2, 5, -4, 10]
print(lst)
n = [i for i in lst if i < 0]
m=0
for i in n:
    m=m+i
print('Сумма отрицательных: ', m)