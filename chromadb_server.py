from fastapi import FastAPI

app = FastAPI()



@app.get("/get_living_expenses/{state}")
def get_living_expenses(state: str):
    return {"state": state, "expense": "Sample data"}

@app.get("/get_job_market/{field}")
def get_job_market(field: str):
    mock_data = {
        "Computer Science": [{"role": "Software Engineer", "growth": "10%"}],
        "Engineering": [{"role": "Mechanical Engineer", "growth": "5%"}],
    }
    return mock_data.get(field, {"error": "Field not found"})
