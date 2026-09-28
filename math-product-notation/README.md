# Product Notation: expanding and evaluating ∏

Beginner | notation | foundations

### The problem, from first principles

`01-summation-notation`'s `Σ` accumulates by adding. `∏` (capital pi) is the exact same accumulation pattern, just multiplying instead — and it shows up wherever probabilities of independent events combine (the likelihood of a whole dataset is a product of per-example probabilities) or wherever a count is built up multiplicatively (a factorial, covered next, is itself a `∏`).

### From theory to code

Implement `product(f, lo, hi)`, computing `∏_{i=lo}^{hi} f(i)` — call `f` once per integer `i` from `lo` to `hi` **inclusive**, and multiply the results together. The signature and docstring are already in the editor.

### Constraints

- `lo` and `hi` are integers; `hi` may be less than `lo`, in which case the product is empty (the standard mathematical convention: an empty product is `1`, not `0` — multiplying by nothing should leave a value unchanged, exactly like adding nothing leaves a sum unchanged at `0`).
- `f` takes a single integer and returns a number (int or float).

### Hints

<details>
<summary>Hint 1</summary>

Structurally identical to `01-summation-notation`'s loop — only the accumulator's starting value (`1` instead of `0`) and the combining operation (`*=` instead of `+=`) differ.

</details>

<details>
<summary>Hint 2</summary>

Starting the accumulator at `1` is exactly what makes the empty-range case correctly return `1` with no special-cased branch, the same way starting at `0` did for summation's empty case.

</details>
