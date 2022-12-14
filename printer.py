import math
from io import StringIO
#source https://bit.ly/38HXSoU
def show_tree(tree, total_width=60, fill=' ', nodes_amount = 2):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, nodes_amount)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = nodes_amount**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return


show_tree([8, 5,7,6, 1,1,1, 4,9,2, 1,5,1], nodes_amount=3)