
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # Price table and offers
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }
        offers = {
            "A": (3, 130),  # 3A for 130
            "B": (2, 45)    # 2B for 45
        }
        
        # Validate input
        if not isinstance(skus, str) or any(ch not in prices for ch in skus):
            return -1
        
        # Count items
        from collections import Counter
        counts = Counter(skus)
        
        total = 0
        for item, count in counts.items():
            if item in offers:
                offer_qty, offer_price = offers[item]
                total += (count // offer_qty) * offer_price
                total += (count % offer_qty) * prices[item]
            else:
                total += count * prices[item]
        
        return total

