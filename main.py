def handle_string(string: str) -> str:
    result = ''
    substring = ''
    need_to_collect = False
    opened_brackets = 0
    closed_brackets = 0
    digit_found = 0

    for symbol in string:
        if symbol == ')':
            if opened_brackets == 0:
                continue

            if opened_brackets:
                substring += symbol

            closed_brackets += 1

            if opened_brackets == closed_brackets:

                if digit_found:
                    result += digit_found * handle_string(substring)
                else:
                    result += handle_string(substring)
                need_to_collect = False
                substring = ''
                opened_brackets = 0
                digit_found = 0
                closed_brackets = 0
            continue

        if need_to_collect:
            substring += symbol
            continue

        if symbol.isdigit():
            digit_found = int(symbol)
            continue

        if symbol == '(':
            opened_brackets += 1
            need_to_collect = True
            continue

        if digit_found:
            result += symbol * digit_found
            digit_found = 0
            continue

        result += symbol

    return result


# 3AB2(Z3K) → AAABZKKKZKKK
res = handle_string('3AB2(Z3K)')
assert res == 'AAABZKKKZKKK'

# 2(Z3(KA)) → ZKAKAKAZKAKAKA
res = handle_string('2(Z3(KA))')
assert res == 'ZKAKAKAZKAKAKA'

# 2(Z3(KA))2(AZ) -> ZKAKAKAZKAKAKAAZAZ
res = handle_string('2(Z3(KA))2(AZ)')
assert res == 'ZKAKAKAZKAKAKAAZAZ'

# 2(Z3(KA3(3B)))2(AZ) -> ZKABBBBBBBBBKABBBBBBBBBKABBBBBBBBBZKABBBBBBBBBKABBBBBBBBBKABBBBBBBBBAZAZ
res = handle_string('2(Z3(KA3(3B)))2(AZ)')
assert res == 'ZKABBBBBBBBBKABBBBBBBBBKABBBBBBBBBZKABBBBBBBBBKABBBBBBBBBKABBBBBBBBBAZAZ'

# 2(AB3(ZZ)) -> ABZZZZZZABZZZZZZ
res = handle_string('2(AB3(ZZ))')
assert res == 'ABZZZZZZABZZZZZZ'

# AB3(ZZ) -> ABZZZZZZ
res = handle_string('AB3(ZZ)')
assert res == 'ABZZZZZZ'

# AB3ZZ -> ABZZZZ
res = handle_string('AB3ZZ')

# AB3((A))() -> ABAAA
res = handle_string('AB3((A))()')
assert res == 'ABAAA'
