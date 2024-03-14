
import requests
pokemon = "dragonite"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
retorno = requests.get(url)
resultado = retorno.json()
poke_name = resultado["name"]
type_poke = resultado["types"]
moves_poke = resultado["moves"]""
lista_type = []
if len(type_poke) == 1:
    nome = type_poke[0]["type"]["name"]
    print(f"O tipo dele é {lista_type[0]}")
else:
    for i in range(len(type_poke)):
        nome = type_poke[i]["type"]["name"]
        lista_type.append(nome)
    print(f"O nome do pokemon é {poke_name}")
    print(f"O tipo dele é {lista_type[0]} e {lista_type[1]}")
        
#"os ataques dele são: ... .. ... ... ..."






# for i in range(len(moves_poke)):
    


# def statuspoke(pokemon):
#     pokemon = "pikachu"
#     url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
#     retorno = requests.get(url)
#     print(retorno)
#     resultado = retorno.json()
#     type_poke = resultado["types"]["name"]
#     if len(type_poke) > 0:
#         for tipo in type_poke:
#             print(f"O tipo dele é {tipo} e {tipo}")
