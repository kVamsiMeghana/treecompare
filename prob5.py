# Python3 program to do level order traversal
# of a generic tree
  
# Represents a node of an n-ary tree
class Node:
     
    def __init__(self, key):
         
        self.key = key
        self.child = []
   
 # Utility function to create a new tree node
def newNode(key):   
    temp = Node(key)
    return temp
    
    
# Prints the n-ary tree level wise
def LevelOrderTraversal(root):
 
    if (root == None):
        return;
    
    list = []

    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    q.append(root); # Enqueue root
    while (len(q) != 0):
        n = len(q);
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0);
            print(p.key, end=' ')
            list.append(p.key)
            # Enqueue all children of the dequeued item
            for i in range(len(p.child)):
             
                q.append(p.child[i]);
            n -= 1
   
        print() # Print new line between two levels
    
    return list
        
        

# Python code t get difference of two lists
# Using set()
def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


# Driver program
if __name__=='__main__':
     
    '''   Let us create below tree
                  10
            /   /    \   \
            2  34    56   100
           / \         |   /  | \
          77  88       1   7  8  9
    '''
    root = newNode(10);
    (root.child).append(newNode(2));
    (root.child).append(newNode(34));
    (root.child).append(newNode(56));
    (root.child).append(newNode(100));
    (root.child[0].child).append(newNode(77));
    (root.child[0].child).append(newNode(88));
    (root.child[2].child).append(newNode(1));
    (root.child[3].child).append(newNode(7));
    (root.child[3].child).append(newNode(8));
    (root.child[3].child).append(newNode(9));
    list1 = LevelOrderTraversal(root);
   
   
    root2 = newNode(10);
    (root2.child).append(newNode(2));
    (root2.child).append(newNode(34));
    (root2.child).append(newNode(56));
    (root2.child).append(newNode(200));
    (root2.child[0].child).append(newNode(77));
    (root2.child[0].child).append(newNode(88));
    (root2.child[2].child).append(newNode(1));
    (root2.child[3].child).append(newNode(7));
    (root2.child[3].child).append(newNode(8));
    (root2.child[3].child).append(newNode(19));
    list2 = LevelOrderTraversal(root2);
    
    resultantList = Diff(list1, list2)
    resultantList.sort()
    print(resultantList)
    
