import UpdateProcedure as UpdateProcedure
import EnDeCodeASymbol as EnDeCodeASymbol
import math

#find and return the external node and road from root to it
def FindExternalNode(AHM_Tree, symbol):
    road = ""
    current = AHM_Tree
    while(current.symbol != symbol):
        if(current.left.symbol == symbol): 
            current = current.left
            road += "0"
        elif (current.right.symbol == symbol): 
            current = current.right
            road += "1"
        elif (current.left.symbol == None): 
            current = current.left
            road += "0"
        else: 
            current = current.right
            road += "1"
    return [current, road]
#find and return the road from root to the NYT node
def FindRoadToNYT(AHM_Tree):
    road = ""
    current = AHM_Tree
    while(current != UpdateProcedure.AdaptiveHuffmanTree.NYT):
        if (current.left.symbol == None): 
            current = current.left
            road += "0"
        else: 
            current = current.right
            road += "1"
    return road
def EncodeProcedure(inputSourceSize, symbols) :
    '''
    @param: inputSourceSize : # the total leafs ~ total size of source
    @param: symbols : the symbol string that need to encode
    @return: encodedString : the binary string encoded from the input
    '''
    [e, r] = EnDeCodeASymbol.FindER(inputSourceSize)
    # the total nodes
    totalNodes = 2*inputSourceSize - 1 
    # create a tree with only one node (NYT)
    AHM_Tree = UpdateProcedure.AdaptiveHuffmanTree(totalNodes)
    AHM_Tree.refresh()
    # the binary string encoded from the input
    encodedString = ""
    for s in symbols :
        # if s have not been transmited yet
        if(AHM_Tree.SymbolsTransmited.get(s) == None):
            #find road to NYT node
            roadToNYT = FindRoadToNYT(AHM_Tree)
            encodedString +=  (roadToNYT + EnDeCodeASymbol.Encode(e, r, s))
            AHM_Tree.UpdateProcedure(s)
        else: # if s have been transmited yet
            #find external node and road to it
            [externalNode, roadToExternalNode] = FindExternalNode(AHM_Tree, s)
            encodedString += roadToExternalNode
            AHM_Tree.UpdateProcedure(s, externalNode)
    return encodedString

