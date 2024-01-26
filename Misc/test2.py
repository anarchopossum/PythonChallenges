def morse_rencode(input_code: str) -> list[str]:
    results = []
    for i in range(len(input_code)):
        if input_code[i:i+2] == "..":
            temp_str = input_code[:i] + "--" + input_code[i+2:]
            results.append(temp_str)
    return results

morsecode = '....'
print(morse_rencode(morsecode))

