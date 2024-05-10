def date_fashion(you, date):
  if(you <= 2 or date <= 2 ):
    table = 0
  elif(you >= 8 or date >= 8):
    table = 2
  else:
    table = 1
    
  return table
