import unittest


class TestTodo(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        self.tasks.append("Task1")
        self.assertEqual(len(self.tasks), 1)

    def test_delete_task(self):
        self.tasks.append("Task1")
        self.tasks.pop(0)
        self.assertEqual(len(self.tasks), 0)

    def test_empty_task(self):
        self.assertEqual(len(self.tasks), 0)


unittest.main(argv=[''], exit=False)
