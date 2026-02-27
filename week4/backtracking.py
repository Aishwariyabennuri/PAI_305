class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        var = next(v for v in self.variables if v not in assignment)

        for value in self.domains[var]:
            if all(constraint(var, value, assignment)
                   for constraint in self.constraints.get(var, [])):

                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(var)

        return None


# Example with COLORS
variables = ['A', 'B', 'C']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}

# Constraint: All must have different colors
constraints = {
    'A': [lambda v, val, a: 'B' not in a or a['B'] != val],
    'B': [lambda v, val, a: 'A' not in a or a['A'] != val],
    'C': [
        lambda v, val, a: 'A' not in a or a['A'] != val,
        lambda v, val, a: 'B' not in a or a['B'] != val
    ]
}

csp = CSP(variables, domains, constraints)
solution = csp.backtrack({})
print(solution)
