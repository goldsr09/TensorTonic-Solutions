def independence_test(p_a: float, p_b: float, p_a_and_b: float) -> dict:
    """
    Returns the rounded product and independence decision in a dictionary.
    """

    if p_a_and_b == (p_a*p_b):
        return {"p_a_times_p_b": p_a*p_b, "is_independent": True}
    else:
        return {"p_a_times_p_b": p_a*p_b, "is_independent": False}
    pass