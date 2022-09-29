#1
print("I***like***Python")

#2
separator = input("введите: ")
s1 = input()
s2 = input()
s3 = input()
print(s1, s2, s3, sep=separator)

#3
num = int(input("Введите число"))
print(f"Целое число - {num}")
print(f"На один меньше {num-1}")
print(f"На один больше {num+1}")

#4
numxx = int(input("Ведите число xx :"))
print(f"{numxx} --- {numxx*2} --- {numxx*3} --- {numxx*4} --- {numxx*5}")

#5
arr = [10, 31, 412, 52, 14, 79, 52, 505]
for i in arr:
    if i % 2 == 0:
        print(i)


#6
def func(a):
    for i in a:
        if i % 2 == 0:
            print(i)

func([10, 421, 420, 40, 21, 89])

#7
x = (input("Введите 4 цифры: ")).split()
print(max(x))