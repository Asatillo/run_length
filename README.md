# Run-Length Encoding and Decoding

This repository contains a Python implementation of a simple Run-Length Encoding (RLE) algorithm, including encoding, decoding, and a test function.

## Usage

To use the provided functions, run the script with the appropriate mode and bit vector as command-line arguments.

```bash
python rle.py [mode] [bit_vector]
```

## Modes:
1) Encode: encode mode compresses the given bit vector using Run-Length Encoding.

```bash
python rle.py encode 100000000000000011000000001
```
2) Decode: decode mode decompresses the given compressed bit vector.

```bash
python rle.py decode 00111010110111101110
```

3) Test: test mode performs encoding, decoding, and checks if the original bit vector matches the decompressed result.

```bash
python rle.py test 100000000000000011000000001
```

## Implementation Details
### Encoding (encode function):
The encode function takes a bit vector as input and compresses it using Run-Length Encoding. It counts consecutive zeros and represents them using unary coding, followed by the binary representation of the count of zeros. Consecutive ones are not encoded.

### Decoding (decode function):
The decode function reverses the encoding process. It reads the unary coding to determine the number of consecutive zeros and appends the corresponding number of zeros followed by a one to the decompressed result.

### Testing (test function):
The test function performs encoding, decoding, and checks if the original bit vector matches the decompressed result. It helps ensure the correctness of the encoding and decoding functions.

## Example
```bash
python rle.py test 100000000000000011000000001
```
This will output the original bit vector, the encoded result, the decoded result, and whether the original and decompressed results match.

## References
Learn more about Unary Coding: [Unary Coding - Wikipedia](https://en.wikipedia.org/wiki/Unary_coding)