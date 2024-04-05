# Built-in imports
def reverse(text):
  """
  Function that reverses text
  Parameters:
  text - string
  Output:
  reversed version of text
  """
  if len(text) <= 1:
    return text
  check = text[0]
  return reverse(text[1:]) + check
  
    
def is_palindrome(text):
  """
  Function that checks if text is a palindrome
  Parameters:
  text - string
  Output:
  True/False
  """
  text = text.lower()
  if len(text) <= 1:
    return True
  a = text[0]
  b = text[-1]
  if a == b:
    return is_palindrome(text[1:-1])
  else: 
    return False
  