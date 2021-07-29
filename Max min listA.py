def mami(listA):
    print("เลขที่มีค่ามากที่สุด คือ ",max(listA))
    print("เลขที่มีค่าน้อยที่สุด คือ ",min(listA))


listA = []
while True :
    num = int(input("กรอกเลขครับ (ยุติการกรอกเลข พิม 99999)>>"))
    if num != 99999 : listA.append(num)
    elif num == 99999 : break
mami(listA)