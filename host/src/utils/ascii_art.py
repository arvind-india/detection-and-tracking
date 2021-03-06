# ******************************
# * Print sentence as ASCII art
# * Style: Graceful
#
# ******************************

def printAsciiArt(sentence):
    art = getArt(sentence)
    for line in art:
        print line

def getArt(word):
    word = word.upper()
    art = ['','','','']
    for letter in word:
        l = getLetter(letter)
        art = addToWord(art, l)
    return art

def addToWord(word, letter):
    for i in range(4):
        word[i] += letter[i]
    return word

def getLetter(letter):
    alphabet = {
        'A' : [
            "  __  ",
            " / _\ ",
            "/    \\",
            "\_/\_/"
        ],
        'B' : [
            " ____ ",
            "(  _ \\",
            " ) _ (",
            "(____/"
        ],
        'C' : [
            "  ___ ",
            " / __)",
            "( (__ ",
            " \___)"
        ],
        'D' : [
            " ____ ",
            "(    \\",
            " ) D (",
            "(____/"
        ],
        'E' : [
            " ____ ",
            "(  __)",
            " ) _) ",
            "(____)"
        ],
        'F' : [
            " ____ ",
            "(  __)",
            " ) _) ",
            "(__)  "
        ],
        'G' : [
            "  ___ ",
            " / __)",
            "( (_ \\",
            " \___/"
        ],
        'H' : [
            " _  _ ",
            "/ )( \\",
            ") __ (",
            "\_)(_/"
        ],
        'I' : [
            "  __  ",
            " (  ) ",
            "  )(  ",
            " (__) "
        ],
        'J' : [
            "   __ ",
            " _(  )",
            "/ \) \\",
            "\____/"
        ],
        'K' : [
            " __ _ ",
            "(  / )",
            " )  ( ",
            "(__\_)"
        ],
        'L' : [
            " __   ",
            "(  )  ",
            "/ (_/\\",
            "\____/"
        ],
        'M' : [
            " _  _ ",
            "( \/ )",
            "/ \/ \\",
            "\_)(_/"
        ],
        'N' : [
            " __ _ ",
            "(  ( \\",
            "/    /",
            "\_)__)"
        ],
        'O' : [
            "  __  ",
            " /  \ ",
            "(  O )",
            " \__/ "
        ],
        'P' : [
            " ____ ",
            "(  _ \\",
            " ) __/",
            "(__)  "
        ],
        'Q' : [
            "  __  ",
            " /  \ ",
            "(  O )",
            " \__\)"
        ],
        'R' : [
            " ____ ",
            "(  _ \\",
            " )   /",
            "(__\_)"
        ],
        'S' : [
            " ____ ",
            "/ ___)",
            "\___ \\",
            "(____/"
        ],
        'T' : [
            " ____ ",
            "(_  _)",
            "  )(  ",
            " (__) "
        ],
        'U' : [
            " _  _ ",
            "/ )( \\",
            ") \/ (",
            "\____/"
        ],
        'V' : [
            " _  _ ",
            "/ )( \\",
            "\ \/ /",
            " \__/ "
        ],
        'W' : [
            " _  _ ",
            "/ )( \\",
            "\ /\ /",
            "(_/\_)"
        ],
        'X' : [
            " _  _ ",
            "( \/ )",
            " )  ( ",
            "(_/\_)"
        ],
        'Y' : [
            " _  _ ",
            "( \/ )",
            " )  / ",
            "(__/  "
        ],
        'Z' : [
            " ____ ",
            "(__  )",
            " / _/ ",
            "(____)"
        ],
        ' ' : [
            "    ",
            "    ",
            "    ",
            "    "
        ],
        ':' : [
            " _ ",
            "(_)",
            " _ ",
            "(_)"
        ]
    }
    return alphabet[letter]    
