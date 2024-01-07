import sys

def encode(bit_vector):    
    # Initialize variables
    count = 0
    compressed_res = ""
    
    # Iterate through the bit vector
    for bit in bit_vector:
        if bit == "0":
            count += 1
        elif bit == "1":
            # occurence of 0's before a single one in binary
            occur = bin(int(count))
            
            # length of the occurence of 0's
            # subsctracting 2 because every binary starts with '0b'
            length = len(occur)-2
            
            # unary representation of lenght is the length of the (occurence - 1) followed by a zero 
            unary = (length-1)*"1" + "0"
            
            compressed_res += unary + occur[2:]
            count = 0

    return compressed_res

def decode(compressed_res):
    # Initialize variables
    decompressed_res = ""
    binary_count_zeros = ""
    cons_ones = 0
    i = 0
    while len(compressed_res) > i:
        if compressed_res[i] == "0":
            # if the bit is equal to 0, get the number of consecutive 1's before it
            num_length = cons_ones + 1
            # move the index to the next bit
            i+=1
            # get the next (consecutive 1's + 1) characters from compressed_res
            binary_count_zeros = compressed_res[i:i+num_length]
            # convert the binary number to decimal and add that number of zeros followed by 1 to the decompressed_res
            decompressed_res += "0"*int(binary_count_zeros, 2) + "1"
            # move the index to the bit after the number of consecutive 1's
            i = i+num_length
            # reset the number of consecutive 1's
            cons_ones = 0
        elif compressed_res[i] == "1":
            # if the bit is equal to 1, increment the number of consecutive 1's and the index
            cons_ones += 1
            i += 1
            
    return decompressed_res

def test(bit_vector):
    compressed_result = encode(bit_vector)
    decompressed_result = decode(compressed_result)
    print("Compression:", bit_vector)
    print("Encoded:", compressed_result)
    print("Decoded:", decompressed_result)
    print(bit_vector == decompressed_result)

if __name__ == "__main__":
    # get arguments from command line
    if len(sys.argv) < 3:
        print("Please provide a mode and a bit vector")
        sys.exit(1)
        
    mode = sys.argv[1]
    bit_vector = sys.argv[2]

    if mode == "encode":
        print(encode(bit_vector))
    elif mode == "decode":
        print(decode(bit_vector))
    elif mode == "test":
        test(bit_vector)
    else:
        print("Invalid mode. Please choose from the following: encode, decode, test")