from client import EGraphCongruenceClosure

def main():
    print("=== Testing E-Graph Congruence Closure ===")
    eg = EGraphCongruenceClosure()

    # Assert a == b
    eg.union("a", "b")
    # Propagate congruence: a == b => g(a) == g(b)
    eg.merge_congruence("g(a)", "g(b)", "a", "b")

    print(f"Equivalence class of g(a): {eg.find('g(a)')}")
    print(f"Equivalence class of g(b): {eg.find('g(b)')}")
    assert eg.find("g(a)") == eg.find("g(b)")
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
