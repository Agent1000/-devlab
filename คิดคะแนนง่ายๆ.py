try:
    score = int(input("กรอกคะแนน >> "))
    if score<0:
        raise Exception("คะแนนติดลบไม่ได้นะ")
    elif score>=0 and score <=25:
        print("fail")
    elif score>=26 and score <=50:
        print("good")
    elif score>=51 and score <=75:
        print("very good")
    elif score>=76 and score <=100:
        print("excellent")
    elif score > 100:
        raise Exception ("คะแนนไม่เกิน 100 ครับ")

except Exception as e:
    print(e)