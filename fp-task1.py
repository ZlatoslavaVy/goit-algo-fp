class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end=" ")
            current = current.next
        print('None')

    def reverse(self):
        """Реалізувати метод реверсування однозв'язного списку, змінюючи посилання між вузлами"""
        # 1 -> 2 -> 3 => 3 -> 2 -> 1
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Змінюємо напрямок посилання
            prev = current            # Переміщуємо prev вперед
            current = next_node       # Переміщуємо current вперед
        
        self.head = prev  # Оновлюємо голову списку

    def merge_sort(self, head):
        """Реалізувати метод сортування для однозв'язного списку (сортування злиттям)"""
        # 2 -> 1 -> 3 => 1 -> 2 -> 3
        
        # Базовий випадок: список з 0 або 1 елемента
        if not head or not head.next:
            return head
        
        # Розділяємо список на дві половини
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        
        # Рекурсивно сортуємо обидві половини
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        
        # Об'єднуємо відсортовані половини
        return self.sorted_merge(left, right)

    def get_middle(self, head):
        """Отримати елемент в середині однозв'язного списку"""
        if not head:
            return head
        
        slow = head
        fast = head
        
        # Повільний покажчик рухається на 1, швидкий на 2
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def sorted_merge(self, a, b):
        """Об'єднує два відсортовані списки"""
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def merge_sorted_lists(self, list1, list2):
        """Реалізувати метод, що об'єднує два відсортовані однозв'язні списки в один відсортований список"""
        # 1 -> 2
        # 1 -> 3
        # Output: 1 -> 1 -> 2 -> 3
        
        # Якщо один зі списків порожній
        if not list1.head:
            self.head = list2.head
            return
        if not list2.head:
            self.head = list1.head
            return
        
        # Використовуємо метод sorted_merge для об'єднання
        self.head = self.sorted_merge(list1.head, list2.head)


if __name__ == '__main__':

    print("=" * 60)
    print("ЗАВДАННЯ 1: Реверсування списку")
    print("=" * 60)
    
    first_list = LinkedList()
    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування:")
    first_list.print_list()

    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 2: Сортування списку")
    print("=" * 60)
    
    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 3: Об'єднання двох відсортованих списків")
    print("=" * 60)
    
    # Створюємо другий відсортований список
    second_list = LinkedList()
    second_list.insert_at_beginning(3)   # Додаємо в second_list 
    second_list.insert_at_beginning(8)   # Додаємо в second_list 
    second_list.insert_at_beginning(12)  # Додаємо в second_list 
    
    print("Перший відсортований список:")
    first_list.print_list()
    
    print("Другий відсортований список:")
    second_list.print_list()
    
    # Створюємо третій список для результату
    merged_list = LinkedList()
    merged_list.merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено:")
    merged_list.print_list()