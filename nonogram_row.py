def nonogram_row(row_string, clue_numbers):
    # find number of clues
    # are there filled cells? 
    # are there empty cells?
    # if only unknown, find difference between clue and len of row, leave difference from both sides, the rest fill



if __name__ == '__main__':
    assert nonogram_row('??????????', [8]) == '??OOOOOO??', 'Simple boxes_1'
    assert nonogram_row('??????????', [4, 3]) == '??OO???O??', 'Simple boxes_2'
    assert nonogram_row('???O????O?', [3, 1]) == 'X??O??XXOX', 'Simple spaces'
    assert nonogram_row('????X?X???', [3, 2]) == '?OO?XXX?O?', 'Forcing'
    assert nonogram_row('O?X?O?????', [1, 3]) == 'OXX?OO?XXX', 'Glue'
    assert nonogram_row('??OO?OO???O?O??', [5, 2, 2]) == 'XXOOOOOXXOOXOOX', 'Joining and splitting'
    assert nonogram_row('????OO????', [4]) == 'XX??OO??XX', 'Mercury'
    assert nonogram_row('???X?', [0]) == 'XXXXX', 'Empty_1'
    assert nonogram_row('?????', []) == 'XXXXX', 'Empty_2'
    assert nonogram_row('??X??', [3]) is None, 'Wrong string'
    print("Check done.")