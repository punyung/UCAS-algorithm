def discounts(price,rate):
    final_price = price * rate
    print ('try 全局变量 old_price的值',old_price)
    return final_price
old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('discounts之后的价格', new_price)