# Currency Converter
with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    data = line.split("\t")
    currencyDict[data[0]] = data[1]

amount = float(input("Enter the amount: \n"))
print("Enter the name of currency you want to convert this amount? Available Options: \n")
[print(item) for item in currencyDict.keys()]
currency = input("please enter the name of currency: \n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")