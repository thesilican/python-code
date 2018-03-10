
def tryAllUpTo(discs: int) -> int:
    for j in range(discs):
        if (j/discs)*((j-1)/(discs-1)) == 0.5:
            return j