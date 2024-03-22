"""
Nom du fichier: bot.py
Auteur: Étienne-Théodore PRIN
Date: 2024-02-02

Description:
Ce module définie la classe bot qui a pour but de choisir l'action à effectuer en fonction de l'état de la partie clash royal.

Classe:
    - bot : classe qui a pour but de choisir l'action à effectuer en fonction de l'état de la partie clash royal.

Dépendances:
    - math
    - time
    - matrice_def (définition de matrice constante et de dictionnaire utilisé pour effectuer les choix )
"""

from use_fonction.configuration.matrice_def import matrice_choix_def_response,dict_trad,elixir_price,dictionnaire_translation,card_dictionnary
import time
import math
import random

class bot():
    """
    classe qui a pour but de choisir l'action à effectuer en fonction de l'état de la partie clash royal.

    Méthodes:
        public:
        get_action(state) : renvoie l'action préconisé par le bot
            sous la forme [] si aucune action est prise ou
            [index_de_la_carte_à_poser(int),position_ou_placer([x(int),y(int)])]
        private:

    """
    def __init__(self):
        """
        Créer un objet qui a pour but de choisir l'action à effectuer en fonction de l'état de la partie clash royal.

        Args:
            None

        Returns:
            None
        """

    def get_action(self, state):
        """
        Renvoie l'action préconisé par le bot

        Args:
            state : l'état du jeu à l'instant t

        Returns:
            action : sous la forme [] si aucune action est prise ou
                [index_de_la_carte_à_poser(int),position_ou_placer([x(int),y(int)])] si une carte doit être joué
        """
        action = 0
        if state[0]:
            card = [] 
            for i in range(4):
                rank = 6 + i
                if state[rank][2]=="geant_vignette.jpg":
                    card += [["tank", 5,"geant_vignette.jpg"]]
                elif state[rank][2]=="gobelin_lances.jpg":
                    card += [["distance", 2,"gobelin_lances_vignette.jpg"]]
                elif state[rank][2]=="gobelin_lances_vignette.jpg":
                    card += [["distance", 2,"archere_vignette.jpg"]]
                elif state[rank][2]=="chevalier_vignette.jpg":
                    card += [["tank", 3,"chevalier_vignette.jpg"]]
                elif state[rank][2]=="gobelin_vignette.jpg":
                    card += [["cac", 2,"gobelin_vignette.jpg"]]
                elif state[rank][2]=="gargouilles_vignette.jpg":
                    card += [["distance", 3,"gargouilles_vignette.jpg"]]
                elif state[rank][2]=="mousquetaire_vignette.jpg":
                    card += [["distance", 4,"mousquetaire_vignette.jpg"]]
                elif state[rank][2]=="PK_vignette.jpg":
                    card += [["cac", 4,"PK_vignette.jpg"]]
                else :
                    card +=[["?",0,"?"]]

            
            weight = 1
            x_range = [44, 412]
            y_range = [255, 609]
            y_min = 0
            x_moy = 0

            if len(state) >= 11: 
                x_moy = 0
                y_min = 0
                for unit in state[10:]:
                    y_unit = unit[1][1]
                    if y_unit > y_min:
                        y_min = y_unit

                    x_unit = unit[1][0]
                    x_moy += x_unit * weight
                x_moy = x_moy/len(state)
                if x_moy <= 220:
                    x_range = [44, 100]
                else:
                    x_range = [350, 412]        
            
            if state[3][2] == "alive tower" and state[2][2] == "alive tower":

                if state[4][2] == "alive tower" and state[5][2] == "alive tower":  
                    if y_min < 363:
                        y_min = 363         
                    y_range = [y_min, 609]
                if state[4][2] == "destroyed tower" and state[5][2] == "alive tower": 
                    if y_min < 500:
                        y_min = 500           
                    y_range = [y_min, 609]
                    x_range = [44, 100]
                if state[4][2] == "alive tower" and state[5][2] == "destroyed tower":    
                    if y_min < 500:
                        y_min = 500         
                    y_range = [y_min, 609]
                    x_range = [350, 412] 
                if state[4][2] == "destroyed tower" and state[5][2] == "destroyed tower":   
                    if y_min < 500:
                        y_min = 500          
                    y_range = [y_min, 609]

            elif state[3][2] == "destroyed tower" and state[2][2] == "alive tower":
                
                if state[4][2] == "alive tower" and state[5][2] == "alive tower":  
                    if y_min < 252:
                        y_min = 252         
                    y_range = [y_min, 609]
                if state[4][2] == "destroyed tower" and state[5][2] == "alive tower": 
                    if y_min < 500:
                        y_min = 500           
                    y_range = [y_min, 609]
                    x_range = [44, 100]
                    """ Stratégie offensive
                    if y_min < 252:
                        y_min = 252           
                    y_range = [y_min, 609]
                    x_range = [44, 190]
                    """
                if state[4][2] == "alive tower" and state[5][2] == "destroyed tower":    
                    if y_min < 500:
                        y_min = 500         
                    y_range = [y_min, 609]
                    x_range = [350, 412] 
                    """ Stratégie offensive
                    if y_min < 252:
                        y_min = 252           
                    y_range = [y_min, 609]
                    x_range = [44, 190]
                    """
                if state[4][2] == "destroyed tower" and state[5][2] == "destroyed tower":   
                    if y_min < 500:
                        y_min = 500          
                    y_range = [y_min, 609]

            elif state[3][2] == "alive tower" and state[2][2] == "destroyed tower":    
                
                if state[4][2] == "alive tower" and state[5][2] == "alive tower":  
                    if y_min < 252:
                        y_min = 252         
                    y_range = [y_min, 609]
                if state[4][2] == "destroyed tower" and state[5][2] == "alive tower": 
                    if y_min < 500:
                        y_min = 500           
                    y_range = [y_min, 609]
                    x_range = [44, 100]
                    """ Stratégie offensive
                    if y_min < 252:
                        y_min = 252           
                    y_range = [y_min, 609]
                    x_range = [250, 412] 
                    """
                if state[4][2] == "alive tower" and state[5][2] == "destroyed tower":    
                    if y_min < 500:
                        y_min = 500         
                    y_range = [y_min, 609]
                    x_range = [350, 412] 
                    """ Stratégie offensive
                    if y_min < 252:
                        y_min = 252           
                    y_range = [y_min, 609]
                    x_range = [250, 412] 
                    """
                if state[4][2] == "destroyed tower" and state[5][2] == "destroyed tower":   
                    if y_min < 500:
                        y_min = 500          
                    y_range = [y_min, 609]
            elif state[3][2] == "destroyed tower" and state[2][2] == "destroyed tower":
                
                if state[4][2] == "alive tower" and state[5][2] == "alive tower":  
                    if y_min < 252:
                        y_min = 252         
                    y_range = [y_min, 609]
                if state[4][2] == "destroyed tower" and state[5][2] == "alive tower": 
                    if y_min < 500:
                        y_min = 500           
                    y_range = [y_min, 609]
                    x_range = [44, 100]
                    """ Stratégie offensive
                    if y_min < 252:
                        y_min = 252           
                    y_range = [y_min, 609]
                    x_range = [44, 190]
                    """
                if state[4][2] == "alive tower" and state[5][2] == "destroyed tower":    
                    if y_min < 500:
                        y_min = 500         
                    y_range = [y_min, 609]
                    x_range = [350, 412] 
                    """ Stratégie offensive
                    if y_min < 252:
                        y_min = 252           
                    y_range = [y_min, 609]
                    x_range = [44, 190]
                    """
                if state[4][2] == "destroyed tower" and state[5][2] == "destroyed tower":   
                    if y_min < 500:
                        y_min = 500          
                    y_range = [y_min, 609]
                
            x = random.randint(x_range[0], x_range[1])
            y = random.randint(y_range[0], y_range[1])

            for type in ["distance", "tank", "cac"]:
                index = 0
                while index <= 3:
                    if card[index][0] == type:
                        if card [index][2] == "geant_vignette.jpg":
                            y = 400
                        elif type == "distance":
                            y = 500
                        return [index, [x, y]]
                    index += 1

            x = random.randint(x_range[0], x_range[1])
            y = random.randint(y_range[0], y_range[1])
            elixir = state[1][2] 
            if elixir >= 8:
                return [random.randint(0, 3), [x, y]]
            
            else:
                return []
            
        return []
