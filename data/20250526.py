import random

def main():
    a = [20, 10, 30, 40]
    print("Original list:", a)
    print("ID of list:", id(a))
    
    # 升序排列
    a.sort()
    print("Sorted list (ascending):", a)
    
    # 降序排列
    a = [10, 20, 30, 40]
    a.sort(reverse=True)
    print("Sorted list (descending):", a)
    
    # 打乱顺序
    random.shuffle(a)
    print("Shuffled list:", a)

if __name__ == "__main__":
    main()

a = [
     ["高小一",18,30000,"北京"],
        ["高小二",19,20000,"上海"],
        ["高小一",20,10000,"深圳"],
   ]
for m in range(3):
  for n in range(4):
    print(a[m][n],end="\t")
  print() #打印完一行，换行

