if __name__ == '__main__':
    lst = list(map(float, input("Введите элементы списка: ").split()))
    res=0
print(lst)
for i in lst:
    if lst.index(i) % 2 != 0:
        res += i
print(f'1) {res:.2f}')
idx=[i for i,j in enumerate(lst) if j<0]
m = (sum(lst[idx[0]+1:idx[-1]]))
print(f'2) {m:.2f}')
