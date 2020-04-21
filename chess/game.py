import pickle 
from random import randint

import chess
import chess.polyglot
from board import evaluate_board

class AlphaBetaPruning:
    def __init__(self, board, player_color):
        self.branches_minimax = 3
        self.board = board
        self.abp_color = not player_color
        self.first_move = []

        with chess.polyglot.open_reader("performance.bin") as reader:
            for entry in reader.find_all(board):
                self.first_move = [str(entry.move) for entry in reader.find_all(board)]

    def aplha_beta_pruning_steps(self):
        step_taken = None
        self.total_score_player = -1e8 if self.abp_color else 1e8
        
        if self.first_move:
            step_taken = chess.Move.from_uci(self.first_move[randint(0, len(self.first_move) // 2)])
        else:
            for move in self.board.legal_moves:
                self.board.push(move)
                provincial_score = self.alphabeta_minimax(self.branches_minimax - 1, not self.abp_color, -1e8, 1e8)
                if self.abp_color and provincial_score > self.total_score_player:
                    self.total_score_player = provincial_score
                    step_taken = move  
                elif not self.abp_color and provincial_score < self.total_score_player:
                    self.total_score_player = provincial_score
                    step_taken = move

                self.board.pop()

                # print(provincial_score, step_taken, move)
        
        # print(step_taken)
        self.board.push(step_taken)

    def alphabeta_minimax(self, minimax_branch, is_maxing_white, alpha, beta):   
        if minimax_branch == 0 or not self.board.legal_moves:
            return evaluate_board(self.board)


        self.total_score_computer = -1e8 if is_maxing_white is True else 1e8
        for move in self.board.legal_moves:
            self.board.push(move)

            provincial_score =self.alphabeta_minimax(minimax_branch - 1, not is_maxing_white, alpha, beta)

            if is_maxing_white:
                self.total_score_computer = max(self.total_score_computer, provincial_score)
                alpha = max(alpha, self.total_score_computer)
           
            else:
                self.total_score_computer = min(self.total_score_computer, provincial_score)
                beta = min(beta, self.total_score_computer)

            self.board.pop()


            if beta <= alpha:
                break

        return self.total_score_computer

