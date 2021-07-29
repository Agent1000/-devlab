K=[]
for i in range (0,5) :
    k = int(input("กรอกเลขครับ 5 ครั้ง >>"))
    K.append(k)
K.sort()
K=K[::-1] # ใช้ .reverse มัน เรียงไม่สมบูรณ์ จึงใช้รูปนี้แทน
print("ผลการเรียงลำดับ")
for i in range(0, len(K)):
    print(K[i])
    