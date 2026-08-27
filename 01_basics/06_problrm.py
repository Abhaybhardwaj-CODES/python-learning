Principal_amount = float(input("Enter the principal amount: "))
Rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
Time = float(input("Enter the time (in years): "))
Amount_after_time = Principal_amount * (1 + (Rate_of_interest / 100) * Time)
print(f"The amount after {Time} years is: {Amount_after_time}")


compound_interest = Amount_after_time - Principal_amount
print(f"The compound interest after {Time} years is: {compound_interest}")