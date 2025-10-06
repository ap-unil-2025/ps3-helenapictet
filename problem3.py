"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        value = input('Enter a number, or type done when you are finished').strip().lower()
        if value == 'done':
            break
        try:
            number = float(value)
            numbers.append(number)
        except ValueError:
            print('Invalid input. please enter a valid number or done')
    return numbers



def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = (sum(numbers)/len(numbers))
    analysis["minimum"] = min(numbers)
    analysis["maximum"] = max(numbers)

    even_count = 0
    odd_count = 0
    for n in numbers:
        if int(n) % 2 == 0:   # cast to int in case numbers contain floats
            even_count += 1
        else:
            odd_count += 1
    analysis["even"] = even_count
    analysis["odd"] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        print("No analysis results to display.")
        return

    print("\nAnalysis Results:")
    print("-" * 20)
 # Loop through dictionary and print each key/value
    for key, value in analysis.items():
        # Capitalize the key and align nicely
        print(f"{key.capitalize():<12}: {value}")



def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()