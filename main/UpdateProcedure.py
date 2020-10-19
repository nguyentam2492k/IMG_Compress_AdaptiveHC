''''
to understand the algorithm 
    B1: see diagram page 59 in "Introduction to DATA COMPRESSION - third edition - author: khalid-sayood"
    B2: read __init__ function
    B3: read UpdateProcedure() function
'''
class AdaptiveHuffmanTree:
# not yet transmitted node (weight = 0, number is min)
    NYT = None 
# Save the symbols that were transmitted
    SymbolsTransmited = {}
#init the tree (root node ~ parent = None, symbol = None)
    def __init__(self, number, parent = None, symbol = None):
        AdaptiveHuffmanTree.NYT = self
        self.right = self.left = None
        self.parent = parent
        self.symbol = symbol
        self.number = number
        self.weight = 0
#refresh the SymbolsTransmited dict
    def refresh(self):
        AdaptiveHuffmanTree.SymbolsTransmited = {}
#swap the current node with the max number node in block (block contains node with the same weight)
    def SwapNode(self, current):
        if(current != self):
            parent = current.parent
            ''' 
                * if current is the right child -> dont need to swap 
                  because number of the right child > left one
                * dont need to compare weight with the children , just need compare with sibling 
                  because the parent's weight always > the its child weight 
            '''
            if(current == parent.left and current.weight == parent.right.weight):
                # the number of left and right child dont change after swap so we need to save it before swapping
                numberBeforeSwap =  [parent.left.number, parent.right.number]
                # swap two node
                parent.left = parent.right
                parent.right = current
                # make the number as before swapping
                [parent.left.number ,parent.right.number] = numberBeforeSwap
#UpdateProcedure function
    def UpdateProcedure(self, symbol, current = None):
        # If first appearance for symbol
        if(AdaptiveHuffmanTree.SymbolsTransmited.get(symbol) == None):
            #current <- NYT
            current = AdaptiveHuffmanTree.NYT
            #NYT node gives birth to new NYT and external node
            current.right = AdaptiveHuffmanTree(current.number - 1, current, symbol)
            current.left = AdaptiveHuffmanTree(current.number - 2, current) # new NYT node
            #Increment weight of external node and old NYT node
            current.right.weight+=1 #external node
            current.weight+=1 #old NYT node
            #Sign the symbols had been transmited by an array
            AdaptiveHuffmanTree.SymbolsTransmited[symbol] = 1
        # If symbol had been appeared before
        else:
            # swap (if not max in block) -> Increment weight node
            self.SwapNode(current)
            current.weight+=1
        # if not root -> go to parent node -> swap (if not max in block) -> Increment weight node
        while (current != self):
            current = current.parent
            self.SwapNode(current)
            current.weight+=1
# traver the tree in pre-order to test
    def PreOrderTraversal(self):
        print(self.number, self.weight, self.symbol)
        if(self.left != None): self.left.PreOrderTraversal()
        if(self.right != None): self.right.PreOrderTraversal() 