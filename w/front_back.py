def front_back(str):
  tam = len(str)
  firstChar = str[0:1]
  if(tam > 1):
    lastchar = str[tam-1:tam]
  else:
    lastchar = ""
  return  lastchar + str[1:tam-1] + firstChar

