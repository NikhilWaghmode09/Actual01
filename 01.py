# ser = "meaning \"Sir\", a common intentional misspelling used in crypto circles \"GM ser\"."
# wagmi = "\"We're All Gonna Make It,\" a common saying in crypto and trading circles signaling camaraderie and a positive outlook."
# gm = "simply meaning “good morning,” gm is a common greeting used in crypto circles"
# fren = "A friend! A friend in crypto lingo"

dic = {'ser' : "meaning \"Sir\", a common intentional misspelling used in crypto circles \"GM ser\".",
  'wagmi':"\"We're All Gonna Make It,\" a common saying in crypto and trading circles signaling camaraderie and a positive outlook.",
  'gm': "simply meaning “good morning,” gm is a common greeting used in crypto circles",
  'fren':"A friend! A friend in crypto lingo"}
print("What word do you want ot Look for ? :")
word = input()
if word == 'ser':
    print(dic['ser'])
if word == 'wagmi':
    print(dic['wagmi'])
if word == 'gm':
    print(dic['gm'])
if word == 'fren':
    print(dic['fren'])
if word not in dic:
    print("Word not found in dictionary")
