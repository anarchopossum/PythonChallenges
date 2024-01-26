import itertools

def solution(morsecode: str) -> list[str]:
    results = []
    for i, _ in enumerate(morsecode):
        doublet = morsecode[i:i+2]
        if doublet == '..':
            results.append(morsecode[:i] + '__' + morsecode[i+2:])
    return results

def test_0():
    assert solution('..') == ['__']

def test_1():
    assert solution('.') == []

def test_2():
    assert solution('....') == ['__..', '.__.', '..__']

def test_3():
    assert solution('_.._') == ['____']
