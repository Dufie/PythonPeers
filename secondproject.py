#This program converts temperatures in Fahreinheit to Degree Celsius

print ("Enter the temperature in Fahrenheit")
fahrenheit = float(input())

#Converting from Fahrenheit to Degree Celsius
degreeCelsius = (fahrenheit -32) * 5/9

#rounding to two decimal places
degreeCelsius = round(degreeCelsius, 2)

print ("The temperature is " + str(degreeCelsius) + " degree celsius")