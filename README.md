# playingcards
A playing cards deck (currently 33 cards) with physical constants instead of numbers (from 1 to 32 + one joker (the number 0)).
Can be use for any game that requires numbers, like that guy for example https://boardgamegeek.com/boardgame/75668/whist-22
## what's in ./pdf/?
The pdf files of the cards
## what's in ./png/?
The png files of the cards
## what's in ./tex/?
The TeX file of the cards
## what's in ./dat/?
The csv file where the card data are stored (like the name, the LaTeX symbol, the value, ...)
## what's in ./src/?
The python code to parse the information from csv file in ./dat/ and generate the TeX files in ./tex/
## what's this shell file compile_cards.sh?
run the python code to parse the csv file and create the TeX code, then call pdflatex to compile the TeX code to generate pdf
