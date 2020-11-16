# 两个等长句子s1, s2,相同位置字符不同的数量
def hamming_distance_str(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("length is different")
    return sum(e1 != e2 for e1, e2 in zip(s1, s2))


def hamming_distance_binary(n1: int, n2: int) -> int:
    return bin(n1 ^ n2 & 0xffffffff).count("1")


def hamming_distance_binary1(n1: int, n2: int) -> int:
    count = 0
    val = n1 ^ n2
    while val & 0xffffffff:
        count += 1
        val &= val - 1
    return count
