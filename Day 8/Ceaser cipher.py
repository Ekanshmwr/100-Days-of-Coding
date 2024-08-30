alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
solution = []
if action == "decode":
   shift *= -1
   for string in text:
       position = alphabet.index(string)
       new_postion = position + shift
       c = alphabet[new_postion]
       solution.append(c)
elif action == "encode":
   for string in text:
       position = alphabet.index(string)
       new_postion = position + shift
       c = alphabet[new_postion]
       solution.append(c)
else:
    print('wrong')
result = ''.join(solution)
if action == 'decode':
  print(f'message successfully decoded : ',result)
elif action == 'encode':
  print(f'message successfully encoded : ',result)
else:
    print('try again')



