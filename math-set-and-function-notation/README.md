# Set and Function Notation Used in ML Papers

Beginner | notation | foundations

### The problem, from first principles

ML papers write things like `f: ℝⁿ → ℝᵐ`, `x ∈ ℝⁿ`, `A ⊆ B`, and `argmax_i f(i)` constantly, without ever pausing to define them — they're assumed background, the same way `for` and `if` are assumed background in code. This question makes the two most operationally useful pieces concrete: **`⊆`** (subset), which shows up in "is this a valid choice from the allowed set," and **`argmax`**, which shows up everywhere a model has to pick the single best option out of many (classification's predicted class, a search algorithm's best move, a language model's next token under greedy decoding).

### From theory to code

Implement `is_subset(a, b)`, checking whether every element of set `a` is also in set `b`, then `argmax(values)`, returning the **index** of the largest value. The signatures and docstrings are already in the editor.

### Constraints

- `a` and `b` are Python `set` objects for `is_subset`.
- `values` is a non-empty list or tuple of numbers for `argmax`.
- If more than one value is tied for the maximum, return the **first** such index (matching NumPy's `np.argmax` convention).

### Hints

<details>
<summary>Hint 1</summary>

`is_subset(a, b)` is one line using Python's own set operations — no explicit loop needed, though writing the loop version once is worth doing mentally to see what the operator is actually checking.

</details>

<details>
<summary>Hint 2</summary>

For `argmax`, track both the best value seen so far and its index as you scan once through `values`; only update when you find something **strictly** greater, which is exactly what keeps the first tied index instead of the last.

</details>
