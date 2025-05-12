import sys
import codecs
input = sys.stdin.readline

n = input()

encod = codecs.encode(n, 'rot13')
print(encod)

# result = ''
# for char in text:
#     if 'A' <= char <= 'Z':
#         result += chr((ord(char) - ord('A')+ 13) %26 + ord('A'))
#     elif 'a' <= char <= 'z':
#         result += chr((ord(char) - ord('a') + 13) %26 + ord('a'))
#     else:
#         result += char

