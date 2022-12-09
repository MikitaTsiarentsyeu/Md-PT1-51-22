def find_matched_by_pattern(pattern):
    def f(s, p = pattern):
        for c in s:
            if c == p[0]:
                p = p[1:]
            elif c in p: 
                break
            if not p: 
                return True
        return False
    return f

predicate = find_matched_by_pattern('acs')

print(predicate('access'))

predicate = find_matched_by_pattern('test')

print(predicate(' t e s t i n g '))