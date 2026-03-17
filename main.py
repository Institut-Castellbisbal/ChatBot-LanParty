import json
import os

def carregar_dades(ruta_fitxer):
    """
    Aquesta funció intenta obrir el fitxer JSON i carregar les dades.
    Si el fitxer no existeix o el format és incorrecte, gestiona l'error
    per evitar que el programa s'aturi bruscament.
    """
    try:
        if os.path.exists(ruta_fitxer):
            with open(ruta_fitxer, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"Error: El fitxer {ruta_fitxer} no s'ha trobat.")
            return None
    except Exception as e:
        print(f"S'ha produït un error inesperat: {e}")
        return None

def cercar_resposta(pregunta_usuari, dades):
    """
    Recorre la llista de diccionaris buscant una coincidència.
    Converteix tot a minúscules per fer la cerca més flexible (case-insensitive).
    """
    # Netegem la pregunta de l'usuari per facilitar la comparació
    pregunta_neta = pregunta_usuari.strip().lower()
    
    for item in dades:
        if item["pregunta"].lower() == pregunta_neta:
            return item["respuesta"]
    
    return "No entiendo tu duda, contacta con un organizador"

def main():
    """
    Funció principal que gestiona el flux del programa i el bucle d'interacció.
    """
    print("--- Benvingut al Suport Tècnic de la LAN Party ---")
    print("(Escriu 'salir' per tancar el xat)\n")
    
    # Carreguem les dades del fitxer JSON
    dades_faq = carregar_dades('faqs.json')
    
    # Si no s'han pogut carregar les dades, finalitzem el programa
    if dades_faq is None:
        return

    while True:
        # Demanem l'entrada a l'usuari
        entrada = input("Tu: ")
        
        # Comprovem si l'usuari vol sortir
        if entrada.lower() == 'salir':
            print("Gràcies per utilitzar el servei de suport. Bona LAN!")
            break
        
        # Busquem la resposta i la mostrem
        resposta = cercar_resposta(entrada, dades_faq)
        print(f"Bot: {resposta}\n")

if __name__ == "__main__":
    # Punt d'entrada del script
    main()
