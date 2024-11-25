import requests

def fetch_living_expenses(state):
    try:
        url = f"http://127.0.0.1:8000/get_living_expenses/{state}"
        response = requests.get(url)
        response.raise_for_status()  # Raise error if HTTP status is not 200
        return response.json()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(fetch_living_expenses("California"))
