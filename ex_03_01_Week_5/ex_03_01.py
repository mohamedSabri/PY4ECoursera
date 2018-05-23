hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r=float(rate)

if h>40:
    reg = h*r
    overtime=(h-40.0)*(r*0.5)
    pay=reg+overtime
else:
	pay = h*r

print(pay)
