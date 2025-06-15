Purchase Request ProcessorThis project provides a FastAPI application that processes incoming email-based purchase requests. It leverages a large language model (LLM) to extract product information, validates the extracted data against a product catalog, and identifies any discrepancies or issues.FeaturesEmail Parsing: Extracts product names, quantities, and delivery notes from free-form email text using an LLM (Anthropic's Claude).Product Catalog Integration: Validates extracted products against a pre-defined product catalog (CSV file).Order Validation: Checks for common issues such as:Product names not found in the catalog.Ordered quantity being less than the Minimum Order Quantity (MOQ).Ordered quantity exceeding available stock.Structured Output: Provides a structured JSON response indicating validated items, identified issues, and delivery notes.Project Structure.
├── app/
│ ├── ai_agent.py # Handles LLM interaction for email parsing
│ ├── catalog_loader.py # Loads and processes the product catalog
│ ├── validator.py # Validates extracted order against catalog rules
│ └── **init**.py # Initializes the app package
├── data/
│ └── Product_Catalog.csv # Example product catalog
├── main.py # Main FastAPI application
├── requirements.txt # Python dependencies
├── .env.example # Example for environment variables
└── README.md # This file
Setup and InstallationPrerequisitesPython 3.8+An Anthropic API KeyStepsClone the repository (if you haven't already):git clone <your-repository-url>
cd <your-repository-name>
Create a virtual environment and activate it:python -m venv venv

# On Windows:

.\venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate
Install dependencies:pip install -r requirements.txt
Set up environment variables:Create a file named .env in the root directory of your project (same level as main.py). Add your Anthropic API key to this file:ANTHROPIC_API_KEY="your_anthropic_api_key_here"
Note: Do not commit your .env file to version control. Add it to your .gitignore.Prepare the Product Catalog:Ensure you have your Product_Catalog.csv file in the data/ directory. An example structure would be:Product_Name,Product_Code,Price,Min_Order_Quantity,Available_in_Stock,Description
Desk TRÄNHOLM 19,DK19,250.00,1,100,Ergonomic office desk
Office Chair Deluxe,OCD99,150.00,2,50,High-back executive chair
Monitor Stand Pro,MSP01,45.00,1,200,Adjustable monitor stand
Running the ApplicationTo run the FastAPI application using Uvicorn:uvicorn main:app --reload
The --reload flag will automatically restart the server on code changes. The API will be accessible at http://127.0.0.1:8000.API EndpointPOST /parse-email/This endpoint accepts an email file, parses it, validates the contained purchase request, and returns a structured response.Method: POSTEndpoint: /parse-email/Content Type: multipart/form-dataForm Field: file (the email content as a text file)Example Request (using curl)Save your email content to a file, e.g., email.txt:Subject: Urgent Purchase Request

Hi Team,

Could you please order the following:

- 2 x Desk TRÄNHOLM 19
- 3 x Office Chair Deluxe

Delivery instructions: Please ship to Germany by July 1st.

Thanks,
John
Then send the request:curl -X POST "http://127.0.0.1:8000/parse-email/" \
 -H "accept: application/json" \
 -H "Content-Type: multipart/form-data" \
 -F "file=@email.txt;type=text/plain"
Example Response (Success){
"validated_items": [
{
"product_name": "Desk TRÄNHOLM 19",
"sku": "DK19",
"quantity": 2,
"price": 250.0,
"description": "Ergonomic office desk"
},
{
"product_name": "Office Chair Deluxe",
"sku": "OCD99",
"quantity": 3,
"price": 150.0,
"description": "High-back executive chair"
}
],
"issues": [],
"delivery_notes": "Please ship to Germany by July 1st."
}
Example Response (with Issues){
"validated_items": [
{
"product_name": "Desk TRÄNHOLM 19",
"sku": "DK19",
"quantity": 2,
"price": 250.0,
"description": "Ergonomic office desk"
}
],
"issues": [
{
"product_name": "Non-existent Chair",
"issue": "Product name not found in catalog.",
"suggestion": "Check for typos or use exact product names."
},
{
"product_name": "Monitor Stand Pro",
"issue": "Ordered quantity (1) < MOQ (2)",
"suggestion": "Increase to MOQ: 2"
}
],
"delivery_notes": ""
}
ContributingFeel free to fork the repository, open issues, and submit pull requests.License[Specify your license here, e.g., MIT, Apache 2.0, etc.]
