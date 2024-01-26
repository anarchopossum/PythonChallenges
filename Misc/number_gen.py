from functools import reduce

def solution(keyboard, sequence):
    # key_to_index = {x: i for i, x in enumerate(keyboard)}
    
    # last_key = keyboard[0]
    # time = 0
    # for key in sequence:
    #     distance = abs(key_to_index[last_key] - key_to_index[key])
    #     time += distance
    #     last_key = key

    return reduce(lambda x, y: (x[0] + abs(x[1] - keyboard.find(y)), keyboard.find(y)), sequence, (0, 0))[0]
    # return time



def test_0():
    assert solution("0123456789", "210") == 4

def test_1():
    assert solution("8459761203", "5439") == 17
