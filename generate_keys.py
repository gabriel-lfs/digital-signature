from Crypto.PublicKey import RSA

chave_a = RSA.generate(1024)
chave_b = RSA.generate(1024)

with open('./public_rsa_a.pem', 'wb+') as file:
    file.write(chave_a.publickey().exportKey())

with open('./private_rsa_a.pem', 'wb+') as file:
    file.write(chave_a.exportKey())

with open('./public_rsa_b.pem', 'wb+') as file:
    file.write(chave_b.publickey().exportKey())

with open('./private_rsa_b.pem', 'wb+') as file:
    file.write(chave_b.exportKey())