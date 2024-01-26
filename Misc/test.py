def morse_rencode(input_code: str) -> list[str]:
#    results = []
#    cur_char = 0 
#    for char in input_code:
#        if char == '.' and input_code[cur_char] == '.':
#            temp_str = input_code
#            temp_str = input_code.replace(char, '-') + input_code.replace(input_code[cur_char], '-')
#            if temp_str not in results:
#                results.append(temp_str)
#        cur_char = input_code.index(char)
    results = []
    for char in range(1, len(input_code)):
        if input_code[char] == input_code[char-1] == '.':
            # This slices the characters within input_code before/after. 
            # leaving an area that can insert text inbetween in this case we used '__'
            results.append(input_code[:char-1] + '_' + input_code[char+1:])

    return results

morsecode = '....'
print(morse_rencode(morsecode))
