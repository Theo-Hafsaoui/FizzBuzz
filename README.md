# FizzBuzz RESTful API with FastAPI

This project implements a **FizzBuzz** game using a RESTful API built with **FastAPI** and an SQL database. It was made as an introduction material to standart backend for a freshmen

- **Customizable FizzBuzz**: Replace divisors with custom numbers and words.
- **RESTful API**: Interaction using HTTP methods.
- **SQL Database**: Stores FizzBuzz results and stats.

## Endpoints

<details>
  <summary>API Endpoints</summary>

- **`GET /`**: Root check.
  
- **`GET /v1/fizz`**: Generate FizzBuzz.
  - Parameters: `int1`, `int2`, `str1`, `str2`, `limit`.
  
- **`GET /v1/stat`**: Fetch usage statistics.
</details>

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the API** using the `Makefile`:
   ```bash
   make run
   ```

3. Access the documentation at `http://localhost:8000/docs`.
