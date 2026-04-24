"""
Version 3: Object-Oriented Programming (OOP)
Encapsulates data into a Client class and logic into a CreditAnalyzer class.
Demonstrates clean separation of concerns.
"""

class Client():
    def __init__(self, name, age, income, score, clean_record, collateral):
        self.name = name
        self.age = age
        self.income = income
        self.score = score
        self.clean_record = clean_record
        self.collateral = collateral

    def credit_analyze(self):
        
        if self.age < 18:
            return 'Not approved: under 18.'
        
        if self.income < 2000:
            return 'Not approved: insufficient income.'
        
        if self.score >= 700:
            if self.clean_record:
                return 'Approved with great conditions!'
            return 'Approved with collateral.' if self.collateral else 'Not approved: bad credit history.'

        if self.score >= 500:
            if self.clean_record:
                return 'Approved with collateral.' if self.collateral else 'Not approved: bad credit history.'
            return 'Not approved: bad credit history.'
        
        return 'Not approved: low score.'
    
clients = [
    Client("Lucas Andrade", 28, 3500, 720, True, False),
    Client("Fernanda Alves", 32, 1800, 810, True, False),
    Client("Rafael Mendes", 45, 4000, 600, False, True),
    Client("Juliana Rocha", 23, 2500, 450, True, False),
    Client("Bruno Martins", 16, 900, 700, True, False),
]

for client in clients:
    print(f'{client.name}: {client.credit_analyze()}')