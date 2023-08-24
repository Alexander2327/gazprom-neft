import copy


class A:
    def clone(self):
        return copy.deepcopy(self)


class B(A):
    pass


if __name__ == '__main__':
    test = B()
    test_clone = test.clone()
    print(test_clone)
