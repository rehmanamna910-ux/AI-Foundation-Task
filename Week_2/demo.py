import csv
import json
import os
import requests
from dotenv import load_dotenv

# 1. Load Environment Variables (.env File)
load_dotenv()
api_key = os.getenv("MY_API_KEY")
print(f"Loaded API Key: {api_key}")

# 2. Read CSV Data without Pandas
print("\n--- Reading Data ---")
raw_data = []
with open("Week_2/input_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        raw_data.append(row)

print("Original Data:")
for row in raw_data:
    print(row)

# 3. Clean Data (Removing rows where 'name' or 'email' is empty)
print("\n--- Cleaning Data ---")
cleaned_data = []
for row in raw_data:
    if row["name"].strip() != "" and row["email"].strip() != "":
        cleaned_data.append(row)

print("Cleaned Data (Missing rows removed):")
for row in cleaned_data:
    print(row)

# 4. API Request (Fetching mock user location/city)
print("\n--- Fetching API Data ---")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
    if response.status_code == 200:
        api_data = response.json()
        print("API Call Successful!")

        # Mapping API cities to cleaned records
        for i, row in enumerate(cleaned_data):
            city = api_data[i % len(api_data)]["address"]["city"]
            row["assigned_location"] = city
    else:
        print(f"API Error: Status {response.status_code}")

except Exception as e:
    print(f"Error connecting to API: {e}")

# 5. Save Output to JSON
print("\n--- Saving Output ---")
with open("output_data.json", "w") as json_file:
    json.dump(cleaned_data, json_file, indent=4)

print("Output successfully saved to 'output_data.json'!")