class Friends:
    def __init__(self, connections):
        self.data = {}
        for i in connections:
            i = list(i)
            if not i[0] in self.data:
                self.data[i[0]] = [i[1]]
            else:
                if i[1] not in self.data[i[0]]:
                    self.data[i[0]].append(i[1])
            if not i[1] in self.data:
                self.data[i[1]] = [i[0]]
            else:
                if i[0] not in self.data[i[1]]:
                    self.data[i[1]].append(i[0])

    def add(self, connection):
        connection = list(connection)
        if (connection[0] in self.data and connection[1] in self.data[connection[0]]) or (connection[1] in self.data and connection[0] in self.data[connection[1]]):
            result = False
        else:
            result = True
            if connection[0] in self.data:
                self.data[connection[0]].append(connection[1])
            else:
                self.data[connection[0]] = [connection[1]]
            if connection[1] in self.data:
                self.data[connection[1]].append(connection[0])
            else:
                self.data[connection[1]] = [connection[0]]
        return result

    def remove(self, connection):
        connection = list(connection)
        if connection[0] in self.data and connection[1] in self.data:
            result = True
            if len(self.data[connection[0]]) == 1:
                del self.data[connection[0]]
            else:
                self.data[connection[0]].remove(connection[1])
            if len(self.data[connection[1]]) == 1:
                del self.data[connection[1]]
            else:
                self.data[connection[1]].remove(connection[0])
        else:
            result = False
        return result

    def names(self):
        return set(self.data.keys())

    def connected(self, name):
        if name in self.data:
            return set(self.data[name])
        else:
            return set()
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"  
    print(letter_friends.data)
