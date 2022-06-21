
nested_list = [
    ['a', ['x', 'y', ['w', 0, 'w'], 'z'], 'b', [1, 0, 9], 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class MyIter:

    def __init__(self, iterable) -> None:
        self.list = []
        for item in iterable[::-1]:
            if type(item) == list:
                while item:
                    e = item.pop()
                    if type(e) == list:
                        item.extend(e)
                    else:
                        self.list.append(e)

        self.len = len(self.list)
        self.cursor = -1

    def __iter__(self):
        self.list.reverse()
        return self

    def __next__(self):
        if self.cursor == self.len-1:
            raise StopIteration
        self.cursor += 1
        return self.list[self.cursor]


if __name__ == '__main__':
    flat_list = [item for item in MyIter(nested_list)]
    print(flat_list)

    # for item in MyIter(nested_list):
    #     print(item)
