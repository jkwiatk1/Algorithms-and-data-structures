from unittest import TestCase
from src import common
from src.avltree import AVL, Node


class TestAVL(TestCase):
    def test_adding_to_avl(self):
        avl = self.build_simple_tree()

        root = avl.get_root()

        common.displayAsTree(root)

        self.assertEquals(root.value, 4)
        self.assertEquals(root.left.value, 2)
        self.assertEquals(root.left.left.value, 1)
        self.assertEquals(root.left.right.value, 3)
        self.assertEquals(root.right.value, 7)
        self.assertEquals(root.right.left.value, 5)
        self.assertEquals(root.right.right.value, 8)
        self.assertEquals(root.right.right.right.value, 9)

    def test_removing_avl(self):
        avl = self.build_simple_tree()

        root = avl.get_root()

        common.displayAsTree(root)

        # start remove

        avl.remove(9)

        common.displayAsTree(root)

        self.assertEquals(root.value, 4)
        self.assertEquals(root.left.value, 2)
        self.assertEquals(root.left.left.value, 1)
        self.assertEquals(root.left.right.value, 3)
        self.assertEquals(root.right.value, 7)
        self.assertEquals(root.right.left.value, 5)
        self.assertEquals(root.right.right.value, 8)
        self.assertEquals(root.right.right.right, None)

    def build_simple_tree(self):
        avl = AVL()
        avl.add(5)
        avl.add(4)
        avl.add(2)
        avl.add(3)
        avl.add(1)
        avl.add(8)
        avl.add(7)
        avl.add(9)
        return avl

    def test_advanced_removing(self):
        avl = self.build_simple_tree()

        root = avl.get_root()

        common.displayAsTree(root)

        avl.remove(4)

        common.displayAsTree(root)

    def test_searching(self):
        avl = self.build_simple_tree()

        root = avl.get_root()

        common.displayAsTree(root)

        searched = avl.search(4)
        searched100 = avl.search(100)

        self.assertEquals(searched, 4)
        self.assertEquals(searched100, None)




    def test_height_left(self):
        avl = AVL()

        avl.add(5)
        avl.add(4)
        avl.add(2)
        avl.add(3)

        root = avl.get_root()
        self.assertEquals(avl.height(root), 3)

        pass



    def test_right_rotate_basic(self):

        avl = AVL()

        root = Node(42)
        root.left = Node(16)
        root.left.left = (Node(8))

        new_root:Node = avl.right_rotate(root)

        self.assertEquals(new_root.value, 16)
        self.assertEquals(new_root.right.value, 42)
        self.assertEquals(new_root.left.value, 8)
        pass

    def test_lll_right_rotate(self):

        avl = AVL()

        z = Node(value=42, height=3)
        t4 = Node(50)
        z.right = t4

        y= Node(value=16, height=2)
        t3 = Node(20)
        y.right = t3

        x = Node(value=10,height=2)
        t1 = Node(7)
        t2 = Node(8)
        x.left = t1
        x.right = t2

        # glowne polaczenie nodow left-> left-> left
        z.left = y
        y.left = x

        print('Left Left -> Right Rotate')
        common.displayAsTree(z)

        new_root:Node = avl.right_rotate(z)

        common.displayAsTree(new_root)

        # asercje rotacji prawej
        self.assertEquals(new_root.value, y.value)
        self.assertEquals(new_root.left.value, x.value)
        self.assertEquals(new_root.right.value, z.value)

        # asercje pozostałych dzieci t1,t2,t3,t4
        self.assertEquals(x.left.value, t1.value)
        self.assertEquals(x.right.value, t2.value)
        self.assertEquals(z.left.value, t3.value)
        self.assertEquals(z.right.value, t4.value)

        #asercje wysokości
        self.assertEquals(y.height,3)
        self.assertEquals(z.height,2)
        self.assertEquals(x.height,2)

        pass

    def test_rrr_left_rotate(self):
        avl = AVL()

        z = Node(value=20, height=3)
        t1 = Node(18)
        z.left = t1

        y = Node(value=25, height=2)
        t2 = Node(21)
        y.left = t2

        x = Node(value=30, height=2)
        t3 = Node(22)
        t4 = Node(31)
        x.left = t3
        x.right = t4

        # glowne polaczenie nodow right-> right-> right
        z.right = y
        y.right = x

        print('Right Right -> Left Rotate')
        common.displayAsTree(z)

        new_root: Node = avl.left_rotate(z)

        common.displayAsTree(new_root)

        # asercje rotacji prawej
        self.assertEquals(new_root.value, y.value)
        self.assertEquals(new_root.left.value, z.value)
        self.assertEquals(new_root.right.value, x.value)

        # asercje pozostałych dzieci t1,t2,t3,t4

        self.assertEquals(z.left.value, t1.value)
        self.assertEquals(z.right.value, t2.value)
        self.assertEquals(x.left.value, t3.value)
        self.assertEquals(x.right.value, t4.value)

        # asercje wysokości
        self.assertEquals(y.height, 3)
        self.assertEquals(z.height, 2)
        self.assertEquals(x.height, 2)

        pass

    def test_lr_rotate(self):
        avl = AVL()

        t1, t2, t3, t4, x, y, z = self.left_right()

        print('Left Right -> Left Right Rotate')
        common.displayAsTree(z)

        new_root: Node = avl.left_right_rotate(z)

        common.displayAsTree(new_root)

        # asercje podstawowe
        self.assertEquals(new_root.value, x.value)
        self.assertEquals(new_root.left.value, y.value)
        self.assertEquals(new_root.right.value, z.value)

        # asercje pozostałych dzieci t1,t2,t3,t4

        self.assertEquals(y.left.value, t1.value)
        self.assertEquals(y.right.value, t2.value)
        self.assertEquals(z.left.value, t3.value)
        self.assertEquals(z.right.value, t4.value)

        # asercje wysokości
        self.assertEquals(x.height, 2)
        self.assertEquals(y.height, 1)
        self.assertEquals(z.height, 1)

        pass

    def left_right(self):
        z = Node(value=25, height=4)
        t4 = Node(30)
        z.right = t4
        y = Node(value=20, height=3)
        t1 = Node(18)
        y.left = t1
        x = Node(value=23, height=2)
        t2 = Node(21)
        t3 = Node(24)
        x.left = t2
        x.right = t3
        # glowne polaczenie nodow right-> right-> right
        z.left = y
        y.right = x
        return t1, t2, t3, t4, x, y, z

    def test_right_left_rotate(self):

        avl = AVL()

        t1, t2, t3, t4, x, y, z = self.right_left()

        print('Right Left -> Right Left Rotate')
        common.displayAsTree(z)

        new_root: Node = avl.right_left_rotate(z)

        common.displayAsTree(new_root)

        # asercje podstawowe
        self.assertEquals(new_root.value, x.value)
        self.assertEquals(new_root.left.value, z.value)
        self.assertEquals(new_root.right.value, y.value)

        # asercje pozostałych dzieci t1,t2,t3,t4

        self.assertEquals(z.left.value, t1.value)
        self.assertEquals(z.right.value, t2.value)
        self.assertEquals(y.left.value, t3.value)
        self.assertEquals(y.right.value, t4.value)

        # asercje wysokości
        self.assertEquals(x.height, 2)
        self.assertEquals(y.height, 1)
        self.assertEquals(z.height, 1)

        pass

    def right_left(self):
        z = Node(value=10, height=3)
        t1 = Node(8)
        z.left = t1
        y = Node(value=15, height=2)
        t4 = Node(18)
        y.right = t4
        x = Node(value=13, height=1)
        t2 = Node(11)
        t3 = Node(14)
        x.left = t2
        x.right = t3
        # glowne polaczenie nodow right-> right-> right
        z.right = y
        y.left = x
        return t1, t2, t3, t4, x, y, z

    def test_rr_get_balance(self):
        avl = AVL()

        z = Node(value=42, height=3)
        t4 = Node(50)
        z.right = t4

        y= Node(value=16, height=2)
        t3 = Node(20)
        y.right = t3

        x = Node(value=10,height=1)
        t1 = Node(7)
        t2 = Node(8)
        x.left = t1
        x.right = t2

        # glowne polaczenie nodow left-> left-> left
        z.left = y
        y.left = x
        print('Left Left ')
        common.displayAsTree(z)

        self.assertEquals(avl.get_balance(z), -2)
        self.assertEquals(avl.get_balance(y), -1)
        self.assertEquals(avl.get_balance(x), 0)

        pass

    def test_ll_get_balance(self):
        avl = AVL()

        z = Node(value=20, height=3)
        t1 = Node(18)
        z.left = t1

        y = Node(value=25, height=2)
        t2 = Node(21)
        y.left = t2

        x = Node(value=30, height=1)
        t3 = Node(22)
        t4 = Node(31)
        x.left = t3
        x.right = t4

        # glowne polaczenie nodow right-> right-> right
        z.right = y
        y.right = x

        print('Right Right ')
        common.displayAsTree(z)

        self.assertEquals(avl.get_balance(z), 2)
        self.assertEquals(avl.get_balance(y), 1)
        self.assertEquals(avl.get_balance(x), 0)

        pass

    def test_lr_get_balance(self):
        avl = AVL()

        t1, t2, t3, t4, x, y, z = self.left_right()

        print('Left Right ')
        common.displayAsTree(z)

        self.assertEquals(avl.get_balance(z), -2)
        self.assertEquals(avl.get_balance(y), 1)
        self.assertEquals(avl.get_balance(x), 0)

        pass

    def test_rl_get_balance(self):
        avl = AVL()

        t1, t2, t3, t4, x, y, z = self.right_left()

        print('Right Left ')
        common.displayAsTree(z)

        self.assertEquals(avl.get_balance(z), 2)
        self.assertEquals(avl.get_balance(y), -1)
        self.assertEquals(avl.get_balance(x), 0)

        pass