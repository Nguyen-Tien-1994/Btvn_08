"""
Bài 00.
Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    Sau đó, unpack các phần tử trong một tuple.
"""
"""
a = int(input("nhập a ="))
b = float(input("nhập b ="))
c = input("nhập c:")
d = [a,b,c]
n = (a, b, c, d)
m = []
for i in n:
    if type(i) == list:
        m.append(tuple(i))
    else:
        m.append(i)
print(m)
for j in set(m):
    print(j)
"""

# Bài 01. Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
# Bài làm:
"""
n = (1,"a", "b",[1,2,3])
print(list(n))
n1 = list(n)
print(tuple(n1))
"""


# Bài 02. Viết chương trình đảo ngược một tuple.
# Bài làm:
"""
n = (1,123,"a",[1,2,3,4])
n = list(n)
Cách 1:
n = n[::-1]
print(tuple(n))
n1 = []
Cách 2:
for i in n:
    n1.insert(0,i)
print(tuple(n1))
"""


# Bài 3:
# ài 03. Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
# bài làm:
"""
n = [1,2,"a","str","python",[1,2,3],(1,2,3),"a","b"]
dem = 0
for i in n:
    if type(i) != tuple:
        dem += 1
    else:
        print(dem)
"""


# Bài 4:
"""
Bài 04.
    Cho 1 list chứa các tuple không rỗng.
    Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
"""
# Bài làm:
"""
x = [(2,5),(4,1),(0,0),(4,6]
y = [x[0]]
for i in x:
    for j in range(len(y)):
        if i[len(i) -1] < y[j][len(y[j]) -1]:
            y.insert(0,i)
        elif y[j][len(y[j]) -1] > y[j][len(y[j]) -1]:
            y.append(i)
        elif y[j -1][len(y[j]) -1] < i[len(i) -1] < y[j][len(y[j]) -1]:
            y.insert(j -1,i)
print(y)
"""


# Bài 05. Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
# Bài làm:
"""
n = [(2,5),(4,1),(0,0),(4,6)]
min = n[0]
for i in n:
    if i[1] < min[1]:
        min = i
print(min)
"""


# Bài 6:
# Bài 06. Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple
"""
n = (1,2,3,"a", "b", "c")
print(n[3])
print(n[-4])
"""


# Bài 7:
# Bài 07. Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
"""
n = (1,2,3,"a","b","c")
m = (4,5,6,78,9)
for i in range(len(n)):
    if n[i] in m:
        print("2 tuple có phần tử chung")
        break
    else:
        if i <= len(n) - 2:
            continue
        else:
            print("2 tuple không có phần tử chung")
"""


# Bài 8:
# Bài 08. Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
# Bài làm:
"""
n = (1,1,1,1,1,1,1)
for i in range(len(n)):
    if n[i] != n[0]:
        print("các phần tử trong tuple không giống nhau")
        break
    else:
        if i <= len(n) -2 :
            continue
        else:
            print("tất cả các phần tử của n giống nhau")
"""


# Bài 09. Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực
"""
n = (1,2,3,1.2,5,8)
tong = 0
max = n[0]
for i in n:
    tong += i
    if i > max:
        max = i

print(tong)
print(max)
"""


#Bài 10:
# Bài 10. Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#    Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
# Bài làm:
"""
n = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
m = []
mien = ""
for i in n:
    for j in range(-1,-len(i) -1,-1):
        if i[j] == "." :
            mien = i[j + 1:]
            m.append(mien)
            break
print(m)
"""


# Bài 11:
# Bài 11. Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
"""
n = input("nhập n:")
m = []
a = -1
for i in range(len(n)):
    if n[i] == " ":
        m.append(n[a+1:i])
        a = i
    elif i == len(n) - 1 :
        m.append(n[a+1:len(n)])
print(m)
max_len = m[0]
for j in m:
    if len(j) > len(max_len):
        max_len = len(j)
print(max_len)
"""
"""
x = [(2,5),(4,1),(0,0),(4,6),(7,8)]
y = [x[0]]
for i in x[1:]:
    if i[-1] < y[0][-1]:
        y.insert(0,i)
    elif i[-1] > y[-1][-1]:
        y.append(i)
    else:
        for j in range(len(y)):
            if y[j -1][-1] < i[-1] < y[j][-1]:
                y.insert(j -1,i)
print(y)
"""







