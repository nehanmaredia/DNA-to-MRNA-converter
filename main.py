import sys

dna = str(input("Enter a DNA sequence: "))
dns = dna.replace("-", "") if "-" in dna else dna.replace(" ", "")
dnas = list(dns)

for i in range(len(dnas)):
  if dnas[i].upper() == "A":
    dnas[i] = "U"
  elif dnas[i].upper() == "T":
    dnas[i] = "A"
  elif dnas[i].upper() == "C":
    dnas[i] = "G"
  elif dnas[i].upper() == "G":
    dnas[i] = "C"
  else:
    print()
    print("Error found in DNA sequence")
    sys.exit()

print()
ques = str(input("Do you want a space ' ' between every 3 bases, do you want a '-' very 3 bases, or nothing. Type 'space' or 'dash' or 'none': "))

if ques.lower() == "space":
  space_mrna = []
  for i in range(len(dnas)):
    if (i + 1) % 3 != 0 or i == len(dnas) - 1:
      space_mrna.append(dnas[i])
    else:
      space_mrna.append(dnas[i] + " ")
  end_mrna = "".join(space_mrna)
  print()
  print(end_mrna)

elif ques.lower() == "dash":
  dash_mrna = []
  for i in range(len(dnas)):
    if (i + 1) % 3 != 0 or i == len(dnas) - 1:
      dash_mrna.append(dnas[i])
    else:
      dash_mrna.append(dnas[i] + "-")
  end1_mrna = "".join(dash_mrna)
  print()
  print(end1_mrna)

else:
  print()
  mrna = "".join(dnas)
  print(mrna)
