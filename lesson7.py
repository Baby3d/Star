# print(3 > 7)



#            False
#      False  ?   True
# print(2 >= 3 and 5 == 5)

# print( 5 > 3 or 4 > 3)

# print(3+5)
#логические операторы: >=, <=, == ... and or
#арифмитические операторы: +, -, *...

#################################

# time = int(input())#4
# #
# #      False         True
# #    -10 >= 1     -10 <= 6


# #         6
# if time >= 1 and time <= 6 :#
#     print("Night")
# if time >= 7 and time <= 12:
#     print("Morning")
# if time >= 13 and time <= 16:
#     print("Day")
# if time >= 17 and time <= 21:
#     print("Evening")        

#################################


shop_meet_have_kg = 20#сколько мяса кг в магазине
shop_kg_meet_price = 150#сколько стоит кг мясa

user_meet_need_kg = int(input())#сколько пользователю нужно килограмм мяса#20
user_balance = int(input())#сколько у него есть деняк#160

need_to_pay = user_meet_need_kg * shop_kg_meet_price
print(need_to_pay)

if user_balance >= need_to_pay and user_meet_need_kg <= shop_meet_have_kg:
    print("You bought meat, thank you for your purchase!")

if user_balance < need_to_pay and user_meet_need_kg > shop_meet_have_kg:    
    print("Unfortunately you don't have enough money, please go to the work and we don't have so much meet")
if user_balance < need_to_pay and shop_meet_have_kg >= user_meet_need_kg:
    print("You dont have maney, sorry!")
if user_balance > need_to_pay and shop_meet_have_kg < user_meet_need_kg:
    print("Sorry, unfortunately,we don't have that kind of kilogram of meat!")    






