f=int(input("Enter feet: "))
inc=int(input("Enter inches: "))

total_inc=(f*12)+inc
hight_cm=total_inc*2.54
print(f"Hight in centemeter is: {hight_cm:.2f} cm")