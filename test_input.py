'''
# add this:
from test_input import input
'''
auto_input = False

input_lista = [
    "MGNG",
    "GMLMKKNMMNNGGM",
    "LGLA",
    "MNLNLNGG",
    "NGMNLLLNLKNN",
    "KLKLLNMG",
    "LLMKMMGMNMNGMNM",
    "GNMLNKLK",
    "K",
    "LNKKLKG",
    "MGMGLLGMMM",
    "KKKMK",
    "NLLMGLLNM",
    "GMLLKMKGGKML",
    "NGKNNKNG",
    "LLNKMNLLNK",
    "NNMKGNGGLLGMMML",
    "KMNNMGMGLLMMLKNGNGML",
    "LMLNNMLGMN",
    "LLKMKKNMMLNKKMGMNKNGLLM",
    "NLKLNLGGGMLNKMGNLG",
    "LLGNNKLLLNKGL",
    "NLMNMMKKLKNK",
    "GKNLGLNLLNNKLK",
    "LKMKKLNKMLMMNLNGMN",
    "KGGNM",
    "MLGLKMNKMLKMG",
    "MKKNGKN",
]

def get_val():
    for rend in input_lista:
        yield rend

gen = get_val()

def input(szoveg):
    val = next(gen)
    print(szoveg, val, sep="")
    return val
