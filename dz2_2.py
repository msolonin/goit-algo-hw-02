from collections import deque


# Завдання 2:
def check_palindrome(word: str) -> bool:
    """ Function for check the word is palindrome or not. Its not sensitive for letter register and whitespaces
    :param word: Any word
    :type word: str
    :return: True/False
    :rtype: bool
    """
    # Clean word from whitespaces and register
    word = word.lower().replace(' ', '')
    # Create collection from word
    collection = deque(list(word))
    # Calculate number for iterations for word
    iterations = int(len(collection) / 2) + 1
    # If number of characters less than 2 its not palindrome
    if len(collection) < 2:
        return False
    # Cycle in range of limited calculations. Its possible also using while here, but i don`t like unlimited cycles
    for _ in range(iterations):
        if len(collection) >= 2 and collection.pop() != collection.popleft():
            return False
    else:
        return True
