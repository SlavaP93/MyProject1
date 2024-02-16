class LinkedList:
    def __init__(self):
        self.__counter = 0
        self.__head = None

    def append(self, obj):
        if self.__head is None:
            self.__head = Node(obj, self.__counter)
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = Node(obj, self.__counter)
        self.__counter += 1

    def __str__(self):
        if self.__head is None:
            return "LinkedList is empty"
        current = self.__head
        result = '['
        while current is not None:
            result += current.get_data()
            current = current.next
            if current is not None:
                result += ', '
        return result + ']'

    def get(self, ind):
        if self.__head is None:
            return None
        current = self.__head
        while current is not None:
            if current.get_ind() == ind:
                return current.get_data()
            current = current.next
        return None

    def remove(self, ind):
        if self.__head is None:
            return None
        if ind == 0:
            self.__head = self.__head.next
            return
        current = self.__head
        prev = None
        while current is not None:
            if current.get_ind() == ind:
                if prev is not None:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        return None



class Node:
    def __init__(self, obj, link):
        self.__obj = obj
        self.__link = link
        self.next = None

    def get_data(self):
        return str(self.__obj)

    def get_ind(self):
        return self.__link



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
my_list.remove(1)
print('Новый список:', my_list)