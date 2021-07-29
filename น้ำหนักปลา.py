Mx=["max","MAX","Max","maX""MAx","MaX","mAX","mAx"]
Mn=["min","MIN","Min","miN""MIn","MiN","mIN","mIn"]
K=[]
while True:
    k = int(input("กรอกน้ำหนักปลา>>>> "))
    if k != 0 : K.append(k)
    elif k ==0 :
      MM=str(input("รูปแบบการจัดเรียง(max/min)>>> "))
      if MM in Mx:
        K.sort()
        K=K[::-1] # ใช้ .reverse มัน เรียงไม่สมบูรณ์ จึงใช้รูปนี้แทน
        for i in range(0, len(K)):
            print(K[i], end = ' ')
        break
      elif MM in Mn :
        K.sort()
        for i in range(0, len(K)):
            print(K[i], end = ' ')
        break