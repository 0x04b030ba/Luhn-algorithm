sum_odd = 0
sum_even = 0

while True:
    card_number = input("Card number? ")
    card_number = card_number.replace("-","")
    card_number = card_number.replace(" ","")
    card_number = str(card_number)


    card_number = card_number[::-1]

    for i in card_number[::2]:
        sum_odd += int(i)


    for i in card_number[1::2]:
        i =int(i) *2
        if i>=10:
            sum_even += (1 + (i % 10))
        else:
            sum_even += i



    total = sum_odd+sum_even

    if total%10==0:
        print("VALID")
    else:
        print("INVALID")

    #reset
    card_number = ""
    i = ""
    sum_odd = 0
    sum_even = 0
