1. Clone the repository
2. Run the Docker file
    - docker build -t receipt-processor .
    - docker run -p 5000:5000 receipt-processor
4. Flask Application will run on port 5000
5. Use postman or curl command to test the API calls
6. Also added validation for the json body


example
1. POST call - http://127.0.0.1:5000/receipts/process

    request body -
        {
          "retailer": "Target",
          "purchaseDate": "2022-01-01",
          "purchaseTime": "13:01",
          "items": [
            { "shortDescription": "Mountain Dew 12PK", "price": "6.49" },
            { "shortDescription": "Emils Cheese Pizza", "price": "12.25" },
            { "shortDescription": "Knorr Creamy Chicken", "price": "1.26" },
            { "shortDescription": "Doritos Nacho Cheese", "price": "3.35" },
            { "shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00" }
          ],
          "total": "35.35"
        }
    
    
    response body -
        {
            "id": "0777967c-72d4-45f6-88d3-fa637784a630"
        }



2. GET call - http://127.0.0.1:5000/receipts/0777967c-72d4-45f6-88d3-fa637784a630/points
    response body -
        {
            "points": 28
        }
