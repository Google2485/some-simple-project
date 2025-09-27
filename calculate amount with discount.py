#input net amount
amt=int(input("Enter amount="))
#calculate amount with discount
if (amt>0):
  if amt<=5000:
    disc=amt*0.10
  elif amt<=15000:
    disc=amt*0.15
  elif amt<=25000:
    disc=amt*0.20
  else:
    disc=amt*0.5
  print("Discount Amount=",disc)
  print("To be paid by coustomer=",amt-disc)
else:
  print("Invalid amount")