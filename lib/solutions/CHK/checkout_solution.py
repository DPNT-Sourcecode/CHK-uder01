
class CheckoutSolution:

    # skus = unicode string
   def checkout(self, skus):
        # Type check
        if not isinstance(skus, str):
            return -1

        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

        # Validate characters
        if any(ch not in prices for ch in skus):
            return -1

        from collections import Counter
        counts = Counter(skus)
        total = 0

        # ---------- A: best bundles first (5A then 3A) ----------
        a = counts.get("A", 0)
        total += (a // 5) * 200
        a %= 5
        total += (a // 3) * 130
        a %= 3
        total += a * prices["A"]

        # ---------- E -> B free (for each 2E, 1B free) ----------
        free_b = counts.get("E", 0) // 2
        payable_b = max(0, counts.get("B", 0) - free_b)

        # ---------- B: apply 2B for 45 on payable qty ----------
        total += (payable_b // 2) * 45
        total += (payable_b % 2) * prices["B"]

        # ---------- F: buy 2 get 1 free (need 3 in basket) ----------
        f_qty = counts.get("F", 0)
        free_f = f_qty // 3               # one free per full group of 3
        payable_f = f_qty - free_f
        total += payable_f * prices["F"]

        # ---------- C, D, E at base price ----------
        total += counts.get("C", 0) * prices["C"]
        total += counts.get("D", 0) * prices["D"]
        total += counts.get("E", 0) * prices["E"]

        return total