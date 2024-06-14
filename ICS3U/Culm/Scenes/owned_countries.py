"""
Robert
ICS3UO
owned_countries.py
June 14

a central hub for claiming countries
"""

#Charachters Mapping to Countries List
#Europe = Peter
#North America = Alexander
#South America = Pericies 
#Africa = Saladin
#Antartica = Seondak
#India = Qin
#Australia = Trajan 

# Owned Countries in this order: AFR, ANT, AUS, EUR, IND, NOA, SOA
def claim_country(leader, won = True):
    characters = ['Saladin', "Seondak", "Trajan", "Peter", "Qin", "Alexander", "Pericies"]
    base.owned_countries[characters.index(leader)] = won

    #remove the country from the alive leaders list
    base.alive_emperors.remove(leader)
