
class Node(object):
    def __init__(self, value, left = None, right = None, height = 1, parent = None ):
        self.height = height
        self.value = value
        self.parent : Node = parent
        self.right = right
        self.left = left



class AVL(object):
    '''

    Implementacja samo równoważącego drzewa BST - AVL(Adelson-Velsky and Landis).
    Inspirowana wykładem dr. Krzysztofa Skoniecznego - Drzewa.

    Asymptotyczne złozoności czasowe:
    Search: O(logn)
    Insert: O(logn)
    Delete: O(logn)

    Pamięciowa: O(n)

    '''

    def __init__(self):
        self.root:Node = None
        pass

    def add(self, value):
        '''
        Dodaje nowy node do drzewa i je balansuje algorytmem AVL.
        :param value:
        :return:
        '''
        if self.root == None:
            self.root = Node(value)
            return self.root
        else:

            root = self.add_req(self.root, value)
            self.root = root
            return root


    def add_req(self, current, value):
        '''
        Rekurencyjna funkcja dodwania elementu do drzewa AVL.
        :param current: aktualny node
        :param value: wartość którą dodajemy
        :return: korzeń drzewa - root
        '''
        if current == None:
            return Node(value)
        else:

            if value > current.value:
                current.right = self.add_req(value=value, current=current.right)
            elif value < current.value:
                current.left = self.add_req(value=value, current=current.left)

            current.height = self.height(current)
            balance = self.get_balance(current)
            if balance == 0:
                return current
            if balance < -1:
                #drzewo lewe zbyt duże
                if value < current.left.value:
                    # układ LL
                    return self.right_rotate(current)
                else:
                    #układ LR
                    return self.left_right_rotate(current)
            elif balance > 1:
                #drzewo prawe zbyt duże
                if value > current.right.value:
                    #układ RR
                    return self.left_rotate(current)
                else:
                    #układ RL
                    return self.right_left_rotate(current)

            return current



    def search(self, value):
        if self.root != None:
            return self.search_req(value, self.root)
        else:
            return None

    def search_req(self, value, current):
        if value == current.value:
            return current.value
        elif value > current.value and current.right != None:
            return self.search_req(value, current.right)
        elif value < current.value and current.left != None:
            return self.search_req(value, current.left)
        else:
            return None
    def remove(self, value):
        if self.root == None:
            return None
        else:
            root = self.remove_req(self.root, value)
            self.root = root
            return root

    def remove_req(self, current, value):

        if current == None:
            return None
        # przeszukiwanie binarne
        if value < current.value:
            current.left = self.remove_req(current.left, value)

        elif value > current.value:
            current.right = self.remove_req(current.right, value)
        else:
            # znajdz nastepny
            if current.left==None:
                temp = current.right
                current = None
                return temp
            # znajdz poprzedni
            elif current.right==None:
                temp = current.left
                current = None
                return temp

            temp = self.find_empty_on_left(current.right)

            #podmiana wartosci
            current.value = temp.value

            current.right = self.remove_req(current.right, temp.value)
        #zostal usuniety
        if current==None:
            return current

        current.height = self.height(current)
        balance = self.get_balance(current)

        # Balance the tree
        if balance < -1:

            if self.get_balance(current.left) <= 0:
                # LL
                return self.right_rotate(current)
            else:
                #LR
                return self.left_right_rotate(current)
        if balance > 1:
            if self.get_balance(current.right)>= 0:
                #RR
                return self.left_rotate(current)
            else:
                #RL
                return self.right_left_rotate(current)

        return current

    def get_root(self):
        '''
        Zwraca aktualnego roota(korzeń) drzewa.
        :return:
        '''
        return self.root

    '''
    Zwraca wysokość drzewa.
    '''
    def height(self, current: Node):
        if current.left == None:
            leftH = 1
        else:
            leftH = self.height(current.left) + 1
        if current.right == None:
            rightH = 1
        else:
            rightH = self.height(current.right) + 1

        return max(leftH, rightH)

    def right_rotate(self, z):
        '''
        Prypadek left left.

        z->y,->x, => y->x,z

        Detailed:
        x-> t1,t2 => x -> t1,t2
        y ->x,t3 => y -> x,z
        z -> y,t4 => z -> t3,t4

        :return: new root
        '''
        y:Node = z.left
        t3 = y.right
        y.right = z
        z.left = t3

        #update heights from z & y
        y.height = self.height(y)
        z.height = self.height(z)

        return y

    def left_rotate(self, z):
        '''
        Prypadek right right.

        z->y->,x => y->x,z

        Detailed:
        z-> t1 => t1,t2
        y -> t2,x => y -> z,x
        x -> t3,t4

        :return: new root
        '''
        # zmiana roota, rotacja w lewo
        y = z.right
        t2:Node = y.left
        y.left = z
        z.right = t2

        #update heights from z & y
        y.height = self.height(y)
        z.height = self.height(z)

        return y


    def left_right_rotate(self, z):
        '''
        Prypadek left right.
        z->y,->,x => z, -> x, -> y, =>  x->y,z
        :return:
        '''
        y = z.left
        x = self.left_rotate(y)
        z.left = x
        new_root = self.right_rotate(z)

        # update heights from z & y & x
        y.height = self.height(y)
        z.height = self.height(z)
        x.height = self.height(x)

        return new_root

    def right_left_rotate(self,z):
        '''
        Prypadek right left.
        z->,y->x, => z-> ,x -> ,y =>  x->z,y
        :return:
        '''
        y = z.right
        x = self.right_rotate(y)
        z.right = x
        new_root = self.left_rotate(z)

        # update heights from z & y & x
        y.height = self.height(y)
        z.height = self.height(z)
        x.height = self.height(x)
        return new_root

    def safe_height(self, current):
        '''
        None safety height.
        :param current: node can be None
        :return: height
        '''
        if current== None:
            return 0
        else:
            return current.height

    def get_balance(self, current):
        '''
        Zwraca balans pomiedzy lewym i prawym poddrzewem jako różnica wysokości R-L.
        :param current: węzeł dla którego liczymy balans
        :return: wartość
        '''
        if current == None:
            return 0
        else:
            return self.safe_height(current.right) - self.safe_height(current.left)

    def find_empty_on_left(self, current):
        if current == None or current.left == None:
            return current
        else:
            return self.find_empty_on_left(current.left)


