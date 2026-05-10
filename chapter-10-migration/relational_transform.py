import json

# Simulated relational rows

orders = [
    {
        "order_id": "O101",
        "customer_id": "C123",
        "customer_name": "John",
        "product": "Laptop",
        "qty": 1
    },
    {
        "order_id": "O101",
        "customer_id": "C123",
        "customer_name": "John",
        "product": "Mouse",
        "qty": 2
    }
]

documents = {}

for row in orders:

    order_id = row["order_id"]

    if order_id not in documents:

        documents[order_id] = {
            "_id": order_id,
            "customer": {
                "id": row["customer_id"],
                "name": row["customer_name"]
            },
            "items": []
        }

    documents[order_id]["items"].append({
        "product": row["product"],
        "qty": row["qty"]
    })

print(json.dumps(list(documents.values()), indent=2))