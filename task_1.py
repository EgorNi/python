from sys import argv


prod_hours, coin_per_hour, prize = argv[1:]
counting = int(prod_hours) * int(coin_per_hour) + (int(coin_per_hour) / 100) * int(prize)
print(f"Your salary is: {counting}")
