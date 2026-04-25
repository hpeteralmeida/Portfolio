"""
Refactored version using @dataclass.

This module represents the final evolution of the credit analysis system,
focusing on cleaner and more maintainable code using Python's dataclasses.

Improvements:
- Reduced boilerplate code (automatic __init__)
- Cleaner and more declarative structure
- Maintains the same business logic from previous versions
"""

from dataclasses import dataclass

@dataclass
class Client():
    """
    Represents a client for credit analysis.

    Attributes:
        name (str): Client's name.
        age (int): Client's age.
        income (float): Monthly income.
        score (int): Credit score.
        clean_record (bool): Indicates if the client has a clean credit history.
        collateral (bool): Indicates if the client can provide collateral.
    """

    name: str
    age: int
    income: float
    score: int
    clean_record: bool
    collateral: bool

    def credit_analyze(self):
        """
        Performs credit analysis based on predefined business rules.

        Rules:
        - Age must be at least 18
        - Minimum income: 2000
        - Score >= 700 → best conditions
        - Score >= 500 → conditional approval
        - Clean record improves approval chances
        - Collateral may compensate for risk

        Returns:
            str: The result of the credit analysis.
        """

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
