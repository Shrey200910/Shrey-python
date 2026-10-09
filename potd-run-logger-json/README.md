# THE RUN LOGGER

Beginner | mlops

**Difficulty:** Easy
**Tags:** MLOps

---

### Story

DoorDash's ML platform requires every training run, no exceptions, to log its full configuration and
final metrics before the model artifact is allowed into the registry. This is the logger every later
MLOps problem in this set assumes already exists.

---

### The Problem

No math here: this is a structured-serialization problem. Given a run id, a set of hyperparameter
key/value pairs, and a set of metric key/value pairs, produce a single canonical serialized record.

### Input Format

```
run_id
h
key_1 val_1
...
key_h val_h
m
metric_1 val_1
...
metric_m val_m
```

### Output Format

A single JSON object with keys `run_id`, `hyperparameters` (object), `metrics` (object).
Hyperparameter and metric keys are sorted alphabetically within their own object.

### Constraints

- `0 <= h, m <= 100`
- Time limit: 1.0 second.

---

### Example

**Input**

```
run_0042
2
lr 0.001
batch_size 64
1
val_loss 0.231
```

**Output**

```json
{
	"run_id": "run_0042",
	"hyperparameters": { "batch_size": "64", "lr": "0.001" },
	"metrics": { "val_loss": "0.231" }
}
```
