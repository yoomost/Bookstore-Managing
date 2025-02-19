#lst = [{'name': 'Alice', 'score': 90}, {'name': 'Bob', 'score': 85}, {'name': 'Carol', 'score': 95}]
sv = input('nhap vao diem va ten sinh vien ').split()
print('djfiuqhfiuqhu', sv)

dic = {}
sv_data = [{'name': sv[i],'score':int(sv[i+1])} for i in range(0, len(sv), 2)]
print(sv_data)
max_cor= max(sv['core'] for sv in sv_data)
print('diem cao nhat cua sinh vien')
for sv  in sv_data:
    if sv['core']==max_cor:
        print(sv['name'])
#2
num = tuple(map(int, input('nhap vao so').split()))
print(num)

sorted_num = sorted(num)
print(sorted_num)

sorted_num2=list(num)
sorted_num2.sort(num)
print('sorted tuple', tuple(sorted_num2))

# cau3

num1 = list(map(int, input('nhap vao so nguyem').split()))

averge = sum(num1)/len(num1)

min_num = min(num1)
max_num = max(num1)

print('gia tri trung binh', averge)
print('gia tri nho nhat', min)
print('gia tri lon nhat', max)
