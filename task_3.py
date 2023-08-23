test_dict = {
    1: '0000',
    2: '00',
    3: '0000000',
    4: '77777777777',
    5: '',
    6: '010000000',
}

max_seq = max([len(value) for value in test_dict.values() if len(value) == value.count('0')])
print(max_seq)
