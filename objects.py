class Board:
    def __init__(self):
        self.mapping = {"11": " ", "12": " ", "13": " ",
                        "21": " ", "22": " ", "23": " ",
                        "31": " ", "32": " ", "33": " "}
        self.board = ""
        self.win = []

    def show_board(self):
        self.board = f' {self.mapping["11"]} | {self.mapping["12"]} | {self.mapping["13"]} \n___|___|___\n ' \
                     f'{self.mapping["21"]} | {self.mapping["22"]} | {self.mapping["23"]} \n___|___|___\n ' \
                     f'{self.mapping["31"]} | {self.mapping["32"]} | {self.mapping["33"]} \n   |   |   '
        print(self.board)

    def check_winner(self):
        self.win = [(self.mapping["11"], self.mapping["12"], self.mapping["13"]),
                    (self.mapping["21"], self.mapping["22"], self.mapping["23"]),
                    (self.mapping["31"], self.mapping["32"], self.mapping["33"]),
                    (self.mapping["11"], self.mapping["21"], self.mapping["31"]),
                    (self.mapping["12"], self.mapping["22"], self.mapping["32"]),
                    (self.mapping["13"], self.mapping["23"], self.mapping["33"]),
                    (self.mapping["11"], self.mapping["22"], self.mapping["33"]),
                    (self.mapping["13"], self.mapping["22"], self.mapping["31"])]
        check_x = any(all(val == "X" for val in tup) for tup in self.win)
        check_o = any(all(val == "O" for val in tup) for tup in self.win)
        if check_x:
            print("Player X is the winner!\nThank you for playing!")
            return True
        elif check_o:
            print("Player O is the winner!\nThank you for playing!")
            return True
