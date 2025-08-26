def vulnerable_function(user_input):
    buffer = [''] * 8
    print(f"Original buffer size: {len(buffer)}")
    
    # Unsafe copying simulation
    try:
        for i, char in enumerate(user_input):
            buffer[i] = char  # will raise IndexError if overflow
        print("Buffer content:", ''.join(buffer))
        print("No overflow occurred.")
    except IndexError:
        print("Buffer Overflow Detected!")
        print("Alert: input exceeded safe buffer length.")

# User input
user_input = input("Enter input for vulnerable function: ")
vulnerable_function(user_input)
