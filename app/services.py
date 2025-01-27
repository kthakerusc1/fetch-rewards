import math
from app.models import in_memory_db
import uuid

def calculate_points(receipt):
    try:
        points = 0
        name = receipt.get("retailer", "")
        if name == "":
            raise ValueError("Retailer name missing or invalid")

        # Rule 1: One point for every alphanumeric character in the retailer name
        points += sum(c.isalnum() for c in receipt.get("retailer", ""))

        # Rule 2: 50 points if the total is a round dollar amount
        total = float(receipt.get("total", 0))
        if total < 0:
            raise ValueError("Total value is missing or invalid")
            
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
            if desc == "":
                raise ValueError("Item Description is missing")
            if float(item.get("price", 0)) < 0:
                raise ValueError("Price value is missing or invalid")
            if len(desc) % 3 == 0:
                price = math.ceil(float(item.get("price", 0)) * 0.2)
                points += price

        # Rule 6: 6 points if the purchase date day is odd
        date = receipt.get("purchaseDate", "")
        if date == "":
            raise ValueError("Date is missing or invalid")
        year, month, day = date.split("-")
        if int(day) % 2 != 0:
            points += 6
        if int(day) > 31 or int(day) < 1 or int(month) > 12 or int(month) < 1 or (int(day) > 29 and int(month) == 2):
            raise ValueError("Date is missing or invalid")

        # Rule 7: 10 points if the purchase time is between 2:00 PM and 4:00 PM
        time = receipt.get("purchaseTime", "")
        if time == "":
            raise ValueError("Purchase Time is missing or valid")
        else:
            time = time.split(":")
            hour, minute = int(time[0]), int(time[1])
            if 14 <= hour < 16:
                points += 10
            if hour < 0 or hour > 23 or minute > 59 or minute < 0:
                raise ValueError("Purchase Time is missing or valid")

        receipt_id = str(uuid.uuid4())
        in_memory_db[receipt_id] = points
        return receipt_id
    except Exception as e:
        raise e
    
def get_receipt_points(receipt_id = ""):
    try:
        if receipt_id in in_memory_db:
            points = in_memory_db[receipt_id]
            return points
        raise ValueError("Receipt id not found")
    except Exception as e:
        raise e
