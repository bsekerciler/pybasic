__author__ = 'bsekerciler'
#encoding: UTF-8

#########################################
#                                       #
#                                       #
#       Python 3x for Beginners         #
#                                       #
#########################################

work_day = 20
bus_pay = 1.5
bus_pay2 = 1.5
#1.5 can be dollar, cent, euro.

total_price = work_day * (bus_pay + bus_pay2)
#this is our formula.

print ("-"*25)
#just a fancy :)
print ("You work\t:", work_day , "day")
#first, we created a dialog with "" symbols. Second, we printed the value on the screen.
print ("Bus Pay for Go to Work\t:", bus_pay)
print ("Bus Pay for Come From Work\t:", bus_pay2)
print ("-"*25)
#a fancy too
print ("Your Total Monthly Price\t:", total_price)
#This part our result. It, printed the formula on the screen.
