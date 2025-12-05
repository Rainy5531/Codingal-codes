a = int(input("Enter 1 or 0 for value of a: "))
b = int(input("Enter 1 or 0 for value of b: "))
c = int(input("Enter 1 or 0 for value of c: "))

a_and_b = a & b
b_or_c = b | c
b_and_c = b & c
b_or_c_AND_b_and_c = b_or_c & b_and_c
q = a_and_b | b_or_c_AND_b_and_c

print(r"""
          ┌───────┐
   A ────►│ AND   │──────┐
          │(A·B)  │      │
   B ──┬─►└───────┘      │
       │                 │
       │   ┌───────┐     │
       ├──►│ OR    │     │
       │   │(B+C)  │     │
       │   └───────┘     │
       │        │        │
       │        │        │
       │   ┌────┴────┐   │
       │   │ AND     │   │
   C ──┴──►│(B·C)    │   │
           └────┬────┘   │
                │        │
                └────┐   │
                     │   │
                 ┌───▼───▼───┐
                 │ OR        │
                 │ (X₁+X₄)=Q │
                 └───────────┘
""")

print(f"The output Q in the circuit is: {q}")