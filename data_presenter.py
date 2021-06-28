data = open('CupcakeInvoices.csv')
all_total = 0
# for line in data:
#     line = line.rstrip('/n').split(',')
#     quantity = int(line[3])
#     price = float(line[4])
#     total = quantity * price
#     all_total += total
#     print(line[2], round(total, 2))
# print(round(all_total, 2))

chocalate_total = 0
strawberry_total = 0
vanilla_total = 0

for notline in data:
    notline = notline.rstrip('/n').split(',')
    notquantity = int(notline[3])
    notprice = float(notline[4])
    nottotal = notquantity * notprice
    if notline[2] == 'Chocolate':
        chocalate_total += nottotal
    elif notline[2] == 'Strawberry':
        strawberry_total += nottotal
    else:
        vanilla_total += nottotal
print('Chocolate: ', chocalate_total, 'Strawberry: ',
      strawberry_total, 'Vanilla: ', vanilla_total)
data.close()
