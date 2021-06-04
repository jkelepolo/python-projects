# Jothan Kelepolo
# 008.2
# 8/25/2020


def isBoardValid(board_dict):
    # check for one black and one white king
    if "bking" not in board_dict.values() or "wking" not in board_dict.values():
        return str(board_dict) + "\nFalse board, missing a king piece"

    # check for a maximum of 16 pieces per player
    black_pieces = 0
    white_pieces = 0
    for colour in board_dict.values():
        if colour[0] == "b":
            black_pieces += 1
        elif colour[0] == "w":
            white_pieces += 1
    if black_pieces >= 17 or white_pieces >= 17:
        return str(board_dict) + "\nFalse board, too many pieces"

    # check for at most 8 pawns per player
    if sum(i == "bpawn" for i in board_dict.values()) >= 9 or sum(i == "wpawn" for i in board_dict.values()) >= 9:
        return str(board_dict) + "\nFalse board, too many pawns"

    # check for a valid location
    board_keys = list(board_dict)  # create list of dictionary keys.
    y = ["1", "2", "3", "4", "5", "6", "7", "8"]
    board_y = [s[:1] for s in board_keys]  # removes letters from list.
    if not all(elem in y for elem in board_y):  
        return str(board_dict) + "\nFalse board, not a valid y location"

    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board_x = [s[1:] for s in board_keys]  # removes numbers from list.
    if not all(elem in x for elem in board_x):  
        return str(board_dict) + "\nFalse board, not a valid x location"

    # check if the name starts with a "w" or "b"
    for pieces in board_dict.values():
        if pieces[0] != "b" and pieces[0] != "w":
            return str(board_dict) + "\nFalse board, invalid color '" + pieces[0] +"'"

    # check if the piece name is valid
    piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for names in board_dict.values():
        if names[1:] not in piece_names:
            return str(board_dict) + "\nFalse board, invalid piece '"+ names [1:]+"'"
    return True


# testing boards

# False, invalid piece
print(isBoardValid({"1a": "bking", "2a": "whand", "3a": "wking"})+"\n")

# False, invalid board color
print(isBoardValid({"1a": "bking", "2a": "wpawn", "3a": "wking", "4a": "zpawn"})+"\n")

#False, too many pawns
print(isBoardValid({"1a": "bking", "2a": "wking", "1b": "wpawn", "2b": "wpawn","3b": "wpawn","4b": "wpawn","5b": "wpawn","6b": "wpawn","7b": "wpawn","8b": "wpawn","1c": "wpawn","2c": "wpawn"})+"\n")
