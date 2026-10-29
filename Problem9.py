
# Problem 9: Electricity Bill with Progressive Tiers

# Part (a)
def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    cost = tier1 * 480 + tier2 * 610 + tier3 * 730
    total = (cost + 2000) * 1.10

    return round(total)


# Part (b)
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh:>4} kWh -> {bill:>9,} riel (≈ {usd:>7.2f} USD)")


# Part (c)
kwh = float(input("Enter your monthly electricity consumption (kWh): "))
bill = electricity_bill(kwh)

if bill is None:
    print("Invalid consumption. Please enter a non-negative number.")
else:
    print(f"Your electricity bill is {bill:,} riel.")
    print(f"Approximately {bill / 4100:.2f} USD.")
