from dictionary import *
from signup import *
def encrypt(string):
    string = string.lower()
    userPassword = string.translate(
        str.maketrans({"a": A, "b": B, "c": C, "d": D, "e": E, "f": F, "g": G, "h": h, "i": i, "j": J, "k": K, "l": L,
                    "m": M, "n": N, "o": o, "p": P, "q": Q, "r": R, "s": S, "t": T, "u": U, "v": V, "w": W, "x": X,
                    "y": Y, "z": Z, " ": space
                    }))
    print(userPassword)


def decrypt(string):
    userPassword = string
    userPassword = userPassword.replace(A, "a").replace(B, "b").replace(C, "c").replace(D, "d").replace(E, "e").replace(
        F, "f").replace(G, "g").replace(h, "h").replace(i, "i").replace(J, "j").replace(K, "k").replace(L, "l").replace(
        M, "m").replace(N, "n").replace(o, "o").replace(P, "p").replace(Q, "q").replace(R, "r").replace(S, "s").replace(
        T, "t").replace(U, "u").replace(V, "v").replace(W, "w").replace(X, "x").replace(Y, "y").replace(Z, "z").replace(
        space, " ")



# en = encrypt
"""
en_first_name = def(first_name)
en_last_name = def(last_name)
en_pass_word = def(pass_word)
en_email = def(email)
en_username = def(user_name)
"""