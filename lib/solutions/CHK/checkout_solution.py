
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # ---- validate type ----
        if not isinstance(skus, str):
            return -1

        # ---- unit prices ----
        prices = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
            "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90,
            "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
            "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
            "Y": 10, "Z": 50,
        }

        # ---- validate characters ----
        if any(ch not in prices for ch in skus):
            return -1

        from collections import Counter
        counts = Counter(skus)
        total = 0

        # ========= FREEBIES (apply BEFORE multi-buys) =========
        # 2E -> get 1B free
        free_b = counts.get("E", 0) // 2
        payable_b = max(0, counts.get("B", 0) - free_b)

        # 3N -> get 1M free
        free_m = counts.get("N", 0) // 3
        payable_m = max(0, counts.get("M", 0) - free_m)

        # 3R -> get 1Q free
        free_q = counts.get("R", 0) // 3
        payable_q = max(0, counts.get("Q", 0) - free_q)

        # Self-freebies:
        # 2F get 1F free -> groups of 3, pay for 2
        f_qty = counts.get("F", 0)
        free_f = f_qty // 3
        payable_f = f_qty - free_f

        # 3U get 1U free -> groups of 4, pay for 3
        u_qty = counts.get("U", 0)
        free_u = u_qty // 4
        payable_u = u_qty - free_u

        # ========= MULTI-BUYS (largest bundles first) =========
        # A: 5 for 200, 3 for 130
        a = counts.get("A", 0)
        total += (a // 5) * 200
        a %= 5
        total += (a // 3) * 130
        a %= 3
        total += a * prices["A"]

        # B: 2 for 45 on PAYABLE quantity (after E->B freebies)
        b = payable_b
        total += (b // 2) * 45
        total += (b % 2) * prices["B"]

        # H: 10 for 80, 5 for 45
        h = counts.get("H", 0)
        total += (h // 10) * 80
        h %= 10
        total += (h // 5) * 45
        h %= 5
        total += h * prices["H"]

        # K: 2 for 150
        k = counts.get("K", 0)
        total += (k // 2) * 150
        total += (k % 2) * prices["K"]

        # P: 5 for 200
        p = counts.get("P", 0)
        total += (p // 5) * 200
        total += (p % 5) * prices["P"]

        # Q: 3 for 80 on PAYABLE quantity (after R->Q freebies)
        q = payable_q
        total += (q // 3) * 80
        total += (q % 3) * prices["Q"]

        # V: 3 for 130, then 2 for 90
        v = counts.get("V", 0)
        total += (v // 3) * 130
        v %= 3
        total += (v // 2) * 90
        v %= 2
        total += v * prices["V"]

        # ========= STRAIGHT PRICES (after adjustments) =========
        total += counts.get("C", 0) * prices["C"]
        total += counts.get("D", 0) * prices["D"]
        total += counts.get("E", 0) * prices["E"]
        total += payable_f * prices["F"]
        total += counts.get("G", 0) * prices["G"]
        total += counts.get("I", 0) * prices["I"]
        total += counts.get("J", 0) * prices["J"]
        total += payable_m * prices["M"]
        total += counts.get("N", 0) * prices["N"]
        total += counts.get("O", 0) * prices["O"]
        total += counts.get("R", 0) * prices["R"]
        total += counts.get("S", 0) * prices["S"]
        total += counts.get("T", 0) * prices["T"]
        total += payable_u * prices["U"]
        total += counts.get("W", 0) * prices["W"]
        total += counts.get("X", 0) * prices["X"]
        total += counts.get("Y", 0) * prices["Y"]
        total += counts.get("Z", 0) * prices["Z"]

        return total