def cigar_party(cigars, is_weekend):
  if(is_weekend and cigars >= 40):
    success = True
  elif(cigars >= 40 and cigars <= 60):
    success = True
  else:
    success = False
    
  return success
