import math

def calculate_points(receipt):
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in receipt.get("retailer", ""))

    # Rule 2: 50 points if the total is a round dollar amount
    total = float(receipt.get("total", 0))
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items
    items = receipt.get("items", [])
    points += (len(items) // 2) * 5

    # Rule 5: Points for item descriptions being multiples of 3
    for item in items:
        desc = item.get("shortDescription", "").strip()
        if len(desc) % 3 == 0:
            price = math.ceil(float(item.get("price", 0)) * 0.2)
            points += price

    # Rule 6: 6 points if the purchase date day is odd
    day = int(receipt.get("purchaseDate", "2022-01-01").split("-")[2])
    if day % 2 != 0:
        points += 6

    # Rule 7: 10 points if the purchase time is between 2:00 PM and 4:00 PM
    time = receipt.get("purchaseTime", "00:00").split(":")
    hour, minute = int(time[0]), int(time[1])
    if 14 <= hour < 16:
        points += 10

    return points
