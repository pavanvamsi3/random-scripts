# This will generate the server key, asks to enter passphrase
openssl genrsa -aes128 -out server.key 2048

# This command will remove the passphrase
openssl rsa -in server.key -out server.key

# Creating a CSR 
openssl req -new -days 365 -key server.key -out server.csr

# Generating a certificate
openssl x509 -in server.csr -out server.crt -req -signkey server.key -days 365
