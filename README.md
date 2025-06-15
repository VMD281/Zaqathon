# 📦 Purchase Request Processor (Zaqathon)

This project is a FastAPI-based backend powered by Claude AI (Anthropic) that intelligently extracts and validates purchase requests from email content.

---

## 🚀 Features

- ✉️ **Email Parsing**  
  Extracts product names, quantities, and delivery notes from free-form email text using an LLM (Claude 3).

- 📚 **Product Catalog Integration**  
  Validates extracted products against a structured product catalog (`CSV`).

- ✅ **Order Validation Checks**

  - Product names not found in the catalog
  - Ordered quantity below Minimum Order Quantity (MOQ)
  - Ordered quantity exceeds available stock

- 📤 **Structured Output**  
  Returns a structured JSON response with:
  - Validated items
  - Validation issues
  - Delivery notes

---

## ⚙️ Setup & Installation

### 🧾 Prerequisites

- Python 3.8+
- [Anthropic API Key](https://docs.anthropic.com/claude/docs/quickstart-guide)

### 🛠 Steps

1. **Clone the repository**:
   ```bash
    git clone https://github.com/YOUR_USERNAME/zaqathon.git
    cd zaqathon
   ```
2. **Create a virtual environment**:
   python -m venv venv
   source venv/bin/activate # Windows: venv\Scripts\activate
3. **Install dependencies**:
   pip install -r requirements.txt
   Copy .env.example → .env
4. **Set up environment variables:**:
   Copy .env.example → .env
   ANTHROPIC_API_KEY="your_key_here"
5. **Running the app:**:
   uvicorn main:app --reload
