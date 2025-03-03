from rich import print

# fonction pour vérifier si la clé est valide 
def est_cle_valide(cle):
    return cle.isalpha() and cle.isascii() 

# fonction pour chiffrer un texte avec la clé de vigenère
def chiffrer_vigenere(texte, cle):
    texte_chiffre = "" 
    cle_index = 0 #pour suivre la position acctuelle du texte
    cle = cle.upper().replace(" ","") #convertir la clé en majuscules 

    for char in texte: #parcourir chaque caratere du texte
        
        if char.isalpha(): #verifier si le caractere est une lettre
            decalage = ord(cle[cle_index % len(cle)]) - ord('A')
            
            if char.isupper(): 
                texte_chiffre += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
            else:
                texte_chiffre += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
            
            cle_index += 1 
        else:
            texte_chiffre += char #conserver les caratéres non aplhabétiques
    
    return texte_chiffre

#fonction pour déchiffrer un texte avec la clé de Vigenère
def dechiffrer_vigenere(texte_chiffre, cle):
    texte_dechiffre = ""
    cle_index = 0
    cle = cle.upper().replace(" ", "")
    
    for char in texte_chiffre:
        if char.isalpha():
            decalage = ord(cle[cle_index % len(cle)]) - ord('A')
            if char.isupper():
                texte_dechiffre += chr((ord(char) - ord('A') - decalage) % 26 + ord('A'))
            else:
                texte_dechiffre += chr((ord(char) - ord('a') - decalage) % 26 + ord('a'))
            cle_index += 1
        else:
            texte_dechiffre += char
    
    return texte_dechiffre

#fonction pour afficher 
def afficher_menu():
    print("[bold cyan]---Bienvenue, agent Codebuster---[/bold cyan]")
    print("1. Chiffrer un texte")
    print("2. Déchiffrer un texte")
    print("3. Quitter")
    print("[bold cyan]--------------------------------------[/bold cyan]")

#fonction principale du programme
def main():
    essais_restants = 3
    
    while essais_restants > 0: 
        afficher_menu()
        choix = input("Entrez votre choix: ")
        
        if choix == '1': #chiffrer un texte
            texte = input("Entrez le texte à chiffrer : ")
            cle = input("Entrez la clé (uniquement des lettres) : ")
            
            if est_cle_valide(cle): #verifier si la cle est valide
                texte_chiffre = chiffrer_vigenere(texte, cle)
                print(f"\n [bold green]✅ Texte chiffré :[/bold green] [yellow]{texte_chiffre}[yellow]")
            else:
                print("\n❌[bold red] ERREUR : La clé doit contenir uniquement des lettres.[/bold red]")
                essais_restants -= 1
                if essais_restants == 0:
                    print("\n[bold red]⚠️ Nombre maximum d'essais atteint. Le programme se termine.[/bold red]")
                    break
        
        elif choix == '2':
            texte_chiffre = input("Entrez le texte à déchiffrer : ")
            cle = input("Entrez la clé (uniquement des lettres) : ")
            
            if est_cle_valide(cle):
                texte_dechiffre = dechiffrer_vigenere(texte_chiffre, cle)
                print(f"\n✅[bold green] Texte déchiffré : [/bold green] [yellow]{texte_dechiffre}[/yellow]")
            else:
                print("\n❌[bold red] ERREUR : La clé doit contenir uniquement des lettres. [/bold red]")
                essais_restants -= 1
                if essais_restants == 0:
                    print("\n⚠️ [bold red] Nombre maximum d'essais atteint. Le programme se termine.[/bold red]")
                    break
        
        elif choix == '3':
            print("\n👋[bold cyan] Au revoir, agent Codebuster ![/bold cyan]")
            break
        
        else: #choix invalide
            print("\n❌[bold red] Choix invalide. Réessayez.[/bold red]")
            essais_restants -= 1
            
            if essais_restants == 0:
                print("\n⚠️ Nombre maximum d'essais atteint. Le programme se termine.")
                break

#debut du programme
if __name__ == "__main__":
    main()