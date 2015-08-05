# playingcards
A playing cards deck with physical constants instead of numbers (cvan be use for any game that requires numbers, like that guy for example https://fr.wikipedia.org/wiki/Ascenseur_%28jeu_de_cartes%29)
## what's in ./pdf/?
The pdf files of the cards
## what's in ./tex/?
The TeX file of the cards
## what's in ./dat/?
The csv file where the card informations are stored
## what's in ./src/?
the python code to parse the information from csv file in ./dat/ and generate the TeX code in ./tex/
## what's this shell file compile_cards.sh?
run the python code to parse the csv file and create the TeX code, then call pdflatex to compile the TeX code to generate pdf
