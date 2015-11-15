import chess
import os
import sqlite3
import db_tools
import game_tools

def parse_board(board, winner):
    start_board_str = str(chess.Board())
    conn = db_tools.get_connection()
    c = conn.cursor()
    while(str(board) != start_board_str):
        move = board.pop()
        is_winner = board.turn == winner
        win_incr = 1 if is_winner else 0
        total_incr = 1

        '''
        There is no way to insert or on duplicate key update in sqlite3, so
        instead it is cut up into two commands
        '''

        ''' insert new row if it doesn't exist '''
        c.execute("INSERT OR IGNORE INTO Moves (Board, Move, Wins, TotalSeen) VALUES (?, ?, ?, ?)", (str(board), str(move), int(0), int(0)))

        ''' update existing row to increment Wins and TotalSeen when needed '''
        c.execute("UPDATE Moves SET Wins=Wins+?, TotalSeen=TotalSeen+? WHERE Board=? AND Move=?", (win_incr, total_incr, str(board), str(move)))

        conn.commit()
    conn.close()


if __name__=='__main__':
    ''' test code for simple board '''
    board = chess.Board()
    board.push(list(board.legal_moves)[0])
    board.push(list(board.legal_moves)[0])
    parse_board(board, game_tools.BLACK)
