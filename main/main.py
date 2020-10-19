import EncodeProcedure as Enp
import DecodeProcedure as Dep

if __name__ == "__main__":
    InputSourceSize = 26 # example the alphabet in english has 26 chacracters
    
    #encode
    symbols = [1,1,18,4,22,1,18,11] # ~ [a,a,r,d,v,a,r,k]
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    print("the encoded string is:", encodedString) # = 00000101000100000110001011010110001010
    #decode
    decodedArray = Dep.DecodeProcedure(InputSourceSize, encodedString)
    print("the decoded symbols array is:", decodedArray) # = [1,1,18,4,22,1,18,11]
