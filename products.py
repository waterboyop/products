products = []

with open ('product.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品, 價格' in line:
            continue #繼續 (跳過這一回)
        name, price = line.strip().split(',')
        products.append([name, price])
    print(products)



while True:
    name = input('input the product name: ')
    if name == 'q':
        break
    price = input('please input the product price: ')
#    p = []
#    p.append(name)
#    p.append(price)
    products.append([name, price])
print(products)
#print(cost)

with open ('product.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

