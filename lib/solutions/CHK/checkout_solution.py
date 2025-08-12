
class CheckoutSolution:

    # skus = unicode string
   def checkout(self, skus):
        # Type check
        if not isinstance(skus, str):
            return -1

        # Unit prices (R5)
        prices = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
            "G": 20, "H": 10, "I": 35, "J": 60, "K": 70, "L": 90,
            "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
            "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
            "Y": 20, "Z": 21,
        }

        # Validate characters
        if any(ch not in prices for ch in skus):
            return -1

        from collections import Counter
        counts = Counter(skus)
        total = 0

        # ====== FREEBIES (apply before multi-buys) ======
        # 2E -> 1B free
        free_b = counts.get("E", 0) // 2
        payable_b = max(0, counts.get("B", 0) - free_b)

        # 3N -> 1M free
        free_m = counts.get("N", 0) // 3
        payable_m = max(0, counts.get("M", 0) - free_m)

        # 3R -> 1Q free
        free_q = counts.get("R", 0) // 3
        payable_q = max(0, counts.get("Q", 0) - free_q)

        # Self-free: 2F get 1F free  => pay for 2 in each 3
        f_qty = counts.get("F", 0)
        payable_f = f_qty - (f_qty // 3)

        # Self-free: 3U get 1U free  => pay for 3 in each 4
        u_qty = counts.get("U", 0)
        payable_u = u_qty - (u_qty // 4)

        # ====== MULTI-BUYS (largest bundles first) ======
        # A: 5 for 200, then 3 for 130
        a = counts.get("A", 0)
        total += (a // 5) * 200; a %= 5
        total += (a // 3) * 130; a %= 3
        total += a * prices["A"]

        # B: 2 for 45 (on payable after E->B free)
        b = payable_b
        total += (b // 2) * 45
        total += (b % 2) * prices["B"]

        # H: 10 for 80, then 5 for 45
        h = counts.get("H", 0)
        total += (h // 10) * 80; h %= 10
        total += (h // 5) * 45;  h %= 5
        total += h * prices["H"]

        # K: 2 for 120 (R5 update)
        k = counts.get("K", 0)
        total += (k // 2) * 120
        total += (k % 2) * prices["K"]

        # P: 5 for 200
        p = counts.get("P", 0)
        total += (p // 5) * 200
        total += (p % 5) * prices["P"]

        # Q: 3 for 80 (on payable after R->Q free)
        q = payable_q
        total += (q // 3) * 80
        total += (q % 3) * prices["Q"]

        # V: 3 for 130, then 2 for 90
        v = counts.get("V", 0)
        total += (v // 3) * 130; v %= 3
        total += (v // 2) * 90;  v %= 2
        total += v * prices["V"]

        # ====== GROUP OFFER: any 3 of (S,T,X,Y,Z) for 45 ======
        group_prices_map = {"S": 20, "T": 20, "X": 17, "Y": 20, "Z": 21}
        gp_list = []
        for sku, price in group_prices_map.items():
            gp_list.extend([price] * counts.get(sku, 0))
        gp_list.sort(reverse=True)  # favor customer: discount the most expensive first

        i = 0
        while i + 2 < len(gp_list):
            total += 45  # one discounted group of 3
            i += 3
        # leftovers (less than 3) at unit prices
        total += sum(gp_list[i:])

        # ====== STRAIGHT PRICES (everything else after adjustments) ======
        total += counts.get("C", 0) * prices["C"]
        total += counts.get("D", 0) * prices["D"]
        total += counts.get("E", 0) * prices["E"]
        total += payable_f * prices["F"]
        total += counts.get("G", 0) * prices["G"]
        total += counts.get("I", 0) * prices["I"]
        total += counts.get("J", 0) * prices["J"]
        total += counts.get("L", 0) * prices["L"]
        total += payable_m * prices["M"]
        total += counts.get("N", 0) * prices["N"]
        total += counts.get("O", 0) * prices["O"]
        total += counts.get("R", 0) * prices["R"]
        # S/T/X/Y/Z are already included via group offer
        total += counts.get("W", 0) * prices["W"]
        total += payable_u * prices["U"]

        return total