from economics import Economics
from marginal_utility_product import MarginalUtilityProduct

def test_1():
    chicken_fajitas = MarginalUtilityProduct(
        'Chicken Fajitas',
        [0, 1.57, 1.5, 1.43, 1.0, 1.15, 0.57, -0.36],
        14)

    cheese_quesadillas = MarginalUtilityProduct(
        'Cheese Quesadillas',
        [0, 1.6, 1.5, 1.4, 1.2, 1.1, 0.5 ],
        10
    )

    print("""Expected:
          Total spent: 48,
          Chicken Fajitas: 2
          Cheese Quesadillas: 2
    """)
    print("Actual:")
    print(Economics.optimal_quantity(56.00, chicken_fajitas, cheese_quesadillas))

test_1()
print("----\n")

def test_2():
    chicken_fajitas = MarginalUtilityProduct(
        'Chicken Fajitas',
        [0, 2.5, 1.8, 1.6, 1.4, 1.1, 0.9, -0.5],
        10)

    cheese_quesadillas = MarginalUtilityProduct(
        'Cheese Quesadillas',
        [0, 3, 2, 1.6, 1.2, 1, -.8, 0.6],
        5
    )

    print("""Expected:
          Total spent: 45,
          Chicken Fajitas: 3
          Cheese Quesadillas: 3
    """)
    print("Actual:")
    print(Economics.optimal_quantity(48.00, chicken_fajitas, cheese_quesadillas))

test_2()
print("----\n")

def test_3():
    chicken_fajitas = MarginalUtilityProduct(
        'Chicken Fajitas',
        [0, 2.5, 1.8, 1.6, 1.4, 1.1, 0.9, -0.5],
        10)

    cheese_quesadillas = MarginalUtilityProduct(
        'Cheese Quesadillas',
        [0, 3, 2, 1.6, 1.2, 1, 0.8, 0.6],
        5
    )

    print("Expecting total spent to be less than $56")
    print(Economics.optimal_quantity(56.00, chicken_fajitas, cheese_quesadillas))

test_3()