# PROFILE SIMILARITY

Beginner | linear-algebra

**Difficulty:** Easy
**Tags:** Linear Algebra

---

### Story

LinkedIn's "People You May Know" starts as raw cosine similarity between two profile embedding
vectors before any graph signal is layered on top.

---

### The Math

```
cos(u, v) = (u . v) / (||u|| * ||v||)
```

### Input Format

```
d
u_1 ... u_d
v_1 ... v_d
```

### Output Format

Scalar similarity, 6 decimals.

### Constraints

- `1 <= d <= 10^4`
- Time limit: 1.0 second.

---

### Example

**Input**

```
4
1 2 0 1
2 0 1 1
```

**Output**

```
0.500000
```
