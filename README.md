# 🇹🇿 Tanzania Pincode Lookup API

A lightweight **FastAPI** service for looking up Tanzanian regions, cities, and districts from a 6-digit pincode.

The API is designed for applications such as **e-commerce checkout forms**, where a customer enters a pincode and the corresponding location information can be automatically populated.

## ✨ Features

- 🔎 Look up a location using a 6-digit pincode
- 📦 Perform bulk pincode lookups
- 🇹🇿 Tanzania-focused location data
- ✅ Automatic pincode validation using Pydantic
- ⚡ Fast API powered by FastAPI
- 🛡️ Custom error handling for invalid and unknown pincodes
- 📚 Interactive API documentation through FastAPI
- 🧩 Easy to integrate with checkout and address forms

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

## 📁 Project Structure

```text
emtaa/
│
├── main.py             # FastAPI application and API routes
├── models.py           # Pydantic request/response models
├── data.py             # Pincode and location data
├── exceptions.py       # Custom exceptions and handlers
├── requirements.txt    # Python dependencies
├── Scripts/            # Virtual environment scripts
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ibrahist/emtaa.git
cd emtaa
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv emtaa
```

Activate it:

```bash
emtaa\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv emtaa
source emtaa/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

Run:

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

Once the server is running, FastAPI automatically provides interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🔌 API Endpoints

### `GET /`

Returns a welcome message.

#### Example

```http
GET /
```

#### Response

```json
{
  "message": "Welcome to the Pincode lookup API!"
}
```

---

### `GET /pincode/{code}`

Look up a location using a 6-digit pincode.

#### Example

```http
GET /pincode/123456
```

#### Response

```json
{
  "pincode": "123456",
  "region": "Dar es Salaam",
  "city": "Dar es Salaam",
  "district": "Ilala"
}
```

### Validation

Pincodes must:

- Contain exactly **6 digits**
- Exist in the available pincode dataset

Invalid or unknown pincodes return an appropriate error response.

---

### `POST /pincodes`

Look up multiple pincodes in a single request.

#### Request

```json
{
  "pincodes": ["123456", "654321", "111111"]
}
```

#### Response

```json
{
  "status": "success",
  "found": 3,
  "not_found": 0,
  "results": [
    {
      "pincode": "123456",
      "region": "Dar es Salaam",
      "city": "Dar es Salaam",
      "district": "Ilala"
    }
  ],
  "missing": []
}
```

The bulk endpoint accepts up to **10 pincodes per request**.

## 🗺️ Current Sample Data

The project currently includes sample pincode mappings for locations including:

| Pincode  | Region        | City          | District |
| -------- | ------------- | ------------- | -------- |
| `123456` | Dar es Salaam | Dar es Salaam | Ilala    |
| `654321` | Mwanza        | Mwanza        | Mwanza   |
| `111111` | Arusha        | Arusha        | Arusha   |
| `222222` | Dodoma        | Dodoma        | Dodoma   |
| `333333` | Mbeya         | Mbeya         | Mbeya    |
| `444444` | Kilimanjaro   | Moshi         | Moshi    |
| `555555` | Tanga         | Tanga         | Tanga    |
| `666666` | Zanzibar      | Zanzibar City | Zanzibar |

> **Note:** These are currently sample/test records. For production use, the dataset should be replaced or expanded with verified Tanzanian postal-code data.

## 🛒 Example Checkout Use Case

The API can be integrated into an e-commerce checkout flow.

For example:

```text
Customer enters pincode
        ↓
Frontend sends pincode to API
        ↓
GET /pincode/{code}
        ↓
API returns region, city & district
        ↓
Checkout form automatically fills location
```

This can reduce manual address entry and improve the checkout experience.

## 🧪 Testing with cURL

### Single lookup

```bash
curl http://127.0.0.1:8000/pincode/123456
```

### Bulk lookup

```bash
curl -X POST http://127.0.0.1:8000/pincodes \
  -H "Content-Type: application/json" \
  -d "{\"pincodes\":[\"123456\",\"654321\",\"111111\"]}"
```

## 🔐 Production Considerations

Before using the API in production, consider:

- Replacing sample pincode data with verified postal data
- Adding API authentication if required
- Adding rate limiting
- Adding logging and monitoring
- Deploying behind HTTPS
- Adding automated tests
- Moving location data from an in-memory dictionary to a database for larger datasets
- Adding CORS configuration for frontend applications
- Adding proper deployment configuration

## 🔮 Future Improvements

Potential improvements include:

- [ ] Add complete Tanzanian postal-code dataset
- [ ] Add database support
- [ ] Add automated tests
- [ ] Add CORS configuration
- [ ] Add API authentication
- [ ] Add rate limiting
- [ ] Add Docker support
- [ ] Add deployment configuration
- [ ] Add API versioning
- [ ] Add search by region, city, or district
- [ ] Add frontend checkout demo

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Commit your changes

```bash
git add .
git commit -m "Add my feature"
```

5. Push your branch

```bash
git push origin feature/my-feature
```

6. Open a Pull Request

## 📄 License

This project is currently available without a specified license.

If you intend to distribute or accept external contributions, consider adding an appropriate open-source license.

## 👨‍💻 Author

**Ibrahist**

GitHub: https://github.com/Ibrahist

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

#❌❌The data provided are auto-generated for testing purposes only. I accept no responsibility for the authenticity or accuracy of the provided data.

Built with ❤️ using **Python + FastAPI**.
