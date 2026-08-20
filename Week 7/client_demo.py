import requests

API_URL = "http://127.0.0.1:8000/query"

def simulate_frontend_query(query_text):
    print(f"\n[Frontend Integration] Query Sent: '{query_text}'")
    payload = {"query": query_text}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        print(f"[Backend Response Code]: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            if data.get("found"):
                print(f"[UI Output - Answer]: {data.get('answer')}")
                print(f"[UI Output - Score]: {data.get('score'):.4f}")
            else:
                print(f"[UI Alert Guardrail]: {data.get('answer')}")
        else:
            print(f"[UI Validation Error]: {response.json()}")

    except Exception as e:
        print(f"[Connection Error]: Make sure FastAPI server is running! Details: {e}")

if __name__ == "__main__":
    print("=== Week 7 Integration Demo Flow ===")
    simulate_frontend_query("What is the primary topic of this document?")
    simulate_frontend_query("Who won the football world cup?")
    simulate_frontend_query("hi")