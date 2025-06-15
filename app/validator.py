def validate_order(order: dict, product_name_set: set, product_info: dict) -> dict:
    validated = []
    issues = []

    names = order.get("product_names", [])
    quantities = order.get("quantities", [])

    for name, qty in zip(names, quantities):
        key = name.lower().strip()

        if key not in product_name_set:
            issues.append({
                "product_name": name,
                "issue": "Product name not found in catalog.",
                "suggestion": "Check for typos or use exact product names."
            })
            continue

        product = product_info[key]

        if qty < product["moq"]:
            issues.append({
                "product_name": name,
                "issue": f"Ordered quantity ({qty}) < MOQ ({product['moq']})",
                "suggestion": f"Increase to MOQ: {product['moq']}"
            })
            continue

        if qty > product["stock"]:
            issues.append({
                "product_name": name,
                "issue": f"Ordered quantity ({qty}) > stock available ({product['stock']})",
                "suggestion": "Reduce quantity or wait for restock"
            })
            continue

        validated.append({
            "product_name": name,
            "sku": product["sku"],
            "quantity": qty,
            "price": product["price"],
            "description": product["description"]
        })

    if not names:
        return {
            "validated_items": [],
            "issues": [{"issue": "No product names found in Claude response."}],
            "delivery_notes": order.get("delivery_notes", "")
        }
    
    return {
        "validated_items": validated,
        "issues": issues,
        "delivery_notes": order.get("delivery_notes", "")
    }
