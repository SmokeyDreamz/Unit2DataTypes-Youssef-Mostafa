""" x = 3
y = float(3)
print(x,y)

values = [100,2.23,5,7,2,30,53]
print(values)
for i in values:
    print(i)

    print(values[0])
print(values[6]) """

""" def message(input):
    print(input)

input("Input a sentence")

x = "input()"
y= x.split( )
z = y[0]
print(y)
print(z) """



""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

#word counter challenge
""" count_words= input("WRITE YOUR SENTENCE TO SEE THE WORD COUNT")
count_words= count_words.split()
print(len(count_words))
 """



""" x = "Class of 2029"
print(f"Welcome, {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """


#even or odd number challenge

""" even_or_odd = input("WRITE A NUMBER")
if int(even_or_odd) % 2 ==0:
    print("YOUR NUMBER IS EVEN")
else:
    print("YOUR NUMBER IS ODD") """

#tip calculator challenge

""" bill = input("WHAT IS THE BILL AMOUNT?")
service = input("HOW WOULD YOU RATE THE SEVICE? BAD, OKAY, GOOD, OR GREAT?")
if service == "BAD":
    print(bill)
elif service == "OKAY":
    print(float(bill) * 1.15)
elif service == "GOOD":
    print(float(bill) * 1.20)
elif service == "GREAT":
    print(float(bill) * 1.25) """

#factor caluclator challenge

""" factor= 2
list_of_factors = [1]
number = input("WRITE THE NUMBER YOU WANT TO FACTOR")
number = int(number)

for i in range(number):
        if (number % factor) ==0:
            second_factor_list = [factor]
            list_of_factors.append(second_factor_list)
        factor = factor + 1
print(f"THE FACTORS OF {number} ARE {list_of_factors}") """


#GCF or greatest common factor caluclator challenge


#DON"T USE THIS CODE. DOESN"T WORK. Use as reference for new code


""" factor = 2
factor_list = [1]
first_number = input("WRITE ONE NUMBER")
second_number = input("WRITE ANOTHER NUMBER")
first_number = int(first_number)
second_number = int(second_number)

for i in range(first_number + second_number):
    if (first_number % factor ==0) and (second_number % factor ==0):
        new_factor_list = [factor]
        factor_list[0] = (new_factor_list)
        factor = factor + 1
print(f"THE GREATEST COMMON FACTOR OF {first_number} AND {second_number} IS {factor_list}") """

#DON"T USE THIS CODE. DOESN"T WORK. Use as reference for new code
        