# FacebookTokenExchange

A modular FastAPI service that converts a valid Facebook user access token into an app-scoped token for a specified Facebook App ID using the `auth.getSessionforApp` endpoint. Designed with clean architecture principles, strict App ID validation, and production-ready structure.

## ✨ Features

- Modular FastAPI architecture with clear separation of concerns  
- Facebook access token exchange via `auth.getSessionforApp` endpoint  
- Strict Enum-based App ID validation to prevent invalid targets  
- Automatic OpenAPI documentation with built-in Swagger UI

## 📦 Project Structure

```
FacebookTokenExchange/
├── app/
│   ├── api/v1/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── run.py
├── requirements.txt
└── README.md
```

## 🚀 Installation

1. Install dependencies
   
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server
   
   ```bash
   python run.py
   ```

3. Access the application
   
   ```
   http://localhost:8000
   ```

## 🔌 Exchange Token

| Method | Endpoint      | Description                             |
| ------ | ------------- | --------------------------------------- |
| POST   | /api/v1/token | Exchange user access token to app token |

### Request Body

| Field | Type   | Required | Description                      |
| ----- | ------ | -------- | -------------------------------- |
| appid | string | Yes      | Target Facebook App (Enum)       |
| token | string | Yes      | Valid Facebook user access token |

Example:

```json
{
  "appid": "FACEBOOK_ANDROID",
  "token": "EAABu2IFZC..."
}
```

## ⚙️ Environment Variables (Optional)

```
HOST=0.0.0.0
PORT=8000
```

## 🔒 Notes

* Do not expose this service publicly without proper authentication and rate limiting.
* Only valid Facebook access tokens can be exchanged.
* Old token permissions are revoked after successful exchange.

## 📄 License

MIT