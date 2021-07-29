K=[]
n = int(input(""))
for i in range (0,n) :
    k = int(input(""))
    K.append(k)
K.sort()
K=K[::-1] # ใช้ .reverse มัน เรียงไม่สมบูรณ์ จึงใช้รูปนี้แทน
for i in range(0, len(K)):
    print(K[i])