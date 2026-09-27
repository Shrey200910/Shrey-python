def compute_total(price: float, quantity: int) -> float:
    # 2. Create a variable subtotal equal to price * quantity.
    subtotal = price * quantity
    
    # 3. Create a variable tax equal to 8% of subtotal (0.08).
    tax = subtotal * 0.08
    
    # 4. Reassign subtotal by adding tax to it, using the += shorthand.
    subtotal += tax
    
    # Return the final value of subtotal
    return subtotal


def swap_two_variables(a, b):
    # 1. Store a's value in a new variable
    temp = a
    
    # 2. Set a equal to b
    a = b
    
    # 3. Set b equal to temp
    b = temp
    
    # Return the two swapped values separated by a comma
    return a, b
