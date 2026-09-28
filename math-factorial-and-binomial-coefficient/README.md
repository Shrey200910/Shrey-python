# Factorial and the Binomial Coefficient (n choose k)

Beginner | notation | foundations

### The problem, from first principles

"How many ways can you arrange `n` distinct items in a row?" and "how many ways can you pick `k` items out of `n`, where order doesn't matter?" are two of the most common counting questions in probability — and both have short, closed-form answers built directly out of `02-product-notation`'s `∏`. This question implements both, since the second (the binomial coefficient) is exactly what the Binomial distribution later in this track counts with.

### From theory to code

Implement `factorial(n)` first, then `n_choose_k(n, k)` in terms of it. The signatures and docstrings are already in the editor.

### Constraints

- `n` and `k` are non-negative integers, with `0 <= k <= n` for `n_choose_k`.
- `factorial(0) == 1` (the empty-product convention from `02-product-notation`).
- Return integers, not floats, even though the intermediate division in `n_choose_k` could otherwise produce one.

### Hints

<details>
<summary>Hint 1</summary>

`factorial(n)` is `∏_{i=1}^{n} i` — the exact same accumulate-by-multiplying loop as `02-product-notation`'s `product`, just written out directly here rather than imported (every question's `solution.py` is self-contained).

</details>

<details>
<summary>Hint 2</summary>

Use integer division (`//`) for the final division in `n_choose_k`, since the numerator is always exactly divisible by the denominator for valid `n`/`k` — the result is a count, and counts are integers.

</details>
