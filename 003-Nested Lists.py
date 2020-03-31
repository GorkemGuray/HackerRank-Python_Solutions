# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    liste_1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inner_list = [name,score]
        liste_1.append(inner_list)

    liste_1.sort(key = lambda x : x[1])

    en_kucuk_sayi_adedi = 1 #aynı zamanda en küçük 2. sayının başlangıç indexi
    en_kucuk_2_sayi_adedi = 1

    for z in range ((len(liste_1)-1)):
        if(liste_1[z][1]==liste_1[z+1][1]):
            en_kucuk_sayi_adedi = en_kucuk_sayi_adedi+1
        else:
            break
  

    for j in range(en_kucuk_sayi_adedi, len(liste_1)-1):
                 
        if (liste_1[j][1] == liste_1[j+1][1]):
            en_kucuk_2_sayi_adedi = en_kucuk_2_sayi_adedi+1
        else:
            break

    
    e1 = en_kucuk_sayi_adedi
    e2 = en_kucuk_sayi_adedi + en_kucuk_2_sayi_adedi

    liste_2  = liste_1 [e1:e2]

    liste_2.sort(key = lambda x:x[0])

    for t in liste_2:
        print(t[0])