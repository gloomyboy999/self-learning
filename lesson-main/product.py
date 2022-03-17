products = []
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = input("請輸入商品價格: ")
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
    # 快速寫法
    # p = [name, price]
    # products.append(p)
    # 最快速寫法
    # products.append([name, price])
print(products)

for p in products:
    print(p[0], "的價格是", p[1])