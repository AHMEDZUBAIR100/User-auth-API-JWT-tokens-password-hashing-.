# FastAPI Authentication & Authorization API

A clean, production-ready RESTful API implementation demonstrating user authentication and token-based authorization using **FastAPI**, **JWT (JSON Web Tokens)**, and modern password hashing with **`pwdlib`**.

---

## 🚀 Features

- **User Registration**: Secure registration with automated validation for existing usernames and emails.
- **Password Hashing**: Secure password management using modern `pwdlib` hashing algorithms.
- **JWT Authentication**: OAuth2-compatible bearer token generation using `PyJWT`.
- **Protected Endpoints**: Endpoint protection and current-user retrieval via FastAPI dependencies.
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc endpoints.

---

## 🛠️ Project Structure

```text
fastapi-auth-api/
│
├── routers/
│   ├── login.py       # Authentication & token generation route
│   ├── me.py          # Protected current-user profile route
│   └── register.py    # User registration route
│
├── database.py        # In-memory database / user collection
├── main.py            # Main application setup and router inclusion
├── schemas.py         # Pydantic data schemas & request validation
├── security.py        # Hashing, token operations, and dependencies
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **Security & Tokens**: [PyJWT](https://pyjwt.readthedocs.io/), [pwdlib](https://github.com/hynek/pwdlib)
- **Validation**: [Pydantic](https://docs.pydantic.dev/)

---

## 🚦 Getting Started

### Prerequisites

Ensure you have **Python 3.9+** installed on your system.

### 1. Installation

Clone the repository and set up a virtual environment:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/fastapi-auth-api.git
cd fastapi-auth-api

# Create and activate virtual environment
# On Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

# On Windows:
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the local development server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## 📖 API Endpoints & Usage

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/` | Root endpoint / Health check | ❌ |
| `POST` | `/register` | Register a new user | ❌ |
| `POST` | `/login` | Authenticate user & issue JWT token | ❌ |
| `GET` | `/me` | Fetch active user's profile | ✅ |

### Interactive API Docs

FastAPI generates interactive documentation automatically. Once the server is running, you can access:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔒 Example Workflow

1. **Register a User**: Send a `POST` request to `/register` with a payload:
   ```json
   {
     "username": "johndoe",
     "email": "john@example.com",
     "password": "securepassword123"
   }
   ```
2. **Obtain Access Token**: Send a `POST` request to `/login` using `form-data`:
   - `username`: `johndoe`
   - `password`: `securepassword123`
   
   Response:
   ```json
   {
     "access_token": "<YOUR_JWT_TOKEN>",
     "token_type": "bearer"
   }
   ```
3. **Access Protected Route**: Pass the token as a Bearer authorization header to `/me`:
   ```http
   Authorization: Bearer <YOUR_JWT_TOKEN>
   ```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.