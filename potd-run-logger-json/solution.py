def build_run_record(
    run_id: str, hyperparameters: list[tuple[str, str]], metrics: list[tuple[str, str]]
) -> dict:
    """
    Build a canonical training-run record.

    run_id: the run's id.
    hyperparameters: (key, value) pairs, in input order, keys may repeat.
    metrics: (key, value) pairs, same shape.

    Return {"run_id": run_id, "hyperparameters": {...}, "metrics": {...}}.
    Within each inner dict, keys are sorted alphabetically. A repeated key
    keeps its LAST value (later pairs overwrite earlier ones). An empty
    list of pairs gives an empty {} for that field, not an omitted key.
    """
    # TODO: build each inner dict first (last-write-wins falls out of plain
    # dict assignment), then rebuild it sorted by key.
    hp_dict = {}
    for k, v in hyperparameters:
        hp_dict[k] = v

    metrics_dict = {}
    for k, v in metrics:
        metrics_dict[k] = v

    sorted_hp = {k: hp_dict[k] for k in sorted(hp_dict.keys())}
    sorted_metrics = {k: metrics_dict[k] for k in sorted(metrics_dict.keys())}
        

    return {
        "run_id": run_id,
        "hyperparameters": sorted_hp,
        "metrics": sorted_metrics
    }
