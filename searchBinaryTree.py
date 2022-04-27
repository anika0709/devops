class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def searchBinaryTree(root):
	if root == None:
		return float('-inf')


	res = root.data
	lres = searchBinaryTree(root.left)
	rres = searchBinaryTree(root.right)
	#print(res, lres, rres)
	if res < lres:
		res = lres
	if rres > res:
		res = rres
	print(res, lres, rres)
	return res


if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
    list_res = []
    print(searchBinaryTree(root))


