customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]
eligible_customers = filter(lambda c : c['age'] in range (18,41),customers)

discount_customers = lambda cus : {**cus,
                                   "total_purchase" : cus['total_purchase'] - (cus['total_purchase'] * 0.1) if cus['age'] in range (18,26)
                                   else cus['total_purchase'] - (cus['total_purchase'] * 0.05) if cus['age'] in range (26,41)
                                   else cus['total_purchase']}
updated_customers = list(map(discount_customers,eligible_customers))
print(updated_customers)