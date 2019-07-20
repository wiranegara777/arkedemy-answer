import math

def arkaFood(price,voucher,distance,tax):
    discount = 0
    if voucher == "ARKAFOOD5":
        if price >= 50000:
            discount = 0.5 * price
            if discount > 50000:
                discount = 50000
    elif voucher == "DITRAKTIRDEMY":
        if price >= 25000:
            discount = 0.6 * price
            if discount > 30000:
                discount = 30000
    if distance <= 1.5:
        deliv_price = 5000
    else:
        distance -= 1.5
        deliv_price = 5000 + 3000 * math.ceil(distance)
    if tax != "False":
        total = price-discount + (tax/100) * (price-discount) + deliv_price
    else:
        total = price-discount +  deliv_price
    return total

total = arkaFood(75000,"ARKAFOOD5",5,"False")
print("Rp. {0:,g}".format(total))