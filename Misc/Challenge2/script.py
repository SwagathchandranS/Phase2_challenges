from pwn import *

# Set up the binary and connection
binary_path = './your_binary'
p = process(binary_path)  # Change this if connecting to a remote server

# Your automation logic goes here
# For example:
p.recvuntil('Enter your move: ')
p.sendline('your_move')

# Receive and print the output
output = p.recvall().decode()
print(output)

# Close the connection
p.close()
