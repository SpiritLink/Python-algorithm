import struct
with open('output', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk) #  double형 1개, int형 1개, char형 4개'
    print(result)