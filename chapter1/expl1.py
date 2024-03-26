print  ('hello')
print ("world")

userAge = 0
userAge, userName = 30, 'Pendo'

x = 5
y = 6
x = y
print("x =", x)
print("y =", y)

userAge = 36
mobileNumber = 789065756

userHeight = 12.3
userWeight = 60.7
userName = 'Soso'.upper()

brand = 'Apple'
exchangeRate = 1.2345
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print(message)
message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR' .format('Apple', 1299, 1.2345)
message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR' .format('Apple', 1299, 1.2345)

myName = input('enter your name:')
