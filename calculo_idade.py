import datetime

def get_valid_year():
    while True:
        try:
            year = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= year <= 2021:
                return year
            else:
                print("Ano inválido. Por favor, insira um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def main():
    print("Bem-vindo ao programa de cálculo de idade!")
    name = input("Digite seu nome completo: ").strip()
    birth_year = get_valid_year()
    
    current_year = 2022
    age = current_year - birth_year
    
    print(f"\nOlá, {name}! Você completou ou completará {age} anos em {current_year}.")

if __name__ == "__main__":
    main()
