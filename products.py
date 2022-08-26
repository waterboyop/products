products = []
#cost = 0
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

with open ('product.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

