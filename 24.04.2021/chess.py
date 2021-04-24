# from abc import ABC, abstractmethod

# # table=[['☐'] * 8 for i in range(8)]
# # table[0][0]='♖'
# # table[0][7]='♖'
# # table[7][0]='♜'
# # table[7][7]='♜'
# # table[0][1]='♘'
# # table[0][6]='♘'
# # table[7][1]='♞'
# # table[7][6]='♞'
# # table[0][2]='♗'
# # table[0][5]='♗'
# # table[7][2]='♝'
# # table[7][5]='♝'
# # table[0][3]='♕'
# # table[7][3]='♛'
# # table[0][4]='♔'
# # table[7][4]='♚'
# # for a in range(8):
# #   print()
# #   for b in range(8):
#       # table[1][b]='♙'
#       # table[6][b]='♟'
# #       print(table[a][b], end=' ')
        
# #цвета фигур
# class Color(object):
#   EMPTY = 0
#   BLACK = 1
#   WHITE = 2

# #несуществующая фигура, чтобы белым и черным фигурам определять возможность хода
# class Empty(object):
#   color = Color.EMPTY

#   def get_moves(self, board, x, y):
#     raise Exception('Error ! ')

#   def __repr__(self):
#     return '☐'

# class ChessMan(object):
#   IMG = None

#   def __init__(self, color):
#     self.color = color

#   def __repr__(self):
#     return self.IMG[0 if self.color == Color.WHITE else 1]

# #пешка
# class Pawn(ChessMan):
#   IMG = ('♙', '♟')

#   def get_moves(self, board, x, y):
#   #   moves = []
#   #   if self.color == Color.BLACK and y < 7 and board.get_color(x, y+1) == Color.EMPTY:
#   #     moves.append([x, y+1])
#   #   return moves
#     moves = []
#     y += -1 if self.color == Color.WHITE else 1
#     if y == -1 or y == 8:
#         return moves
#     if x > 0 and board.get_color(x-1, y) == self.enemy_color():
#         moves.append([x-1, y])
#     if x < 7 and board.get_color(x+1, y) == self.enemy_color():
#         moves.append([x+1, y])
#     if board.is_empty(x, y):
#         moves.append([x, y])
#         if self.color == Color.WHITE and y == 5 and board.is_empty(x, y-1):
#             moves.append([x, y-1])
#         if self.color == Color.BLACK and y == 2 and board.is_empty(x, y+1):
#             moves.append([x, y+1])
#     return moves


# #король
# class King(ChessMan):
#   IMG = ('♛', '♕')

#   def get_moves(self, board, x, y):
#     moves = []
#     return moves



# #шахматная доска с фигурами
# class Board(object):
#   def __init__(self):
#     self.board = [[Empty()] * 8 for y in range(8)]
#     self.board[1][0] = Pawn(Color.BLACK)
#     self.board[1][1] = Pawn(Color.BLACK)
#     self.board[1][2] = Pawn(Color.BLACK)
#     self.board[1][3] = Pawn(Color.BLACK)
#     self.board[1][4] = Pawn(Color.BLACK)
#     self.board[1][5] = Pawn(Color.BLACK)
#     self.board[1][6] = Pawn(Color.BLACK)
#     self.board[1][7] = Pawn(Color.BLACK)

#     self.board[0][3] = King(Color.BLACK)
#     self.board[7][3] = King(Color.WHITE)
    
#     self.board[6][0] = Pawn(Color.WHITE)
#     self.board[6][1] = Pawn(Color.WHITE)
#     self.board[6][2] = Pawn(Color.WHITE)
#     self.board[6][3] = Pawn(Color.WHITE)
#     self.board[6][4] = Pawn(Color.WHITE)
#     self.board[6][5] = Pawn(Color.WHITE)
#     self.board[6][6] = Pawn(Color.WHITE)
#     self.board[6][7] = Pawn(Color.WHITE)

#   def get_color(self, x, y):
#     return self.board[y][x].color

#   def get_moves(self, x, y):
#     return self.board[y][x].get_moves(self, x, y)

#   def move(self, xy_from, xy_to):
#     captured = self.board[xy_to[1]][xy_to[0]]
#     self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
#     self.board[xy_from[1]][xy_from[0]] = Empty()
#     return captured

#   def __repr__(self):
#     res = ''
#     for y in range(8):
#       res += ''.join(map(str, self.board[y])) + '\n'
#     return res

# b = Board()
# print(b)
# m = b.get_moves(2, 1)
# b.move([2, 0], m[0])
# print(b)

# # table[0][7]='♖'
# # table[7][0]='♜'
# # table[7][7]='♜'
# # table[0][1]='♘'
# # table[0][6]='♘'
# # table[7][1]='♞'
# # table[7][6]='♞'
# # table[0][2]='♗'
# # table[0][5]='♗'
# # table[7][2]='♝'
# # table[7][5]='♝'
# # table[0][3]='♕'
# # table[7][3]='♛'
# # table[0][4]='♔'
# # table[7][4]='♚'

class Chess_Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board_x = []

        for x in range(8):
            board_y = []
            for y in range(8):

                board_y.append('.')

            board_x.append(board_y)

        board_x[7][4] = '♛'#White Queen
        board_x[7][3] = '♚'#White King 
        board_x[7][1] = '♞'#White Knight
        board_x[7][2] = '♝'#White Bishop
        board_x[7][0] = '♜'#White Rook
        return board_x

class WHITE_KING(Chess_Board):
  def __init__(self):
    Chess_Board.__init__(self)
    self.xi = 7
    self.yi = 3
    self.symboli = '♚'

  def move(self):
    while True:
      print ('Give a x and y coordinate for WHITE KING')
      movexi = int(input())
      moveyi = int(input()) 
      # if (abs(self.x - movex) > 1 or abs(self.y - movey) > 1 or (self.x == movex and self.y == movey)):
      #   print ('The king cannot perform that move, please choose co-ordinates again.')
      #   continue

      #   print ('White King to {} {}...'.format(movex, movey))
      #   self.board[self.x][self.y] = self.symbol
      #   break # Moved successfully

      # else:
      #   print ('Your move is invalid for this board, please choose co-ordinates again.')
      #   continue
    # You could have a more specific message about not placing the King in check.
      if self.board[movexi][moveyi] == '.':
        if abs(self.xi - movexi) < 2 and abs(self.yi - moveyi) < 2:
          self.board[self.xi][self.yi] = '.'
          self.xi = movexi
          self.yi = moveyi
          print ('White King to {} {}...'.format(movexi, moveyi))
          self.board[self.xi][self.yi] = self.symboli
          return self.board
        else:
          print ('your move is invalid, please choose coordinates again')
          continue

class WHITE_QUEEN(Chess_Board):
  def __init__(self):
    Chess_Board.__init__(self)
    self.xq = 7
    self.yq = 4
    self.symbolq = '♛'

  def move(self):
    while True:
      print ('give a x and y coordinate for WHITE QUEEN')
      movexq = int(input())
      moveyq = int(input())

      if self.board[movexq][moveyq] == '.' :
        if movexq == self.xq or moveyq == self.yq or abs(self.xq - movexq) == abs(self.yq - moveyq):
          self.board[self.xq][self.yq] = '.'
          self.xq = movexq
          self.yq = moveyq
          self.board[self.xq][self.yq] = self.symbolq

          return self.board
          break

        else:
          print ('your move is invalid, please choose coordinates again')
          continue

class WHITE_ROOK(Chess_Board):
  def __init__(self):
    Chess_Board.__init__(self)
    self.xr = 7
    self.yr = 0
    self.symbolr = '♜'

  def move(self):
    while True:
      print ('give a x and y coordinate for WHITE ROOK ')
      movexr = int(input())
      moveyr = int(input())
      if self.board[movexr][moveyr] == '.' :
        if movexr != self.xr or mover != self.y:
          self.board[self.xr][self.yr] = '.'
          self.xr = movexr
          self.yr = moveyr
          self.board[self.xr][self.yr] = self.symbolr
          return self.board
        else:
          print ('your move is invalid, please choose coordinates again')
          continue

class WHITE_BISHOP(Chess_Board):
  def __init__(self):
    Chess_Board.__init__(self)
    self.xb = 7
    self.yb = 2
    self.symbolb = '♝'

  def move(self):
    while True:
      print ('Give a x and y coordinate for WHITE BISHOP')
      movexb = int(input())
      moveyb = int(input())
      if self.board[movexb][moveyb] == '.':
        if abs(self.xb - movexb) == abs(self.yb - moveyb):
          self.board[self.xb][self.yb] = '.'
          self.xb = movexb
          self.yb = moveyb
          self.board[self.xb][self.yb] = self.symbolb
          return self.board
        else:
          print ('your move is invalid, please choose co-ordinates again')
          continue

class WHITE_KNIGHT(Chess_Board):
  def __init__(self):
    Chess_Board.__init__(self)
    self.xk = 7
    self.yk = 1
    self.symbolk = '♞'

  def move(self):
    while True:
      print ('give a x and y coordinate for WHITE KNIGHT')
      movexk = int(input())
      moveyk = int(input())

      if self.board[movexk][moveyk] == '.' :
        if abs(self.xk - movexk) ** 2 + abs(self.yk - moveyk) ** 2 == 5:
          self.board[self.xk][self.yk] = '.'
          self.xk = movexk
          self.yk = moveyk
          self.board[self.xk][self.yk] = self.symbolk
          return self.board
          
        else:
          print ('your move is invalid, please choose coordinates again')
          continue

class Engine(Chess_Board):
  def __init__(self):
    WHITE_KING.__init__(self)
    WHITE_QUEEN.__init__(self)
    WHITE_ROOK.__init__(self)
    WHITE_BISHOP.__init__(self)
    WHITE_KNIGHT.__init__(self)
    Chess_Board.__init__(self)

  def play(self):
    print('''Please write what figure you choose to move: 
      white_king, 
      white_queen, 
      white_rook, 
      white_bishop
      white_knight, 
      and if u wanna stop the game choose: close
      or if u wanna see the board again choose: show''')

    while True:
      choice = str(input())

      if choice == 'white_king':
        WHITE_KING.move(self)

      elif choice == 'white_queen':
        WHITE_QUEEN.move(self)

      elif choice == 'white_bishop':
        WHITE_BISHOP.move(self)
        
      elif choice == 'white_knight':
        WHITE_KNIGHT.move(self)

      elif choice == 'white_rook':
        WHITE_ROOK.move(self)

      elif choice == 'close':
        break

      elif choice == 'show':
        return self.board

      else:
        print ('please choose again')


  def display(self):
    for i in range (8):
      for j in range (8):
        print (self.board[i][j], end=' ')
      print()

b = Chess_Board()

c_engine = Engine()
print(c_engine.display())
c_engine.play()
print(c_engine.display())     