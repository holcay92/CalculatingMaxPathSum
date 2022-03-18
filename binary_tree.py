class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

def insert(self, val):
    if not self.val:
        self.val = val
        return

    if self.val == val:
        return

    if val < self.val:
        if self.left:
            self.left.insert(val)
            return
        self.left = BSTNode(val)
        return

    if self.right:
        self.right.insert(val)
        return
    self.right = BSTNode(val)


def main():
    bst = BSTNode()
    with open('input.txt', 'r') as file:
        twoDlist = [[int(x) for x in line.split()] for line in file]

    row = col = len(twoDlist)
    # filling array with zeros
    iterColumn = 1
    for item1 in range(0, row):
        for item2 in range(0, row - iterColumn):
            twoDlist[item1].append(int(0))
        iterColumn = iterColumn + 1
        
    for i in range(0, row):
        for j in range(0, row):
            bst.insert(twoDlist[i][j])

if __name__ == "__main__":
    main()