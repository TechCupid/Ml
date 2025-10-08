letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()

if choice == 'E':
    msg = input("Enter the message to encrypt: ").upper()
    
    encrypted_nums = []
    
    for char in msg:
        if char in letters:
            position = letters.index(char)
            position = (position + 3) % 26
            encrypted_nums.append(position)

    print("Encrypted numeric values:", encrypted_nums)

elif choice == 'D':
    nums_str = input("Enter numeric values separated by spaces: ").strip()
    nums = [int(n) for n in nums_str.split()]
    
    decrypted_msg = ""
    
    for num in nums:
        pos = (num - 3) % 26
        char = letters[pos]
        decrypted_msg += char
        
    print("Decrypted message:", decrypted_msg)

else:
    print("Invalid choice. Please select 'E' or 'D'.")