import UpdateProcedure as UpdateProcedure
import EnDeCodeASymbol as EnDeCodeASymbol
import math
    
def DecodeProcedure(inputSourceSize, encodedString) :
    '''
    @param: inputSourceSize : # the total leafs ~ total size of source
    @param: encodedString : the binary string encoded from the source
    @return: decodedArray : the symbols array decoded from the encodedString
    '''

    [e, r] = EnDeCodeASymbol.FindER(inputSourceSize)
    # the total nodes
    totalNodes = 2*inputSourceSize - 1
    # create a tree with only one node (NYT)
    AHM_Tree = UpdateProcedure.AdaptiveHuffmanTree(totalNodes)
    AHM_Tree.refresh()
    
    decodedArray = []
    #convert encodedString to an array
    encodedArray = list(encodedString)

    while (encodedArray != []):
        current = AHM_Tree
        #if current is not an external node (leaf node) -> read next bit
        while(current.left != None):
            if (encodedArray.pop(0) == "0"): 
                current = current.left
            else: current = current.right
        #if current is NYT
        if(current == UpdateProcedure.AdaptiveHuffmanTree.NYT):
            symbol = EnDeCodeASymbol.Decode(e,r,encodedArray)
        #if current is not NYT (leaf contain a symbol)
        else:
            symbol = current.symbol
        #append the decoded symbol to array and update tree
        decodedArray.append(symbol)
        AHM_Tree.UpdateProcedure(symbol, current)
    return decodedArray






