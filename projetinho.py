import requests

def obter_taxa(codigo_base, codigo_alvo):
    url = f"https://api.exchangerate.host/latest?base={codigo_base}&symbols={codigo_alvo}"
    resposta = requests.get(url)
    dados = resposta.json()
    
    if "rates" in dados and codigo_alvo in dados["rates"]:
        return dados["rates"][codigo_alvo]
    else:
        return None

def converter_moeda(valor, taxa):
    return valor * taxa

def main():
    print("=== Conversor de Moedas ===")
    base = input("De qual moeda (ex: BRL): ").upper()
    alvo = input("Para qual moeda (ex: USD): ").upper()
    valor = float(input(f"Digite o valor em {base}: "))
    
    taxa = obter_taxa(base, alvo)
    if taxa:
        resultado = converter_moeda(valor, taxa)
        print(f"{valor:.2f} {base} = {resultado:.2f} {alvo}")
    else:
        print("Erro ao buscar taxa de câmbio. Verifique os códigos das moedas.")

if __name__ == "__main__":
    main()
