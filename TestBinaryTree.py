#  File: TestBinaryTree.py

#  Description: Writing helper functions for binary trees

#  Student Name: Rakshana Govindarajan

#  Student UT EID: rg38236

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 27 April 2016

#  Date Last Modified: 28 April 2016 


class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None


class Tree (object):
  def __init__ (self):
    self.root = None

  # search for a node with a key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if(key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    newNode = Node (val)

    if(self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while(current != None):
        parent = current
        if(val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if(val < parent.data):
        parent.lchild = newNode
      else:
        parent.rchild = newNode


  # Returns true if two binary trees are similar
  def isSimilar (self, self_node, pNode_node):
    result = True
    # If the first tree's node is None
    if(self_node == None):
      return (pNode_node == None)

    # If the second tree's node is None
    if(pNode_node == None):
      return False

    # If the data from both tree's nodes don't match, returning False
    if(self_node.data != pNode_node.data):
      return False

    # Recursively checking the left and right subtree comparisons of both trees, if matches, then returning True
    if((self.isSimilar(self_node.lchild, pNode_node.lchild) == True) and (self.isSimilar(self_node.rchild, pNode_node.rchild) == True)):
      return True

   # Otherwise returning False
    else:
      return False


  
  # Prints out all nodes at the given level
  def printLevel (self, level):
    count = 1
    current = 0
    # Sets the current level at the root node
    if (count <= level):
      current = [self.root]
      while current:
        # Makes a list of the following nodes
        next = list()
        print("Level " + str(count) + ": ", end = " ")
        for item in current:
          # For node on that level, prints the node
          print(item.data, end = " ")
          # Appending the right and left children of the node to the list
          if(item.lchild != None):
            next.append(item.lchild)
          if(item.rchild != None):
            next.append(item.rchild)

        print()
        # Going to the next level
        current = next
        count += 1

    
  # Returns the height of the tree
  def getHeight (self, self_node):
    # Returns 0 if the node is None
    if(self_node == None):
      return 0

    else:
      # Finds the heights of the left and right subtrees and gets the max, then adds 1 to the height to account for the root node
      return (max(self.getHeight(self_node.lchild), self.getHeight(self_node.rchild)) + 1)
    
    
    


  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes (self, self_node):
    # Returns 0 if the node is None
    if(self_node == None):
      return 0

    else:
     # Finds the number of nodes in the left subtree and the right subtree and adds 1 to account for the root node
     return(self.numNodes(self_node.lchild) + self.numNodes(self_node.rchild) + 1)

     
     



def main():
    # Create three trees - two are the same and the third is different
    tree1 = Tree()
    a = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    print("Tree1 has the following numbers: " + str(a))
    for item in a:
      tree1.insert(item)

    #tree1.printTree(tree1.root)

    tree2 = Tree()
    b = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    print("Tree2 has the following numbers: " + str(b))

    for item in b:
      tree2.insert(item)

    tree3 = Tree()
    c = [12, 22, 83, 15, 14, 96, 43, 7, 98, 4]
    print("Tree3 has the following numbers: " + str(c))

    for item in c:
      tree3.insert(item)

    print()   

    
    # Test your method isSimilar()
    # Tree1 and Tree2 are the same, checking the function on them
    print("Testing method isSimilar()")
    print("Tree1 and Tree2 are: ", end = " ")
    y = tree1.isSimilar(tree1.root, tree2.root)
    if(y == True):
      print("True/Similar")
    else:
      print("False/Not similar")
    

    # Checking tree1 and tree3 which are not the same
    print("Tree1 and Tree3 are: ", end = " ")
    z = tree1.isSimilar(tree1.root, tree3.root)
    if(z == True):
      print("True/Similar")
    else:
      print("False/Not similar")
    print()
    

    # Print the various levels of two of the trees that are different
    print("Testing method printLevel()")

    # Printing various levels of Tree1
    print("Tree1 Levels: ")
    p = tree1.printLevel(1)

    print()

    print("Tree3 Levels: ")
    p2 = tree3.printLevel(1)
    print()

    # Get the height of the two trees that are different
    print("Testing method getHeight()")
    h = tree1.getHeight(tree1.root)
    # Printing height of tree1
    print("Height of Tree1 is: " + str(h))

    # Printing height of tree3
    h2 = tree3.getHeight(tree3.root)
    print("Height of Tree3 is: " + str(h2))
    print()
    

    # Get the number of nodes in the left and right subtree
    print("Testing method numNodes()")
    num = tree1.numNodes(tree1.root.lchild)
    print("Total number of nodes in left subtree Tree 1 = " + str(num))

    num = tree1.numNodes(tree1.root.rchild)
    print("Total number of nodes in right subtree Tree 1 = " + str(num))

    print()
    num = tree3.numNodes(tree3.root.lchild)
    print("Total number of nodes in left subtree Tree 3 = " + str(num))

    num = tree3.numNodes(tree3.root.rchild)
    print("Total number of nodes in right subtree Tree 3 = " + str(num))



     
  
main()