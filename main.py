meme_dict = { 
    "CRINGE": "Algo vergonhoso ou constrangedor", 
    "STALKEAR": "Investigar a vida de alguém online", 
    "VDD": "Abreviação da palavra verdade", 
    "SS": "Abreviação da palavra sim", 
    "VC": "Abreviação da palavra você" 
}

word = input("Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Essa palavra ainda não está no dicionário.")
