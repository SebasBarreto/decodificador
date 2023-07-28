print ("hello, Contosoville!")
# This is a comment that won't be interpreted as a command.
# Associate variable town with the value "Contosoville"
town = "Contosoville"
# Print a message about the secret location
print( "The town I am looking for is " + town )
# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )
    # Invoke the power to chant on the phrase "Contosoville!"
chant( "Contosoville!" )
def lasso_letter( letter, shift_amount ):
    letter_code = ord(letter.lower())
    decoded_letter_code = letter_code + shift_amount
    decoded_letter = chr(decoded_letter_code)
    return decoded_letter
print(lasso_letter('p', -2))
print(lasso_letter('N', 13))
three_two = 3 % 2
eleven_four = 11 % 4 
five_ten = 5 % 10

print(three_two)
print(eleven_four)
print(five_ten)
# Define a function to find the truth by shifting the letter by the specified amount
def lasso_letter( letter, shift_amount ):
    # Invoke the ord function to translate the letter to its ASCII code 
    # Save the code to the letter_code variable
    letter_code = ord(letter.lower())
    
    # The ASCII number representation of lowercase letter 'a'
    a_ascii = ord('a')

    # The number of letters in the alphabet
    alphabet_size = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    # Convert the ASCII number to the character or letter
    decoded_letter = chr(true_letter_code)

    # Send the decoded letter back
    return decoded_letter
print(lasso_letter('a', 2))

# Define a function to find the truth by shifting the letter by a specified amount
def lasso_letter( letter, shift_amount ):
    # Invoke the ord function to translate the letter to its ASCII code 
    # Save the code value to the variable called letter_code
    letter_code = ord(letter.lower())
    
    # The ASCII number representation of lowercase letter a
    a_ascii = ord('a')

    # The number of letters in the alphabet
    alphabet_size = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    # Convert the ASCII number to the character or letter
    decoded_letter = chr(true_letter_code)

    # Send the decoded letter back
    return decoded_letter

# Define a function to find the truth in a secret message
# Shift the letters in a word by a specified amount to discover the hidden word
def lasso_word( word, shift_amount ):

    # This variable is updated each time another letter is decoded
    decoded_word = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lasso_letter() function is invoked with each letter and the shift amount
        # The result (the decoded letter) is stored in a variable called decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # The decoded_letter value is added to the end of the decoded_word value
        decoded_word = decoded_word + decoded_letter

    # The decoded_word is sent back to the line of code that invoked this function
    return decoded_word

# Try to decode the word "terra"
print( "Shifting terra by 13 gives: \n" + lasso_word( "terra", 13 ) )
print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )

