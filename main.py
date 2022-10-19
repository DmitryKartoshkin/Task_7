
class Stak:
    def __init__(self, list_):
        self.stak = list_

    def isEmpty(self):
        '''isEmpty - проверка стека на пустоту. Метод возвращает True или False'''
        if len(self.stak) == 0:
            return False
        else:
            return True

    def push(self, element):
        '''push - добавляет новый элемент на вершину стека. Метод ничего не возвращает'''
        self.stak.append(element)

    def pop(self):
        '''pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        flag = self.isEmpty()
        if flag:
            removed = self.stak.pop()
        else:
            return None
        return removed

    def peek(self):
        '''peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        return self.stak[-1]

    def size(self):
        '''size - возвращает количество элементов в стеке.'''
        return len(self.stak)

    def is_correct_bracket(self):
        '''is_correct_bracket - решает задачу на проверку сбалансированности скобок'''
        if len(self.stak) % 2 != 0:
            return f"Несбалансированно"
        total = 0
        for i in self.stak:
            if i in "([{":
                total += 1
            elif i in "}])":
                total -= 1
            if total < 0:
                return f"Несбалансированно"
        if total == 0:
            return f"Сбалансированно"
        else:
            return f"Несбалансированно"


# if __name__ == '__main__':



