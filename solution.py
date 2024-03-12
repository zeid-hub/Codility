from datetime import datetime

def solution(A, D):
    balance = 0                # My current account balance at the beginning of the year
    monthly_fee = 5            # A monthly fee for having a card
    card_payments = 0          # Number of card payments in the current month
    card_payment_total = 0     # Total cost of card payments in the current month

    # Process each transaction
    for amount, date_str in zip(A, D):
        # Convert date string to datetime object
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Update balance based on transaction type
        if amount >= 0:
            balance += amount
        else:
            # For card payments, update card payment information
            balance += amount
            card_payments += 1
            card_payment_total += abs(amount)
            
            # This code is checking if the monthly fee will be avoided
            if card_payments >= 3 and card_payment_total >= 100:
                card_payments = 0
                card_payment_total = 0
            else:
                # Here is where the monthly fee will be applied
                balance -= monthly_fee

    # Returning the final balance after deducting the fees for the entire year
    return balance - (monthly_fee * 12)

# Example usage and expected output
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))  # Expected Output: 230
