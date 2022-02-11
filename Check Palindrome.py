def Palindrome(text):
  a=text[::-1]
  if a==text:
      return 'It is a palindrome'
  else:
      return 'It is not a palindrome'
print(Palindrome(input("Enter text to check if it is a palindrome or not: ")))
