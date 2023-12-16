temperature=input("enter the from temperature (C for celsius or F for farenheit(in CAPITAL))")
TEMP=["F","C"]
if temperature not in TEMP:
    print("invalid")
elif temperature =="C":
    celsius=input("enter the temperature in celsius : ")
    farenheit=(float(celsius)*9/5)+32
    print(f"farenheit for given {celsius}C is",farenheit)
elif(temperature=="F"):
    farenheit1=input("enter the temperature in farenheit : ")
    celsius1=(float(farenheit1)-32)*5/9
    print(f"celsius for given {farenheit1}F is",celsius1)