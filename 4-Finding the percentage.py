#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = str(input())

    liste = student_marks.get(query_name, "isim yok")

    toplam=0

    for i in liste:
        toplam = i + toplam

    ortalama = toplam/len(liste)

    print("{:.2f}".format(ortalama))








