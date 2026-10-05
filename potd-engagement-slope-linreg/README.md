# ENGAGEMENT SLOPE

Beginner | regression

**Difficulty:** Easy
**Tags:** Regression

---

### Story

A lightweight linear model relating post length to engagement is the very first thing a new
content-ranking hire implements at Meta: a rite of passage, and a correctness bar every later
ranking model gets compared against.

---

### The Math

```
w = sum((x_i - mean_x) * (y_i - mean_y)) / sum((x_i - mean_x)^2)
b = mean_y - w * mean_x
```

### Input Format

```
n
x_1 y_1
...
x_n y_n
```

### Output Format

`w b`, 6 decimals.

### Constraints

- `2 <= n <= 10^5`
- Time limit: 1.0 second.

---

### Example

**Input**

```
5
1 50
2 55
3 65
4 70
5 80
```

**Output**

```
7.500000 41.500000
```
