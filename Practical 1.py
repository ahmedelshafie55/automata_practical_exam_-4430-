def dfa_divisible_by_3(binary_string):
    # الحالات: 0 (عدد 1's ≡ 0 mod 3), 1 (≡ 1 mod 3), 2 (≡ 2 mod 3)
    state = 0
    for char in binary_string:
        if char == '1':
            state = (state + 1) % 3
        elif char != '0':
            return False  # مدخل غير صحيح
    return state == 0

# اختبار
test_strings = ["", "111", "10101", "1100", "111111"]
for s in test_strings:
    print(f"{s} => {'Accepted' if dfa_divisible_by_3(s) else 'Rejected'}")
