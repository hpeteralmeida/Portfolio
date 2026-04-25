"""
Test module for the credit analysis system.

This script runs multiple test cases to validate the behavior
of the dataclass-based implementation.
"""

from src.dataclass_logic import Client

def run_tests():
    """
    Executes predefined test scenarios for credit analysis.

    Each test case represents a different combination of inputs
    to validate business rules.
    """

    test_cases = [
        ("Approved - high score",
         Client("Test1", 30, 3000, 750, True, False)),

        ("Approved with collateral",
         Client("Test2", 30, 3000, 750, False, True)),

        ("Rejected - bad credit history",
         Client("Test3", 30, 3000, 750, False, False)),

        ("Approved (medium score + collateral)",
         Client("Test4", 30, 3000, 600, True, True)),

        ("Rejected - low score",
         Client("Test5", 30, 3000, 400, True, False)),

        ("Rejected - low income",
         Client("Test6", 30, 1500, 800, True, False)),

        ("Rejected - underage",
         Client("Test7", 16, 3000, 800, True, False)),
    ]

    print("=" * 50)
    print("CREDIT ANALYSIS TEST RESULTS")
    print("=" * 50)

    for description, client in test_cases:
        result = client.credit_analyze()
        print(f"{description}")
        print(f"Client: {client.name}")
        print(f"Result: {result}")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()