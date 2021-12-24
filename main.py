
for number in range(2, 34):
    div = []
    
    for posdiv in range(2, number):
        if number % posdiv == 0:
            div.append(posdiv)
            continue
        
          
    if div == []:
      print(f"{number} is prime")
    else:
      print(f"{number} has {div} as divisors")
      
