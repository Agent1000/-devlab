def makeresult(listA):
    avg = sum(listA)/len(listA)
    listA.sort()
    mid = len(listA)//2
    resu = (listA[mid]+listA[~mid])/2
    print("ค่าเฉลี่ย = ",avg)
    print("เลขมัธยฐาน = ",str(resu))
    print("ฐานนิยม = ",(max(set(listA),key = listA.count)))


listA = []
n = int(input("จำนวนข้อมูลที่ต้องการกรอก >> "))
for i in range (0,n) :
    num = int(input("กรอกเลขครับ >>"))
    listA.append(num)
makeresult(listA)