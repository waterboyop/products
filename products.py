products = []
#cost = 0
while True:
    name = input('input the product name: q for exit ')
    if name == 'q':
        break
    price = int(input('please input the product price: '))
#    p = []
#    p.append(name)
#    p.append(price)
    products.append([name, price])
print(products)
#print(cost)