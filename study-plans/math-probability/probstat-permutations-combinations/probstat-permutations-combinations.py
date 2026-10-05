def perms_and_combs(n: int, r: int) -> list:
    """
    Returns permutations, combinations, and n factorial as integers.
    """
    def recursion(n):
        if n == 0:
            return 1

        return n * recursion(n-1)
            
    denom = n-r
    perms = recursion(n)//recursion(denom)
    combs = recursion(n)//(recursion(r)*recursion(denom))
    fact = recursion(n)
    return [perms,combs,fact]
    
    pass