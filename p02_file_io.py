# Open and write file
file1 = open('presidents.txt', 'w')
file1.write('a. George W Bush')
file1.close()

# Read file
file2 = open('presidents.txt')
print(file2.read())
file2.close()

print('----------')

# Append
file3 = open('presidents.txt', 'a')
# file3.write('\n'.join('b. Barack Obama') + '\n')
file3.write('\n' + 'b. Barack Obama' + '\n')                # suggesting string + '\n' to start a new line
file3.writelines('c. Donald Trump')                         # writelines() usually applied for list argument
file3.close()
file3 = open('presidents.txt')
print(file3.read())
file3.close()

# Readline
file4 = open('presidents.txt')
print(file4.readline())
print(file4.tell())                                         # ATTENTION: current position of cursor is line 2
for line in file4.readlines():
    print('[' + line + ']')
file4.close()

# Cursor
file5 = open('presidents.txt')
file5.seek(5)
file5.seek(1, 1)                                            # Expecting position 6, why throw exception???
print(file5.tell())
file5.close()
