sudo docker build -t stock-market-app .

sudo docker run -p 5000:5000 --env-file .env stock-market-app
