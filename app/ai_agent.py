import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_with_claude(email_text: str) -> dict:
    prompt = f"""
You are an intelligent assistant that extracts clean, structured purchase requests from messy emails.

Extract ONLY:
1. A list of **product names** exactly as written in the email (not SKUs).
2. Their ordered **quantities**.
3. Any **delivery instructions** or notes.

IMPORTANT: Return valid JSON ONLY like this:
{{
  "product_names": ["Desk TRÄNHOLM 19", "Office Chair Deluxe"],
  "quantities": [2, 3],
  "delivery_notes": "Ship to Germany by July 1st"
}}

EMAIL:
\"\"\"
{email_text}
\"\"\"
"""


    try:
        response = anthropic_client.messages.create(
            model="claude-3-sonnet-20240229",  # Use "claude-3-opus-20240229" for higher quality
            max_tokens=512,
            temperature=0.2,
            system="You are a helpful assistant.",
            messages=[{"role": "user", "content": prompt}]
        )
        import json
        return json.loads(response.content[0].text)
    except Exception as e:
        return {"error": str(e)}
