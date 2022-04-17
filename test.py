from package import*


# def egcd(a, b):
#     x, y, u, v = 0, 1, 1, 0
#     while a != 0:
#         q, r = b//a, b % a
#         m, n = x-u*q, y-v*q
#         b, a, x, y, u, v = a, r, u, v, m, n
#     gcd = b
#     return gcd, x, y


# def modinv(a, m):
#     gcd, x, y = egcd(a, m)
#     if gcd != 1:
#         return None  # modular inverse does not exist
#     else:
#         return x % m


# # affine cipher encryption function
# # returns the cipher text
# def affine_encrypt(text, key):
#     '''
#     C = (a*P + b) % 26
#     '''
#     return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26)
#                         + ord('A')) for t in text.upper().replace(' ', '')])


# # affine cipher decryption function
# # returns original text
# key = [17, 20]


# def affine_decrypt(cipher, key):
#     '''
#     P = (a^-1 * (C - b)) % 26
#     '''
#     return ''.join([chr(((modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
#                          % 26) + ord('A')) for c in cipher])


# text = "bismillahfixbuganjay"

# print(affine_encrypt(text, key))
# print(decrypt(encrypt(text)))

input()
kerangajaib()
