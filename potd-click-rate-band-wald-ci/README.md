# THE CLICK-RATE BAND

Beginner | probability-and-statistics

**Difficulty:** Easy
**Tags:** Probability & Statistics

---

### Story

A search-ads team reports today's click-through rate to stakeholders every morning, and a bare
point estimate without an uncertainty band has burned them before on low-traffic days.

---

### The Math

```
p_hat = clicks / n
SE = sqrt( p_hat * (1 - p_hat) / n )
interval = p_hat +- z * SE,   z = 1.959964   (95% interval)
```

### Input Format

```
n clicks
```

### Output Format

`p_hat lower upper`, 6 decimals.

### Constraints

- `1 <= clicks <= n <= 10^9`
- Time limit: 1.0 second.

---

### Example

**Input**

```
1000 45
```

**Output**

```
0.045000 0.032151 0.057849
```
