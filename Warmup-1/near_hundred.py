def near_hundred(n):
  pertoCem = abs(100 - n) 
  pertoDuz = abs(200 - n)
  if pertoCem <= 10 or pertoDuz <= 10:
    return True
  else:
    return False
    
