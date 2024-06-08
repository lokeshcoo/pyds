import pandas as pd
from prophet import Prophet

def predict_stock_price(csv_file, n):
    # Step 1: Load stock data from CSV file
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'].str[:-6])
    # Step 2: Preprocess the data
    df = df.rename(columns={'Date': 'ds', 'Close': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    
    # Step 3: Initialize Prophet model
    model = Prophet()
    
    # Step 4: Train the model
    model.fit(df)
    
    # Step 5: Make future predictions
    future = model.make_future_dataframe(periods=n)
    forecast = model.predict(future)
    
    # Step 6: Return predictions in a DataFrame
    return forecast[['ds', 'yhat']].tail(n)

# Example usage:
csv_file = r'C:\Users\ASUS\Desktop\major_project\code\data\AAPL.csv'
n_days = 30
predictions = predict_stock_price(csv_file, n_days)
print(predictions)
