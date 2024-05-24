def citanje_najveceg_scorea():
    try:
        with open("scores.txt") as fajl:
            score = fajl.readline()
        return score
    except Exception as e:
        print(e)

def upis_scorea_u_fajl(score):
    try:
        poslednji_max_score = int(citanje_najveceg_scorea())
        if score > poslednji_max_score:
            with open("scores.txt", "w") as fajl:
                fajl.write(str(score))
    except Exception as e:
        print(e)



