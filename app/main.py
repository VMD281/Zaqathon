from fastapi import FastAPI, UploadFile, File
from app.catalog_loader import load_catalog
from app.validator import validate_order
from app.ai_agent import extract_with_claude

# ✅ Load the catalog — this defines both product_name_set and product_info
product_name_set, product_info = load_catalog("data/Product_Catalog.csv")

app = FastAPI()

@app.post("/parse-email/")
async def parse_email(file: UploadFile = File(...)):
    content = await file.read()
    email_text = content.decode("utf-8")
    print(f"Received email text:\n{email_text}")

    parsed = extract_with_claude(email_text)
    print(f"Parsed Claude response: {parsed}")

    if "error" in parsed:
        return parsed

    validated = validate_order(parsed, product_name_set, product_info)
    print(f"Validation result: {validated}")
    return validated
