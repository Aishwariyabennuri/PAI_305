
import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination


# Step 1: Create dataset
data = pd.DataFrame({
    'IncomeStability': ['Stable', 'Stable', 'Unstable', 'Stable', 'Unstable', 'Stable', 'Unstable', 'Unstable'],
    'CreditHistory': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Bad', 'Good', 'Bad'],
    'EmploymentType': ['Salaried', 'Self', 'Self', 'Salaried', 'Self', 'Salaried', 'Self', 'Salaried'],
    'DefaultRisk': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes']
})


# Step 2: Define Bayesian Network
model = DiscreteBayesianNetwork([
    ('IncomeStability', 'DefaultRisk'),
    ('CreditHistory', 'DefaultRisk'),
    ('EmploymentType', 'DefaultRisk')
])


# Step 3: Train model
model.fit(data)


# Step 4: Print CPDs
print("\nConditional Probability Tables:\n")
for cpd in model.get_cpds():
    print(cpd)


# Step 5: Perform inference
inference = VariableElimination(model)

result = inference.query(
    variables=['DefaultRisk'],
    evidence={
        'IncomeStability': 'Unstable',
        'CreditHistory': 'Bad',
        'EmploymentType': 'Self'
    }
)

print("\nProbability of Default Risk:\n")
print(result)
