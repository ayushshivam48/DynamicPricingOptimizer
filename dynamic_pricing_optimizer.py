import random

def predict_demand(base_demand, price, elasticity):
    # Higher price -> lower demand
    demand = base_demand * (1 - elasticity * (price / 100))
    noise = random.uniform(-0.05, 0.05) * base_demand
    return max(round(demand + noise), 0)

def optimize_price(product, base_demand, current_price, elasticity, stock, competitor_price):
    price_range = [round(current_price * f, 2) for f in [0.8, 0.9, 1, 1.1, 1.2]]
    best_price = current_price
    max_revenue = 0

    for price in price_range:
        predicted_demand = min(predict_demand(base_demand, price, elasticity), stock)
        revenue = predicted_demand * price
        # Consider competitor adjustment: penalize if price is much higher than competitor
        if price > competitor_price * 1.2:
            revenue *= 0.9
        if revenue > max_revenue:
            max_revenue = revenue
            best_price = price
    return best_price, max_revenue

def main():
    print("💰 Dynamic Pricing Optimizer for Retail & E-commerce 💰")
    n = int(input("Enter number of products: "))
    products = {}

    for _ in range(n):
        name = input("\nProduct Name: ")
        base_demand = int(input("Average daily demand: "))
        stock = int(input("Current stock: "))
        current_price = float(input("Current price (₹): "))
        elasticity = float(input("Price elasticity (0-1): "))
        competitor_price = float(input("Competitor price (₹): "))
        products[name] = {
            "base_demand": base_demand,
            "stock": stock,
            "current_price": current_price,
            "elasticity": elasticity,
            "competitor_price": competitor_price
        }

    print("\n📊 Recommended Dynamic Prices")
    print("-"*50)
    for name, data in products.items():
        best_price, expected_revenue = optimize_price(
            name,
            data["base_demand"],
            data["current_price"],
            data["elasticity"],
            data["stock"],
            data["competitor_price"]
        )
        print(f"\nProduct: {name}")
        print(f"Current Price: ₹{data['current_price']:.2f}")
        print(f"Recommended Price: ₹{best_price:.2f}")
        print(f"Expected Revenue at Recommended Price: ₹{expected_revenue:.2f}")
        if best_price < data["current_price"]:
            print("💡 Suggestion: Apply discount to boost sales.")
        elif best_price > data["current_price"]:
            print("💡 Suggestion: Increase price to maximize revenue.")
        else:
            print("✅ Price is optimal.")

if __name__ == "__main__":
    main()
