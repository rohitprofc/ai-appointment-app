import random
import csv

def generate_indian_phone_number():
    provider_codes = ["7", "8", "9", "6"]
    provider_code = random.choice(provider_codes)

    subscriber_number = str(random.randint(0, 999999999)).zfill(9)

    indian_phone_number = provider_code + subscriber_number

    return indian_phone_number


phone_number = []
for _ in range(1400):
    phone_number.append(generate_indian_phone_number())
with open("indian_phone_numbers.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Phone_Number"])
    for number in phone_number:
        writer.writerow([number])
