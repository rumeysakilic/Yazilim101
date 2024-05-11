from IPython.core.display_functions import display
from IPython.display import clear_output
import random

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] # Oyunumuz icin bos bir board olusturalim

# kullaniciya nereye isaret koyabilecegini anlamak icin fonsiyon
def display_position_board():

  print("Lutfen marker'inizi yerlstireceginiz pozisyonu secin.. ")

  print('  |   | ')
  print('1'+' | '+'2'+' | '+'3')
  print('  |   | ')
  print("----------")
  print('  |   | ')
  print('4'+' | '+'5'+' | '+'6')
  print('  |   | ')
  print("----------")
  print('  |   | ')
  print('7'+' | '+'8'+' | '+'9')
  print('  |   | ')

display_position_board() # fonksiyon cagrisi

# kullanıcının oyun tahtasındaki bir pozisyon seçmesini sağlamak icin fonksiyon

def position_choice():

  choice = '' # en basta secimimiz bos karakter dizisi

  while choice not in range(1,10): #1, 2, 3, ...., 9
    choice = int(input("Lutfen marker'inizi yerlestireceginiz pozisyonu secin(1-9): "))

    if choice not in range(1,10):
      clear_output() # ekran temizlenir, kullanicidan yeni sayi girmesi istenir.


  return choice

def player_input():
    marker = '' #kullanıcının seçeceği işareti tutmak için boş bir dize olarak başlatılır.
    player1 = '' # player1 ve computer değişkenleri, kullanıcının seçtiği işareti ve bilgisayarın kalan işaretini tutmak için boş bir dize olarak başlatılır.
    computer = ''
    while not (marker == 'X' or marker == 'O'): # marker X veya O olmadığı sürece kullanıcıya işaret seçmesi için bir input isteği yapılır.

        marker = input("Lutfen bir marker seciniz 'x' or 'o': ").upper() # Girilen değer büyük harfe dönüştürülür (upper() kullanılarak).

        if (marker != 'X') or (marker != 'O'): # Eğer girilen işaret X veya O değilse,
            clear_output() # ekran temizlenir (clear_output()) ve kullanıcıya tekrar işaret seçmesi istenir.

        if marker == 'X': # Eğer kullanıcı X seçerse, kullanıcıya seçtiği işaret ve bilgisayarın kalan işareti söylenir (print kullanılarak) ve player1 ve computer değişkenleri güncellenir.
            print(f"Siz --> '{marker}' '")
            print("Computer --> O")
            player1,computer = 'X','O'

        elif marker == 'O': # Eğer kullanıcı O seçerse, yine aynı işlemler yapılır.
            print(f"Siz --> '{marker}' '")
            print("Computer --> X ")
            player1,computer = 'O','X'
    return player1,computer # Son olarak, player1 ve computer değişkenleri tuple olarak döndürülür.



# belirli bir pozisyonda (position) oyun tahtasının (board) boş olup olmadığını kontrol eden fonksiyon. position ve board olmak üzere iki parametre alır.

def empty_space(position, board):
  return board[position] == ' ' #  belirli pozisyon bos ise True, dolu ise False dondurur.


# oyun tahtasının (board) dolu olup olmadığını kontrol eden fonksiyon

def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False  # dolu olup olmadigini kontrol ettigi icin False dondurur

    return True  # eger butun pozisyonlar dolu ise, True doner.

# belirli bir pozisyona (position) belirli bir işaret (marker) yerleştirmek için kullanilan fonksiyon

def placing_input(board, position, marker):

  board[position] = marker

print(board)

placing_input(board, 1, 'X')
print(board)

placing_input(board, 3, '0')
print(board)


# bir oyuncunun (mark) oyun tahtasında (board) kazanıp kazanmadığını kontrol eden fonksiyon.
# Kazanma durumu, aynı işaretin üçlüsünün yan yana, alt alta veya çapraz olarak tahtada olmasıyla gerçekleşir.
# Eğer kazanma koşulu sağlanıyorsa, True değeri döndürülür; aksi halde False döndürülür.

def win_check(board, mark):

  #kazanma kosullari: bunlardan biri gerceklesirse, yani True donerse, kazanirim.

  return ((board[7] == mark and board[8] == mark and board[9] == mark) or # yan yana (en alt)
    (board[4] == mark and board[5] == mark and board[6] == mark) or # yan yana (orta)
    (board[1] == mark and board[2] == mark and board[3] == mark) or # yan yana (en ust)
    (board[7] == mark and board[4] == mark and board[1] == mark) or # ust uste (sol)
    (board[8] == mark and board[5] == mark and board[2] == mark) or # ust uste (orta)
    (board[9] == mark and board[6] == mark and board[3] == mark) or # ust uste (sag)
    (board[7] == mark and board[5] == mark and board[3] == mark) or # çapraz
    (board[9] == mark and board[5] == mark and board[1] == mark)) # çapraz

# bilgisayarın rastgele bir sayı üretmesini sağlayan fonksiyon (marker'ini board'un hangi pozisyonuna yerlestirecegini anlamak icin)

def computer():
  # bilgisayarin hangi pozisyona mark atacagini belirtmek icin random sayi dondurur.

  return random.randint(1,9) # random kutuhanesindeki, randint fonksiyonunu 1 ve 9 parametresiyle cagirir, yani integer olan 1 ve 9 sayilari arasindan (1-9 dahil) rastgele sayi uretir

#  oyunda kimin başlayacağını rastgele seçen fonksiyon.

def whose_turn():

  r = random.randint(1,2)

  if r == 1:
    return "player1"
  else:
    return 'computer'

turn = whose_turn()
print(turn)


display_position_board()

turn = whose_turn() # kimin baslayacagi belli olsun

print("Kimin sirasi ???")
print(turn)

print("XOX oyunumuza hosgeldiniz !!!")

play = True

#while play:  #play False olana kadar oyun devam etsin

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Oyun başladığında, boş bir tahta oluşturulur

player1_marker, computer_marker = player_input() # oyuncuların seçeceği işaretler (player1_marker ve computer_marker) belirlenir

display_position_board()

turn = whose_turn() # kimin baslayacagi belli olsun
print(turn)

game_on = True  #kullancidan marker degeri alindiktan sonra oyun baslar


while game_on: # game_on False olana kadar oyun devam eder

  if turn == "player1":
    position = position_choice()

    # kullanicinin sectigi pozisyonun bos olup olmadigini kontrol edelim
    if empty_space(position,board): #true donerse, o pozisyon board'da bos demek
      placing_input(board, position, player1_marker)
      display(board)

      if win_check(board, player1_marker): # her adimda kazanma durumu kontrol edilir
        print("Tebrikler kazandiniz !")
        break


      if full_board_check(board): # eger bord'da bos alan kalmadiysa ve o zamana kadar kazanma durumu olmadiysa berabere kalindi demek
        print('Oyun beraber kaldi ')
        break



      turn = 'computer' # sira bilgisayarda


  else:

    position = computer()

    if empty_space(position, board):

      placing_input(board, position, computer_marker)
      display(board)

      if win_check(board, computer_marker):
        print("Kaybettiniz, bilgisayar kazandi :(")
        break

      if full_board_check(board):
        print("Oyun berabere kaldi ")
        break

      turn = "player1"



print("Oynadiginiz icin tesekkurler .. ")