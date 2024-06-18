def remove_vowels(input_string):
    vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    result = ''.join([char for char in input_string if char not in vowels])
    return result

def main():
    user_input = input("Enter a string: ")
    result = remove_vowels(user_input)
    print("String without vowels:", result)
    input("Press Enter to exit...") 

if __name__ == "__main__":
    main()