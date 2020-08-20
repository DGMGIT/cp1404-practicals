TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_number = int(input("Which tariff 11 or 31: "))
if tariff_number == 11:
    price_per_kWh = TARIFF_11
else:
    price_per_kWh = TARIFF_31
# price_per_kWh = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

bill = billing_days * price_per_kWh * daily_use

print(f"Estimated bill: ${bill:.2f}")
