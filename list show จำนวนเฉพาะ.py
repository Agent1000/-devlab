def SpecialNo(listA):
   SN=['2','3','5','7','11','13','17','19','23','29','31','37','41','43','47','53','59','61','67','71','73','79','83','89','97']
   for i in range(0,len(listA)):
    if listA[i] in SN:
        listA.pop[i]
        listA.insert(i,"true")
    print[listA[i]]

   #SN แทนจำนวนเฉพาะ

listA = []
while True :
    num = int(input("กรอกเลขครับ (ยุติการกรอกเลข พิม 111)>>"))
    if num != 111 : listA.append(num)
    elif num == 111: break
   
SpecialNo(listA)
