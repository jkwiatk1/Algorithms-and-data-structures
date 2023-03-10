import math
from io import StringIO
from heap import MaxHeap

output = StringIO()
def create_tree(row,n,nodes_amount,last_row,total_width, fill = ' ', SepareWhenEqualToNodesAmount = 0):
    if row != last_row:
        output.write('\n')
    columns = nodes_amount ** row
    col_width = int(math.floor((total_width * 0.25) / columns))
    output.write(str(n).center(col_width, fill))
    if row != 0 and SepareWhenEqualToNodesAmount == nodes_amount:
        output.write("|")
        if row == 2:
            output.write("  ")
    return row


def show_tree(tree, total_width=300, fill=' ', nodes_amount = 2):
    rowsB = 0
    last_row = -1
    for rowP in range(0,len(tree)//nodes_amount,1):
        rows = nodes_amount**rowP
        SepareWhenEqualToNodesAmount = 0
        for i, n in enumerate(tree):
            if rows == 1 and i == 0:
                row = 0
                last_row = create_tree(row,n, nodes_amount, last_row, total_width,fill, SepareWhenEqualToNodesAmount)

            elif i < rowsB + rows and i >= rowsB:
                SepareWhenEqualToNodesAmount += 1
                row = rowP
                last_row = create_tree(row,n, nodes_amount, last_row, total_width,fill, SepareWhenEqualToNodesAmount)
                if SepareWhenEqualToNodesAmount == nodes_amount:
                    SepareWhenEqualToNodesAmount = 0
        rowsB = rows + rowsB

    print(output.getvalue())
    print('-' * total_width)
    return


heapBinary = MaxHeap(4)
heapBinary.add(2)
heapBinary.add(3)
heapBinary.add(9)
heapBinary.add(4)
heapBinary.add(1)
heapBinary.add(8)
heapBinary.add(7)
heapBinary.add(15)
heapBinary.add(20)
heapBinary.add(41)
heapBinary.add(32)
heapBinary.add(5)
heapBinary.add(4)
heapBinary.add(1)
heapBinary.add(8)
heapBinary.add(6)
heapBinary.add(13)
heapBinary.add(22)
heapBinary.add(16)
heapBinary.add(56)
heapBinary.add(17)

show_tree(heapBinary.get_nodes(), nodes_amount = 4)