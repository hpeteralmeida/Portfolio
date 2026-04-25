"""
Initial version of the credit analysis system.

This implementation uses deeply nested conditional statements,
which makes the code harder to read, maintain, and scale.

Purpose:
- Demonstrate poor readability due to excessive nesting
- Serve as a baseline for future refactoring
"""

def credit_analyze(name, age, income, score, clean_record, collateral):
    if age >= 18:
        if income >= 2000:
            if score >= 700:
                if clean_record:
                    return 'Approved with great conditions!'
                return 'Approved with collateral.' if collateral else 'Not approved: Bad credit history.'
            if score >= 500:
                if clean_record:
                    return 'Approved with collateral.' if collateral else 'Not approved: Bad credit history.'
                return 'Not approved: Bad credit history.'
            return 'Not approved: Insufficient score.'
        return 'Not approved: Insufficient income.'
    return 'Not approved: Under 18.'

# A clients list to test the function:
clients = [
    ("Luke", 19, 2000, 800, True, True),
    ("Leia", 20, 2000, 800,  False, True),
    ("Obi", 25, 2000, 600, True, True),
    ("Anakin", 23, 2000, 600, True, False),
    ("Padme", 28, 2000, 630, False, False),
    ("Mandalorian", 30, 1300, 500, False, False),
    ("Grogu", 5, 0, 0, True, False)
]

for name, age, income, score, clean_record, collateral in clients:
    result = credit_analyze(name, age, income, score, clean_record, collateral)
    print(f'{name}: {result}')
