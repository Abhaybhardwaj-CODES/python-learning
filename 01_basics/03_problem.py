Time = int(input("Enter the time in seconds: "))
Hours = Time // 3600
Minutes = (Time % 3600) // 60
seconds = Time % 60
print("Time in hours:", Hours, "hours" )
print("Time in minutes :", Minutes, "minutes")
print("Time in seconds:", seconds, "seconds")