#####################
### Stringi (str) ###
#####################
# Oficjalna dokumentacja:
#https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str


# s.upper() 	- zmienia wszystkie litery na wielkie
assert "Ala ma kota".upper() == "ALA MA KOTA"

# s.lower()	- zmienia wszystkie litery na małe
assert 'AlA mA KOTa'.lower() == 'ala ma kota'

# s.replace(old, new) - zastępuje każde wystąpienie napisu old napisem new
s = 'Janina grzybiarka'
assert s.replace('Janina', 'Helenka') == 'Helenka grzybiarka'

# s.strip() 	- usuwa początkowe i końcowe białe znaki (spacje itp)
s = '   ala ma kota    '
assert s.strip() == 'ala ma kota'

# s.split()	- dzieli napis na poszczególne słowa, wynikiem jest lista słów
s = 'ala ma kota'
assert s.split() == ['ala', 'ma', 'kota']

# s.splitlines()  - dzieli wielo-linijkowy napis na linijki, wynikiem jest lista linijek
s = """Linia 1
Linia 2
Ostatnia linia."""
assert s.splitlines() == ["Linia 1", "Linia 2", "Ostatnia linia."]

# s.join(lista_slow)	- scala napisy z listy lista_slow w jeden napis, łącznikiem jest s
assert " - ".join(["Warszawa", "Monachium", "Nowy Jork"]) == "Warszawa - Monachium - Nowy Jork"

# s.count(sub) 	- zlicza wystąpienie napisu sub w napisie s
s = 'we all live in a yellow submarine, yellow submarine, yellow submarine'
assert s.count('sub') == 3    # to nie musi być wyraz "sub" :D

# s.index(sub)	- podaje pozycję, na której zaczyna się napis sub w napisie s (jeśli nie znajdzie zwraca błąd)
assert s.index('sub') == 24

# s.find(sub)		- jak index tylko jeśli nie znajdzie, to zwraca -1
assert s.find('bus') == -1

# s.find(sub, start, end) - find z podaniem opcjonalnych argumentów, wyszukuje w s[start:end]
assert s.find('sub',25) == 42

# s.startswith(sub) - sprawdza, czy s zaczyna się od napisu sub
assert s.startswith("all") == False

# s.isdigit() 	- sprawdza czy wszystkie znaki są cyframi
s = "1,2,3 baba jaga Patrzy!"
s2 = "123"
assert s.isdigit() == False
assert s2.isdigit() == True

# s.islower() 	- sprawdza czy wszystkie litery są małe
assert s.islower() == False

# s.isupper() 	- sprawdza czy wszystkie litery są duże
s = "HALO ZIEMIA"
assert s.isupper() == True

# sub in s        - sprwadza czy napis s zawiera napis sub
s3 = 'byc jak kot'
assert 'byc' in s3  #tu nie dawać == True/False

# len(s)        - zwraca ilość liter
assert len("Skok") == 4

# s[index]      - zwraca literę o podanym indeksie
s = 'ala ma kota'
assert s[2] == 'a'

# s[indeksStart:indeksStop]
assert s[2:5] == 'a m'

# s[indeksStart::krok]
assert s[2:10:2] == 'am o'

# s[:indeksStop]
assert s[:5] == 'ala m'


####################
### Listy (list) ###
####################
# Oficjalna dokumentacja:
# https://docs.python.org/3.7/library/stdtypes.html#sequence-types-list-tuple-range


# list(s) 	- konwertuje sekwencję s na listę
assert list((1,2,3)) == [1, 2, 3]

# l.append(x) 	- dodaje nowy element x na końcu l, nic nie zwraca!
l = [1]
l.append(2)
assert l == [1, 2]

# l.extend(t) 	- dodaje nową listę t na końcu l, nic nie zwraca!
l = [1,2,3]
t = [4,5,6]
l.extend(t)
assert l == [1,2,3,4,5,6]

# l.count(x) 	- zlicza ilość wystąpień x w l
l = [1, 2 , 1 ,23, 1, 23, 1, 4, 1]
assert l.count(1) == 5

# l.index(x) 	- zwraca najmniejszy indeks i, gdzie l[i] == x
assert l.index(1) == 0

# l.pop(i) 	- zwraca element o indeksie i jednocześnie usuwając go z listy
l = [1, 2, 3, 4, 5, 6]
l.pop(0)
assert l == [2, 3, 4 ,5 ,6]

# l.remove(x) 	- usuwa z listy l pierwsze wystąpienie elementu x (jeśli nie znajdzie zwraca błąd), nic nie zwraca!
l = [1, 'pow!', 'abs', [1,2,3], 10.4]
l.remove(1)
assert l == ['pow!', 'abs', [1,2,3], 10.4]

# l.copy()       - tworzy kopię - zwraca nową listę. To samo co l[:]. Trudno napisać na to ciekawy test :)
assert [1, 2, 3].copy() == [1, 2, 3]

# l.reverse() 	- odwraca kolejność elementów l "w miejscu" (czyli modyfikuje listę), nic nie zwraca!
l = [2, 1, 3, 0]
l.reverse()
assert l == [0, 3, 1, 2]

# l.sort() 	- sortuje elementy l "w miejscu" (czyli modyfikuje listę) - elementy muszą dać się porównywać (np. int i float), nic nie zwraca!
l = [232, 1, 4124, 60, 104.4, 123]
l.sort()
assert l == [1, 60, 104.4, 123, 232, 4124]

# del l[i]   - usuwa element o indeksie i z listy, nic nie zwraca!
l = [1, 2, 3]
del l[1]
assert l == [1, 3]

# x in l     - sprawdza czy x jest elementem listy
l =[1, 2, 4, 5, 124, 125]
assert 1 in l

# len(l)        - zwraca ilość elementów
assert len(l) == 6



print("Wszystko poszło poprawnie!")