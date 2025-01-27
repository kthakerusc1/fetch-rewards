1. Clone the repository
2. Run the Docker file
    - docker build -t receipt-processor .
    - docker run -p 5000:5000 receipt-processor
4. Flask Application will run on port 5000
5. Use postman or curl command to test the API calls
6. Also added validation for the json body for checking the following
   - Purchase Time
   - Date
   - Price
   - Total
   - Description
