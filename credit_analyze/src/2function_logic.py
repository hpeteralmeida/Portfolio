"""
Version 2: Functional Approach
Refactored to use 'Guard Clauses' for better readability.
Each validation is isolated, making the main logic linear and easier to follow.
"""

def check_age(age):
     # Early return avoids wrapping the entire logic in a conditional block
    if age < 18:
        return 'Not approved: Under 18.'
    return None

def check_income(income):
     # Isolating this rule makes it easier to modify later
    if income < 2000:
        return 'Not approved: Insufficient income.'
    return None

def check_score(score, clean_record, collateral):
    # This logic was previously deeply nested inside the main function
    # Now it is isolated, making it easier to understand and maintain
    if score >= 700:
        if clean_record:
            return 'Approved with great conditions!'
        return 'Approved with collateral.' if collateral else 'Not approved: bad credit history.'
    if score >= 500:
        if clean_record:
            return 'Approved with collateral.' if collateral else 'Not approved: bad credit history.'
        return 'Not approved: bad credit history.'

    return 'Not approved: Low score.'

def credit_analyze(name, age, income, score, clean_record, collateral):
    # Step-by-step validation (fail fast approach)
    check_validations = [
        check_age(age),
        check_income(income)
    ]

    for result in check_validations:
        if result:
            return f'{name}: {result}'
    
    # Main decision logic separated from validations 
    return f'{name} - {check_score(score, clean_record, collateral)}'

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

for client in clients:
    # The * operator unpacks the client tuple into the function arguments
    print(credit_analyze(*client))
