from collections import Counter


class StringClass:
    def __init__(self, string1):
        self.string1 = string1

    def length_of_string(self, string):
        return len(string)

    def string_to_list(self, string):
        return list(string)


class PairsPossible(StringClass):
    def __init__(self, string1, string2):
        self.store = []
        self.string2 = string2
        super().__init__(string1)

    def all_possible_pairs(self):
        list1 = StringClass.string_to_list(self, self.string1)
        list2 = StringClass.string_to_list(self, self.string2)
        for element in list1:
            for ele in list2:
                self.store.append((int(element), int(ele)))
        print()
        return list1, list2, self.store

    def print_possible_pairs(self):
        print("All possible pairs : ")
        for i in range(len(self.store)):
            print(f"{self.store[i]}", end=" ")
        print()


class SearchCommonElements:
    def __init__(self, string1, string2):
        self.dictionary = {}
        self.string1 = string1
        self.string2 = string2

    def common_elements(self):
        obj = PairsPossible(self.string1, self.string2)
        list1, list2, store = obj.all_possible_pairs()
        new_list = list1 + list2
        self.dictionary = dict(Counter(new_list))
        common_values = [int(key) for key, value in self.dictionary.items() if value > 1]
        print(f"Common elements : {common_values}")
        print()
        return store


class EqualSumPairs:
    def __init__(self, string1, string2):
        self.dictionary = {}
        self.string1 = string1
        self.string2 = string2

    def common_sum(self):
        obj = SearchCommonElements(self.string1, self.string2)
        store = obj.common_elements()
        for i in range(len(store)):
            if sum(store[i]) in self.dictionary:
                self.dictionary[sum(store[i])].append(store[i])
            else:
                self.dictionary[sum(store[i])] = [store[i]]
        print("Sum : pairs")
        for key, value in sorted(self.dictionary.items()):
            print(f"{key}   : {value}, Number of pairs = {len(value)}")


str1 = str(input("Enter first string : "))
str2 = str(input("Enter second string : "))
k = PairsPossible(str1, str2)
k.all_possible_pairs()
k.print_possible_pairs()
obj2 = SearchCommonElements(str1, str2)
obj2.common_elements()
obj3 = EqualSumPairs(str1, str2)
obj3.common_sum()
