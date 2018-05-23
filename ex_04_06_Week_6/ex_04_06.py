def computepay(hours,rate):
    if hours>40:
        reg = hours*rate
        overtime=(hours-40.0)*(rate*0.5)
        pay=reg+overtime
    else:
    	pay = hours*rate
    return pay

hrs = input("Enter Hours:")
r = input("Enter Rate:")
try:
    hours = float(hrs)
    rate=float(r)
except:
    print("Error,please enter numeric input")
    quit()

print("hours:",hours,"rate:",rate)


p = computepay(hours,rate)
print(p)
