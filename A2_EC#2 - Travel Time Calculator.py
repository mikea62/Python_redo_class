

print("Travel Time Calculator")
print()
miles = input("Enter miles: ")
mph = input("Enter miles per hour: ")
hours = int(miles) / int(mph)
mins = int(miles) % int(mph)
print()
print("Estimate Travel Time: ")
print("Hours: ", int(hours))
print("Minutes: ", mins)