money_value = int(input("How much money will you withdraw? "))
money_received = 0
hundred_bill = 0
fifth_bill = 0
twenty_bill = 0
ten_bill = 0
five_bill = 0
one_bill = 0
while(True):
    if(money_value>= 100):
        hundred_bill +=1
        money_received+= 100
        money_value -= 100
    else:
        break
while(True):
    if(money_value>= 50):
        fifth_bill+=1
        money_received+=50
        money_value-=50
    else:
        break
while(True):
    if(money_value>=20):
        twenty_bill +=1
        money_received +=20
        money_value-=20
    else:
        break
while(True):
    if(money_value>=10):
        ten_bill +=1
        money_received+=10
        money_value-=10
    else:
        break
while(True):
    if(money_value>=5):
        five_bill+=1
        money_received=5
        money_value-=5
    else:
        break
while(True):
    if(money_value>=1):
        one_bill+=1
        money_received+=1
        money_value-=1
    else:
        break
if(one_bill>=1):
    print(f"You got {one_bill} 1 dollar bills." , end=" ")
if(five_bill>=1):
    print(f"You got {five_bill} 5 dollar bills." , end=" ")
if(ten_bill>=1):
    print(f"You got {ten_bill} 10 dollar bills.", end=" ")
if(twenty_bill>=1):
    print(f"You got {twenty_bill} 20 dollar bills.", end=" ")
if(fifth_bill>=1):
    print(f"You got {fifth_bill} 50 dollar bills.", end=" ")
if(hundred_bill>=1):
    print(f"You got {hundred_bill} 100 dollar bills.", end=" ")
print(f"Totalling {money_received} dollars.")