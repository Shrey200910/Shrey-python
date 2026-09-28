# Summation Notation: expanding and evaluating Σ

Beginner | notation | foundations

### The problem, from first principles

Every other track on this site writes formulas using `Σ` (sigma) without ever teaching what it means — a loss function's `Σ_i (y_i - ŷ_i)²`, entropy's `-Σ_x p(x) log p(x)`, a dot product's `Σ_i a_i b_i`. All of them are the exact same idea: "add up a sequence of values, one per index, over a specified range." This question makes that idea concrete before it shows up disguised inside a bigger formula.

### From theory to code

`Σ` is nothing more than a `for` loop that accumulates a running total. Implement `summation(f, lo, hi)`, computing `Σ_{i=lo}^{hi} f(i)` — call `f` once per integer `i` from `lo` to `hi` **inclusive**, and add up the results. The signature and docstring are already in the editor.

### Constraints

- `lo` and `hi` are integers; `hi` may be less than `lo`, in which case the sum is empty (the standard mathematical convention: an empty sum is `0`).
- `f` takes a single integer and returns a number (int or float).
- Do not use `sum()` with a generator that secretly hides the loop from yourself — write the accumulation explicitly, since the point is to see the mechanics `Σ` is standing in for.

### Hints

<details>
<summary>Hint 1</summary>

`range(lo, hi + 1)` — `hi` is inclusive in summation notation, unlike Python's own `range`, which stops one short.

</details>

<details>
<summary>Hint 2</summary>

Handle the empty case (`hi < lo`) by starting `total = 0` and simply never entering the loop, rather than special-casing it separately — `range(lo, hi + 1)` is already empty in that case, so no extra branch is needed.

</details>
