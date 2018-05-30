hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hours = float(hrs)
    rate=float(rate)
except:
    print("Error,please enter numeric input")
    quit()

print("hours:",hours,"rate:",rate)
if hours>40:
    reg = hours*rate
    overtime=(hours-40.0)*(rate*0.5)
    pay=reg+overtime
else:
	pay = hours*rate

print(pay)
