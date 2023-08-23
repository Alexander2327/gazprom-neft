import copy


class A:
    def __copy__(self):
        clone = self.__class__()
        for key, value in vars(self).items():
            setattr(clone, key, copy.deepcopy(value))
        return clone

    def clone(self):
        return self.__copy__()


class B(A):
    pass


if __name__ == '__main__':
    test = B()
    test_clone = test.clone()
    print(test_clone)
