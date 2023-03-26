def say_the_number(num):
    # Resolve the case where 0 is an input
    if num == 0:
        return "Zero."

    # Define the base words for numbers up to 20, and multiples of 10 up to 90
    base_words = {
                0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                70: 'seventy', 80: 'eighty', 90: 'ninety'
	}

    # Define the suffixes for numbers in the thousands, millions, billions, and trillions
    suffixes = {0: ' trillion', 1: ' billion', 2: ' million', 3: ' thousand', 4: ""}

    # Convert the num to a string
    num_str = str(num)

	# Create a string of numbers the lenght of 15 as a representation of the original number
    while len(num_str) < 15:
        num_str = '0' + num_str
    padded_num = num_str

    # Split the string into groups of three digits each
    groups = []
    for i in range(0, len(padded_num), 3):
        group = padded_num[i:i+3]
        groups.append(group)

    # Initialize a result list
    result = []

    # Iterate over the groups and convert each group into words
    for group_number, digits in enumerate(groups):
        # Convert the group to an integer
        group_int = int(digits)

        # Skip the group if it's zero or return 'zero' if input is 0
        if group_int == 0:
            if len(groups) == 1:
                return base_words[0] + '.'
            continue

        # Initialize a group_words string
        group_words = ""

        # Check if there is a value in the hundreds place
        hundreds = int(digits[0])

        if hundreds:
            group_words += base_words[hundreds] + " hundred"

        # Extract the tens and ones place from the digits
        tens = int(digits[1])*10
        ones = int(digits[2])

        if tens + ones:
            # Add 'and' between the hundreds place and the tens place if the hundreds place exists
            if hundreds:
                group_words += " and "
            # Check if the value of the tens and ones place is in the base_words dictionary
            if tens + ones in base_words:
                group_words += base_words[tens + ones]
            else: 
                group_words += base_words[tens] + "-" + base_words[ones]

        # Append the group_words to the result list with its corresponding suffix
        result.append(group_words + suffixes[group_number])

    if not result:
        return ""
    # if there's only one item in the result, capitalize it and add a period
    if len(result) == 1:
        return result[0].capitalize() + "."
    # if the last item in the result contains the word "and", join all items with commas and capitalize the first letter
    if "and" in result[-1]:
        result = ", ".join(result).capitalize()
    else:
        result = ", ".join(result[:-1]).capitalize() + " and " + result[-1]
    return result + "."


if __name__ == "__main__":
    while(True):
        # Get user input
        user_input = input("Please enter a number from 0 to 999,999,999,999\n")
        # If user inputs 'exit' app will close
        if user_input.lower() == "exit":
            break
        # Prints the number in spoken word
        print(say_the_number(user_input))
