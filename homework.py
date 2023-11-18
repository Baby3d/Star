# *Домашка*



# -Задание 1-

# Наш пользователь предприимчивый юный бизнесмен, который захотел приобрести парочку рабов для своих прекрасных хлопковых полей.

# Один раб стоит 3000 грн в месяц в аренду.

# Реализовать программу, в которой пользователь вводит свой бюджет, и на сколько месяцев хочет арендовать крепостных. 

# По итогу, ему должно вывестись, сколько у него останется денег после покупки этого дивного аппарата дешевой рабочей силы.

# one_slave = 3000
# budget = int(input())#10 000
# month = int(input())


# #10 000 - 9 000 = 1 000
# slave_cost_sum = one_slave * month#9000
# print(f"Price: {slave_cost_sum}")
# print(budget - slave_cost_sum )




# -Задание 2-

# Магазин печенья:

# Печенье стоит 120 грн за килограмм. Пользователь вводит сколько килограмм он хочет купить печенья. По итогу, мы должны вывести сколько ему нужно заплатить.


# -Задание 3-

# Пользователь вводит, сколько дней он отработал. Наша задача вывести, сколько это в неделях.


#28 - days
#7 - week


#####worked_days = int(input())
#week = 7

#weeks_sum = worked_days // week
#print(weeks_sum)




# -Задание 4-

# Текущий курс доллара 37 грн. Пользователь вводит, сколько у него есть денег в долларах, после чего вывести, сколько это в гривнах.




##########homework 09.27.23


# dollar_price = 37
# client_dollars = int(input())
# print(str(dollar_price * client_dollars) + " grn." )

############################################################

# one_day_company = 1200
# work_day_company = int(input())
# full_income = one_day_company * work_day_company
# print(full_income)

############################################################

# buyer = 20000
# apartment = int(input())
# buy = buyer // apartment
# print(buy)


#############################################################

#one_worker = 3_000
#all_employees = int(input())
#salary = one_worker * all_employees
#print(salary)
####################################################

# print("Enter payment for one worker: ")
# one_worker = int(input())

# print("Enter count of workers: ")
# all_employees = int(input())

# salary = one_worker * all_employees

# print(salary)

#############################################
# print(" Enter file size : ")
# file = int(input())#mb

# print(" Enter speed please : ")
# user_megabytes = int(input())

# download = file / user_megabytes

# print(download)


############################################

# print(" Enter your balance: ")
# balance = int(input())

# print(" Enter price please :")
# keyboard_cost = int(input())

# quantity = balance //keyboard_cost

# print(quantity)

############################################
# 
#

                   ### HOMWORK 09.30.23 ###

# print("Please indicate your gas consumption:")
# gasoline_consumption_per_100_km = int(input())#15 (на 100 км)
 
# print("Please indicate how many kilometers you have traveled:")   
# mileage = int(input())#300



# print("Your total expenses:")
# print( (mileage / 100) * gasoline_consumption_per_100_km )          # Bentley client program was introduced to calculate mileage and fuel consumption.

# print("Thank you! See you soon!")
############################################

# print("Enter the cost of one MacBook:")
# cost_of_macbook = int(input())

# print("Enter quantity sold:")
# sold_macbooks = int(input())

# print("Your total earnings:")
# print(cost_of_macbook * sold_macbooks)             # total value of client income.

# print("Thank you and see you soon!")
#############################################

# print("Cost of one cubic meter of water:")
# cost_of_water = int(input())

# print("Please enter water consumption data:")
# water_use = int(input())

# print("Your total payment:")
# print(cost_of_water * water_use)          #a program for calculating payments for water use has been compiled.

# print("Thank you very much for your cooperation, see you soon!")

####################################

# waste_of_gigabytes_today = int(input())
# cost_of_100_megabytes = int(input())

# print(waste_of_gigabytes_today / 100 * cost_of_100_megabytes)

#####################################

# one_bun = int(input())
# one_sausage = int(input())

# hot_dog_count = int(input())
# print((one_bun + one_sausage )* hot_dog_count)



#############################################

# number_of_bricks = int(input())    # 1000
# needed_to_build_bricks = int(input())  # 30

# print( number_of_bricks // needed_to_build_bricks )

##########################################

# number_of_torches = int(input())
# burning_torch_time = int(input())

# print(number_of_torches * burning_torch_time)
##########################################
# sleeps_at_night = int(input())  
# quiet_time = int(input())

# print((sleeps_at_night * 60 ) + quiet_time)
##########################################

# money_for_macbook = int(input())
# price = int(input())

# print(money_for_macbook //price ) 

############################################

# a = "32"

# print(type(a))


# a = int(a)


# print(type(a))

#################################################

# a = 32

# print(type(a))

# a = str(a)

# print(type(a))


####################################################



# Нужно реализовать приложение "Калькулятор постройки домов".

# Пользователь вводит данные о:


# - Сколько у нас всего есть кирпичей. 

# - Кол-во кирпичей для постройки одной стены.

# - Требуемом кол-во установленных стен.

# - Сколько дней строится одна стена.

# - За сколько дней НУЖНО выполнить всю постройку.


#Вывести сколько осталось керпичей для постройки
#Вывести сколько осталось дней до конца плана


#### контрольна робота 10/05/23
############ calculator
# print("Enter how many bricks you have:")

# how_many_bricks = int(input())

# print("Enter the number of bricks to build one wall:")
# bricks_for_one_wall = int(input())

# print("Required number of instlled wall:")
# number_of_instlled_wall= int(input())#3

# print("how many days does it take to build one wall:")
# building_one_wall = int(input())#2

# print("How many days we have?")
# count_free_days = int(input())#free days for building#20

100#сколько у тебя есть деняг
20#цена яблока
3#сколько яблок нужно купить
# 100 - 20*3 = 40


#
#       (сколько дней нужно для постройки стен)
# print(building_one_wall * number_of_instlled_wall )
#print(count_free_days - (building_one_wall * number_of_instlled_wall) )


################################################################

# print("Enter the duration of your trip:")
# minutes_of_travel = int(input())

# print("Enter the duration of one song:")
# song_duration = int(input())

# print("Your number of songs to your destination:")
# print(minutes_of_travel / song_duration) 

# print("Thank you very much for reaching out and have a nice trip!")




#############################################################################


# print("Indicate the amount of flour you have:")
# gram_flour = int(input())

# print("Indicate how many grams of flour are needed for one bread:")
# need_amount_of_flour = int(input())

# print("Indicate what the cost of one bread will be:")
# cost_of_bread = int(input())
# all_bread = gram_flour // need_amount_of_flour

# print("Your quantity of cooked bread:")
# print(gram_flour // need_amount_of_flour)

# print("Your earnings from selling bread:")
# print( all_bread * cost_of_bread)

# print("Thank you for contacting us, see you soon.")

#############################################################################


# sleep_hours = int(input())
# working_hours = int(input())
# one_episode_of_the_series = 1.5
# day = 24
# print((day-(sleep_hours + working_hours) ) /  one_episode_of_the_series)
# #Мы спим 8 часов
# #Мы работаем 8 часов
# #Серия длится 1.5 часа
# #По итогу мы посмотрели: 5.,,, серий

# print("мы спим " + str(sleep_hours))
# print("мы работаем " + str(working_hours ))
# print("серия длится " + str(one_episode_of_the_series))
# print("по итогу мы посмотрели: " + str((day-(sleep_hours + working_hours))  // one_episode_of_the_series))

###############################################################################


# free_disk_space = int(input())  
# installer = int(input())  
# result = free_disk_space  - installer
# print(str(result) + " MB")

################################################################

# rental_per_day = int(input())
# apartment_delivery_days = int(input())

# print(rental_per_day * apartment_delivery_days)

########################################
# now_year = int(input())
# print("Per day:" + str(now_year * 365))
# print("Per month:" + str(now_year * 12))
# print("Per week:" + str(now_year * 48))
# print("Per hour:" + str(now_year * 365 * 24))
###############################################


# age = int(input())
# if age >= 55 :
#     print("That's right, retirement age") 

###########################################################

    #  True  FALSE   False
# print(1 == 1 and 3 >= 2)# &&
# print(2 == 2 or 3 == 2)#True


# outside_temperature = int(input())
# if outside_temperature > 0 and outside_temperature <=14 :
#     print("cool")
 
# if outside_temperature >= 15 and outside_temperature <= 29:  
#     print("normal")


# if outside_temperature > 30 and outside_temperature <= 45:
#     print("I'm a kebab")


# if outside_temperature < 0:
#     print("pay for heating again")      

#######################################################

# cubic_meters_of_water_per_month = int(input())
# if cubic_meters_of_water_per_month > 50 :
#     print("you have exceeded the monthly norm")
##################################################

# programmer_homework = int(input("Enter count homework: "))
# if programmer_homework > 3 and programmer_homework <= 4 :
#     print("Well done!")

# if programmer_homework > 5 and programmer_homework <= 9 :
#     print("you're handsome!")

# if programmer_homework > 10 and programmer_homework <=15 :
#     print("promoted to senior!")   

# if programmer_homework < 3 :
#     print("Goodbye!")     
######################################################

# pay = input("Enter your rank (Junior, Middle or Senior): ")

# if pay == "junior":
#     print("your salary is 3600 dollars")
# pay = input("Enter your rank (Junior, Middle or Senior): ")    
# if pay == "middle":
#     print("your salary is 7200 dollars")    
# pay = input("Enter your rank (Junior, Middle or Senior): ")
# if pay == "senior":
#     print("your salary is 9800 dollars")   

########################################################################


# season = int(input("We introduce all seasons of the year Winter Spring Summer and Autumn):"))#3
# #season = 3

# if season == 1:#False
#     print("Winter")# :(  ->  (:

# if season == 2:
#     print("Spring")

# if season == 3:
#     print("Summer")   

# if season == 4:
#     print("Autumn")

# if season > 4:
#     print("Sorry, you entered the information incorrectly, please try again!")   
# ##################################################################################

# Для установки нашей программы требуется ОС MacOS, и 200мб свободного места.

# Пользователь вводит свою ОС, и сколько у него свободного места, если ОС совпадает,
# а памяти хватает, выводим сообщение об успешной установке.


# os_= input()
# storage = int(input())

# if os_ == "MacOS" and storage >= 200  :
#     print("Thank you, your installation was successful")
##################################################################3


# print("Please enter your age: you must be over 18 years old !")
# age = int(input())

# print("Enter your balance:")
# balance = int(input())

# if age >= 18 and balance >= 150:
#     print("Thank you for a successful purchase!")

# if age < 18 or balance < 150:
#     print("Sorry, your purchase cannot be processed, you are under 18 years of age, or you have insufficient funds.")

######################################################################

# print("Please enter your width:")
# width = int(input())

# print("Please enter your height:")
# height = int(input())

# if width >= 150 and height >= 200:
#     print("Thank you very much, the sizes fit")

# if width < 150 or height < 200: 
#     print("Sorry, your sizes don't fit!")   

############################################################################
 
    

    