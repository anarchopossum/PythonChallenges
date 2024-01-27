def frogs(X, S, Y):
    # Initialize a list to store the number of flies each frog can eat
    #result = [1]
    results = []
    catch = 0
    for froggy in range(len(X)):
        catch = 0
        frog_pos = X[froggy] + S[froggy]
        frog_neg = X[froggy] - S[froggy]
        print(f"{frog_pos}, {frog_neg}")

        for fly in Y:
            if frog_neg <= fly <= frog_pos:
                catch += 1
                print(f"Catch: {catch}")
            print(catch)
        results.append(catch)
        print(results)
    return results

def test1():
    assert frogs([1,4,5],[2,3,5],[2,3,5]) == [2,3,3]

def test2():
    assert frogs([],[2,3,5],[2,3,5]) == []


def test3():
    assert frogs([1,4,5],[2,3,5],[]) == [0,0,0]

print(f"final resutls:{frogs([1,4,5],[2,3,5],[2,3,5]) == [2,3,3]}")
