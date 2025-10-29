# Backward Chaining in Python

# Knowledge Base (Horn Clauses)
knowledge_base = [
    (["mammal(A)"], "vertebrate(A)"),
    (["vertebrate(A)"], "animal(A)"),
    (["vertebrate(A)", "flying(A)"], "bird(A)"),
    ([], "vertebrate('duck')"),
    ([], "flying('duck')"),
    ([], "mammal('cat')")
]

def substitute(clause, var, val):
    """Replace variable with value in a clause."""
    return clause.replace(var, val)

def backward_chain(goal, known_facts=None):
    """Try to prove the goal using backward chaining."""
    if known_facts is None:
        known_facts = set()

    # If already proven
    if goal in known_facts:
        return True

    # Check for known facts (base case)
    for premises, conclusion in knowledge_base:
        if not premises and conclusion == goal:
            known_facts.add(goal)
            return True

    # Try using rules to derive the goal
    for premises, conclusion in knowledge_base:
        if "(" in conclusion and ")" in conclusion:
            fun_concl, arg_concl = conclusion.split("(", 1)
            fun_goal, arg_goal = goal.split("(", 1)

            # Remove the closing bracket
            arg_concl = arg_concl[:-1]
            arg_goal = arg_goal[:-1]

            # Check if predicate matches
            if fun_concl.strip() == fun_goal.strip():
                # unify variables (like A) with actual constant
                if arg_concl.isupper():  # variable
                    sub_premises = [substitute(p, arg_concl, arg_goal) for p in premises]
                else:
                    sub_premises = premises

                # recursively prove all premises
                if all(backward_chain(p, known_facts) for p in sub_premises):
                    known_facts.add(goal)
                    return True

    return False


# ---------------------------
# MAIN PROGRAM
# ---------------------------
if __name__ == "__main__":
    print("Knowledge Base Loaded.")
    goal = input("Enter the goal (e.g., bird('duck')): ").strip()
    if not goal.endswith(")"):
        print("❌ Invalid goal format. Example: bird('duck')")
    else:
        result = backward_chain(goal)
        if result:
            print(f"✅ Goal {goal} can be derived from the knowledge base.")
        else:
            print(f"❌ Goal {goal} cannot be derived from the knowledge base.")
