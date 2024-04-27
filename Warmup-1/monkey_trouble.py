def monkey_trouble(a_smile, b_smile):
  both_true = (a_smile == True and b_smile == True)
  both_false = (a_smile == False and b_smile == False)
  
  if both_true or both_false:
    return True
  else:
    return False
    
