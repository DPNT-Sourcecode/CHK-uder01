
class CheckoutSolution:

    # skus = unicode string
   def checkout(self, skus):
        # Validate type
        if not isinstance(skus, str):
            return -1

        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

        # Validate characters
        if any(ch not in prices for ch in skus):
            return -1

        from collections import Counter
        counts = Counter(skus)

        total = 0

        # ---- A: use best bundles first (5A then 3A) ----
        a = counts.get("A", 0)
        total += (a // 5) * 200
        a %= 5
        total += (a // 3) * 130
        a %= 3
        total += a * prices["A"]

        # ---- E -> B free: for each 2E, 1B is free ----
        free_b = counts.get("E", 0) // 2
        payable_b = max(0, counts.get("B", 0) - free_b)

        # ---- B: apply 2B for 45 on the payable quantity ----
        total += (payable_b // 2) * 45
        total += (payable_b % 2) * prices["B"]

        # ---- C, D, E straight prices ----
        total += counts.get("C", 0) * prices["C"]
        total += counts.get("D", 0) * prices["D"]
        total += counts.get("E", 0) * prices["E"]

        return total
