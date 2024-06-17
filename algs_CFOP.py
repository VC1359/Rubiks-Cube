# Force yellow daisy
cross = {

}

f2l = {
    "easy": {
        #basics
        "1": "U R U' R'",
        "2": "U' F' U F",
        "3": "F' U' F",
        "4": "R U R'",
        #corner and edge top
        "5": "U' R U R' U' R U2 R'",
        "6": "U F' U' F U F' U2 F",
        "7": "U' R U2 R' U' R U2 R'",
        "8": "U F' U2 F U F' U2 F",
        "9": "U F' U' F U' F' U' F",
        "10": "U' R U R' U R U R'",
        "11": "U' R U2 R' d R' U' R",
        "12": "d R' U2 R d' R U R'",
        "13": "U F' U F U' F' U' F",
        "14": "U' R U' R' U R U R'",
        "15": "F' U F U' d' F U F'",
        "16": "R U' R' U d R' U' R",
        #corner point up
        "17": "R U2 R' U' R U R'",
        "18": "F' U2 F U F' U' F",
        "19": "U R U2 R' U R U' R'",
        "20": "U' F' U2 F U' F' U F",
        "21": "U2 R U R' U R U' R'",
        "22": "U2 F' U' F U' F' U F",
        "23": "R U R' U' U' R U R' U' R U R'",
        #"24": "y' R' U' R U U R' U' R U R' U' R", #Original alg with y'
        "24": "F' U' F U2 F' U' F U F' U' F", #Transcription of the above without y'
        #corner bottom and ege top
        "25": "U' F' U F U R U' R'",
        "26": "U R U' R' U' F' U F",
        "27": "R U' R' U R U' R'",
        "28": "F' U F U' F' U F",
        "29": "F' U' F U F' U' F",
        "30": "R U R' U' R U R'",
        #corner top and edge middle
        "31": "R U' R' d R' U R",
        "32": "R U R' U' R U R' U' R U R'",
        "33": "U' R U' R' U' R U2 R'",
        "34": "U F' U F U F' U2 F",
        "35": "U' R U R' d R' U' R",
        "36": "U F' U' F d' F U F'",
        #corner bottom and edge middle
        "37": "R U' R' d R' U2 R U R' U2 R",
        "38": "R U' R' U' R U R' U' R U2 R'",
        "39": "R U' R' U R U2 R' U R U' R'",
        "40": "R U' R' d R' U' R U' R' U' R",
        "41": "R U R' U' R U' R' U d R' U' R"
    },
}

oll = {
    "2OLL": {
        "Dot": "F R U R' U' F' f R U R' U' f'",
        "l-Shape": "F R U R' U' F'",
        "L-Shape": "f R U R' U' f'",
        "Antisune": "R U2 R' U' R U' R'",
        "H": "R U R' U R U' R' U R U2 R'",
        "L": "F R' F' r U R U' r'",
        "Pi": "R U2 R2 U' R2 U' R2 U2 R",
        "Sune": "R U R' U R U2 R'",
        "T": "r U R' U' r' F R F'",
        "U": "R2 D R' U2 R D' R' U2 R'"
    },
}

pll = {
    "2PLL": {
        "Diagonal": "F R U' R' U' R U R' F' R U R' U' R' F R F'",
        "Headlights": "R U R' U' R' F R2 U' R' U' R U R' F'",
        "H": "M2 U M2 U2 M2 U M2",
        "Ua": "R U' R U R U R U' R' U' R2",
        "Ub": "R2 U R U R' U' R' U' R' U R'",
        "Z": "M' U M2 U M2 U M' U2 M2"
    },
}

def alg_extraction(piece, alg):
    if piece.ort != 'F':
        #2alg = alg.replace("")
        pass
    else: return alg