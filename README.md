# Python Project Fast api

## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer) should also be available.

## Setting Up the Virtual Environment

Follow these steps to set up and use a virtual environment:

### 1. Create/Start the Virtual Environment

1. Open a terminal in your project directory and create a virtual env (if not created already):
   ```cmd
   python -m venv venv
2. Then activate venv:
   ```cmd
   .\venv\Scripts\activate
3. Install dependencies (if not installed already):
   ```cmd
   pip install -r requirements.txt
5. Deactivate vevn before closing:
   ```cmd
   deactivate
### 2. Run jupyter
1. Start jupyter server:
   ```cmd
   jupyter notebook
### 3. Run Fast api project
1. navigate to Fast-api folder:
   ```cmd
   cd .\fast-api
2. Start Fast-api server:
   ```cmd
   uvicorn main:app --host 127.0.0.1 --port 8080 --reload
3. Swagger:
   [url](http://localhost:8080/docs)

