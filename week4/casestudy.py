# Compact Dynamic CSP for Proctor Assignment (Fixed)
exams = [
    {"name":"E1","subject":"Math","time":"10AM"},
    {"name":"E2","subject":"Physics","time":"10AM"},
    {"name":"E3","subject":"Math","time":"2PM"},
    {"name":"E4","subject":"Chemistry","time":"2PM"}
]

proctors = {
    "P1":{"skills":["Math","Chemistry"],"available":["10AM","2PM"]},
    "P2":{"skills":["Physics"],"available":["10AM"]},
    "P3":{"skills":["Math","Physics"],"available":["2PM","10AM"]}
}

def is_valid(exam, proctor, assignment):
    if exam["subject"] not in proctors[proctor]["skills"]:
        return False
    if exam["time"] not in proctors[proctor]["available"]:
        return False
    for e_name, p in assignment.items():
        if p == proctor and next(exam_["time"] for exam_ in exams if exam_["name"]==e_name)==exam["time"]:
            return False
    return True

def backtrack(assignment={}):
    if len(assignment) == len(exams):
        return assignment
    for exam in exams:
        if exam["name"] not in assignment:
            break
    for p in proctors:
        if is_valid(exam, p, assignment):
            assignment[exam["name"]] = p
            result = backtrack(assignment)
            if result:
                return result
            assignment.pop(exam["name"])
    return None

solution = backtrack()
if solution:
    for e_name, p in solution.items():
        print(f"{e_name} → {p}")
else:
    print("No valid assignment found")
