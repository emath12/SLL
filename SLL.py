
class Node:
    def __init__(self, id, right=None, next=None, left=None, prev=None):
        self.id = id
        self.left: Node = left
        self.right: Node = right
        self.next: Node = next
        self.prev: Node = prev

    def print_by_row(self):
        rows = []
        b_index = 0
        room = self

        while room:

            rows.append([])
            columns = rows[b_index]

            columns.append(room.id)

            if room.left:
                left = room.left
                while left:
                    columns.insert(0, left.id)
                    left = left.left

            if room.right:
                right = room.right
                while right:
                    columns.append(right.id)
                    right = right.right

            room = room.next

            b_index += 1

        for row in rows:
            print(row)


class Location:
    def __init__(self, far_left: bool, far_right: bool, far_front: bool, rows_deep: int = 0):

        """

        Instruction passed to append to notate where it should go.

        :param far_left: bool
        :param far_right: bool
        :param far_front: bool
        :param rows_deep: int
        """

        if (far_left and far_right) or (far_left and far_front) or (far_right and far_front) or (far_right and far_front and far_left):
            print("invalid instruction")

        if far_left:
            self.location = "far_left"
        elif far_right:
            self.location = "far_right"
        elif far_front:
            self.location = "far_front"

        if rows_deep < 0:
            print("invalid rows_deep call")
        else:
            self.rows_deep = rows_deep

class SLL:

    def __init__(self):
        self.head: Node = None
        self.total_nodes = 0

    def append(self, loc: Location):
        """
        Append a node to the edges of the grid. Far left indicates that you want it appended to the far left
        of the indicated row. Far right indicates the same but vice versa. Far_front indicates
        that you want it appended to the tip of the indicated row.
        :param loc: A location struct
        :return: void
        """
        if self.head is None:
            self.head = Node(id=0, prev=None)
        else:
            cur_node = self.head
            rows_deep = loc.rows_deep

            while rows_deep != 0:
                if not cur_node:
                    print("you entered an invalid row_deep value")
                    return

                if cur_node.next:
                    cur_node = cur_node.next

                rows_deep -= 1

            the_last_node = None

            if loc.location == "far_left":
                left = right = prev = None
                while cur_node:
                    right = the_last_node
                    the_last_node = cur_node
                    cur_node = cur_node.left

                if the_last_node.prev:
                    if the_last_node.prev.left:
                        prev = the_last_node.prev.left
                else:
                    prev = None

                if the_last_node.next:
                    if the_last_node.next.left:
                        next = the_last_node.next.left
                else:
                    next = None

                cur_node = Node(id=self.total_nodes, next=next, prev=prev, right=the_last_node)
                the_last_node.left = cur_node

            elif loc.location == "far_right":
                left = right = prev = None

                while cur_node:
                    the_last_node = cur_node
                    cur_node = cur_node.right

                if the_last_node.prev:
                    if the_last_node.prev.right:
                        prev = the_last_node.prev.right
                else:
                    prev = None

                if the_last_node.next:
                    if the_last_node.next.right:
                        next = the_last_node.next.right
                else:
                    next = None

                cur_node = Node(id=self.total_nodes, next=next, left=the_last_node, prev=prev)
                the_last_node.right = cur_node

            elif loc.location == "far_front":
                left = right = prev = None

                while cur_node:
                    the_last_node = cur_node
                    cur_node = cur_node.next

                if the_last_node.right:
                    if the_last_node.right.next:
                        right = the_last_node.right.next
                else:
                    left = None
                if the_last_node.left:
                    if the_last_node.left.next:
                        left = the_last_node.left_next
                else:
                    left = None

                cur_node = Node(id=self.total_nodes, left=left, right=right, prev=the_last_node)
                the_last_node.next = cur_node

            else:
                print("invalid instruction")

        self.total_nodes += 1

    def traverse(self, row):
        cur_node = self.head
        for i in range(0, row):
            cur_node = cur_node.next
            if not cur_node and i != row:
                print("invalid traversal ")

        left_node = cur_node.left
        right_node = cur_node.right
        left_len = right_len = 0
        while left_node:
            left_node = left_node.left
            left_len += 1


        while right_node:
            right_node = right_node.right
            right_len += 1


        return right_len, left_len

    def insert(self, row, col, loc, node):
        cur_node = self.head

        for i in range(0, row):
            cur_node = self.head.next
            if not cur_node and i != row:
                print("invalid insertion location")

        right_len, left_len = self.traverse(row)

        head_loc = round((right_len + left_len) / 2)

        if head_loc < col:
            for i in range(0, abs(col - head_loc)):
                cur_node = cur_node.right
        elif head_loc > col:
            for i in range(0, abs(col - head_loc)):
                cur_node = cur_node.left

        if loc.location == "far_left":

            prev_left = cur_node.left

            if prev_left:
                prev_left.right = node
            cur_node.left = node
            node.left = prev_left
            node.right = cur_node

        elif loc.location == "far_right":
            prev_right = cur_node.right

            if prev_right:
                prev_right.left = node
            cur_node.right = node
            node.right = prev_right
            node.left = cur_node

        elif loc.location == "far_front":
            prev_next = cur_node.next
            if prev_next:
                prev_next.prev = node

            cur_node.next = node
            node.next = prev_next
            node.prev = cur_node

        else:
            print("invalid location struct")

    def remove(self, row, col):
        cur_node = self.head
        for i in range(0, row):
            if cur_node:
                cur_node = cur_node.next
            else:
                print("invalid insertion row")

        right_len, left_len = self.traverse(row)
        head_loc = round((right_len + left_len) / 2)

        if head_loc < col:
            for i in range(0, abs(col - head_loc)):
                cur_node = cur_node.right
        elif head_loc > col:
            for i in range(0, abs(col - head_loc)):
                cur_node = cur_node.left

        print(cur_node.id)
        if cur_node.right:
            if cur_node.left:
                cur_node.right.left = cur_node.left
                cur_node.left.right = cur_node.right
            else:
                cur_node.right.left = None
                cur_node.right = None


        if cur_node.left:
            if cur_node.right:
                cur_node.left.right = cur_node.right
                cur_node.right.left = cur_node.left
            else:
                cur_node.left.right = None
                cur_node.left = None


        if cur_node.next:
            if cur_node.prev:
                cur_node.next.prev = cur_node.prev
                cur_node.prev.next = cur_node.next
            else:
                cur_node.prev.next = None
                cur_node.next = None

        if cur_node.prev:
            if cur_node.next:
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev
            else:
                cur_node.next.prev = None
                cur_node.prev = None

    def print_as_matrix(self):
        """
        Prints the existing grid as a matrix. Note: if the number of cols and rows and uneven,
        the print will reflect such. Prints the id to indicate which room is which.
        :return: none
        """
        if self.head is None:
            print("S")
        else:
            self.head.print_by_row()





