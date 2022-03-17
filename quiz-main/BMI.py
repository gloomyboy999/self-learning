height = float(input("請輸入身高(cm): "))
weight = float(input("請輸入體重(kg): "))
height = height / 100
bmi = weight / height**2  
if bmi >= 35:
    print("重度肥胖")
elif 35 > bmi >= 30:
    print("中度肥胖")
elif 30 > bmi >=27:
    print("輕度肥胖")
elif 27 > bmi >= 24:
    print("過重")
elif 24 > bmi >= 18.5:
    print("正常範圍")
else:
    print("體重過輕")