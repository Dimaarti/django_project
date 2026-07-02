import random
import unittest
from src.task_manager.queue import UniqueQueue


class TestUniqueQueue(unittest.TestCase):

    def setUp(self):
        self.queue = UniqueQueue()

    def test_queue_exist_strategy(self):
        with self.assertRaises(ValueError):
            self.queue = UniqueQueue("LOFA")

    def test_add_to_queue(self):
        item_1 = 1
        self.queue.add(item_1)
        item = self.queue.storage[0]
        self.assertEqual(item_1, item)

    def test_remove_from_queue(self):
        item_1 = 1
        self.queue.add(item_1)
        item = self.queue.remove()
        self.assertEqual(item, item_1)

    def test_remove_item_for_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.remove()

    def test_add_and_remove_multi_value_from_queue(self):
        item_1 = 1
        item_2 = 2
        item_3 = 3
        self.queue.add(item_1)
        self.queue.add(item_2)
        self.queue.add(item_3)
        item = self.queue.remove()
        self.assertEqual(item_3, item)
        item = self.queue.remove()
        self.assertEqual(item_2, item)
        item = self.queue.remove()
        self.assertEqual(item_1, item)

    def test_unique_check(self):
        item_1 = 1
        item_2 = 2
        self.queue.add(item_1)
        self.queue.add(item_2)
        self.queue.add(item_1)
        self.assertEqual(self.queue.storage, [item_1, item_2])
        self.assertEqual(self.queue.unique_check, {item_1, item_2})

    def test_length_queue(self):
        item_0 = 0
        item_1 = 1
        item_2 = 2
        self.assertEqual(len(self.queue.storage), item_0)
        self.queue.add(item_1)
        self.queue.add(item_2)
        self.assertEqual(len(self.queue.storage), item_2)
        self.queue.add(item_1)
        self.assertEqual(len(self.queue.storage), item_2)

    def test_last_item_add_to_queue(self):
        item_1 = 1
        item_2 = 2
        item_4 = 4
        self.queue.add(item_1)
        self.queue.add(item_2)
        self.queue.add(item_4)
        self.assertEqual(self.queue.storage[-1], item_4)

    def test_add_and_remove_string_items_from_queue(self):
        str_1 = "aaa"
        str_2 = "bbb"
        self.queue.add(str_1)
        self.queue.add(str_2)
        self.queue.add(str_1)
        self.assertEqual(self.queue.storage, [str_1, str_2])

    def test_add_many_random_items(self):
        item_1 = 1
        self.queue.add(item_1)
        for _ in range(10):
            self.queue.add(random.randint(10, 20))
        item = self.queue.remove()
        self.assertEqual(item, item)

if __name__ == '__main__':
    unittest.main()
