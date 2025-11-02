# Convert USD to EUR
rate = 0.92 # conversion rate
for usd in range(1,6):
    eur = usd * rate
    print(usd, "USD=",round(eur,2),"EUR")
else:
    print("conversion complete")


