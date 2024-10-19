'''print("键盘敲烂")
print(     "月薪过万")
print("学it"
      )
n = int(input("请输入一个整数:"))
sum = 0
for i in range(n+1):
    sum += i
print("1-%d的求和结果为:%d"%(n,sum))'''
'''l= [9]
for i in range(3):
        x =float(input("请输入整数:"))
        l.append(x)
l.sort()
print(l)'''
'''for i in range(1,10):
     for j in range(1,i+1):
         print("%dx%d=%-3d"%(j,i,i*j),end="")
     print("")'''
'''import turtle as t
def draw_fiveStars(leng):
    count = 1
    while count <=5:
        t.forward(leng)
        t.right(144)
        count += 1
    leng +=10
    if leng <=100:
     draw_fiveStars(leng)
def main():
        t.penup()
        t.backward(100)
        t.pendown()
        t.pensize(3)
        t.pencolor('yellow')
        segment = 400
        draw_fiveStars(segment)
        t.exitonclick()
if __name__ == '__main__':
     main()'''

