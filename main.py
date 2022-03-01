import discord
from discord.ext import commands
import random
from keep_alive import keep_alive

player1 = ""
player2 = ""
turn = ""
gameover = True
board = []
count = 0

def printBoard(board,ctx):
    line = ""
    for i in range(len(board)):
      line = line + board[i] + '   '
      if i%3 == 2:
        line += '\n\n'
    return line
  
client = commands.Bot(command_prefix="!")

winning_conditions = [[0,1,2],
                      [3,4,5],
                      [6,7,8],
                      [0,3,6],
                      [1,4,7],
                      [2,5,8],
                      [0,4,8],
                      [2,4,6]]

def check_winner(count,board):
  if count>=9:
    return 'Draw'
  global winning_conditions
  for cond in winning_conditions:
    if board[cond[0]]== ':regional_indicator_x:' and board[cond[1]]== ':regional_indicator_x:' and board[cond[2]]== ':regional_indicator_x:':
      return 'X'
    elif board[cond[0]]== ":o2:" and board[cond[1]]== ":o2:" and board[cond[2]]== ":o2:":
      return 'O'
  return 'None'

@client.event
async def on_ready():
  print("The bot is ready!")

@client.command()
async def TicTacToe(ctx, p1:discord.Member,p2:discord.Member):
  global player1
  global player2
  global turn
  global gameover
  global count

  if gameover:
    global board
    board = [':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:']
    
    turn = ''
    gameover = False
    count = 0

    player1 = p1
    player2 = p2

    line = printBoard(board,ctx)
    await ctx.send(line)

    player = random.choice([p1,p2])
    await ctx.send(f"Its {player.mention} turn!")
    turn = player


@client.command()
async def p(ctx,num:int):
  global player1
  global player2
  global turn
  global gameover
  global count
  global board
  global win_conditions

  if not gameover:
    if ctx.author != turn:
      await ctx.send(f"Please wait for your turn {ctx.author.mention}!")
      return
    else:
      if turn == player1:
        mark = ':regional_indicator_x:'
      elif turn == player2:
        mark = ":o2:"
      
      if num>=10 and num<=0:
        await ctx.send(f"Please enter a number between 1 to 9!, {ctx.author.mention}")

      elif board[num-1] != ':white_large_square:':
        await ctx.send(f"That box has already been filled. Please enter another number!, {ctx.author.mention}")
      
      else:
        board[num-1] = mark
        count += 1
        line = printBoard(board,ctx)
        await ctx.send(line)
        if check_winner(count,board) == 'X':
          await ctx.send(f"{player1.mention} wins the game!")
          gameover = True
        elif check_winner(count,board) == 'O':
          await ctx.send(f"{player1.mention} wins the game!")
          gameover = True
        elif check_winner(count,board) == "Draw":
          await ctx.send("Its a draw!")
          gameover = True
        elif check_winner(count,board) == "None":
          if turn == player1:
            turn = player2
          elif turn == player2:
            turn = player1
          await ctx.send(f"Its {turn.mention} 's turn!")
  else:
    await ctx.send("There is no game going on right now!")


keep_alive()
client.run("OTMyMTQxMjU4NjU3Mzc4MzA0.YeOqMg.VUkp3O4VRsSWFhHOVbVskwQH75Y")