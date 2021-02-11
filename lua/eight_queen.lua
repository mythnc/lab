BOARD_SIZE = 8 -- board size
CHECK_TIME = 0

-- check whether position (queen_num, column) is free from attacks
function isplaceok(board, queen_num, column)
  CHECK_TIME = CHECK_TIME + 1
  for i = 1, queen_num - 1 do -- for each queen already placed
    if (board[i] == column) or          -- same column?
       (board[i] - i == column - queen_num) or  -- same diagonal?
       (board[i] + i == column + queen_num) then  -- same columdiagonal?
      return false               -- place can be attacked
    end
  end
  return true         -- no attacks; place is OK
end

-- print a board
function printsolution(board)
  for row = 1, BOARD_SIZE do -- for each row
    for column = 1, BOARD_SIZE do -- and for each column
      -- write "X" or "-" plus a space
      io.write(board[row] == column and "X" or "-", " ")
    end
    io.write("\n")
  end
  io.write("\n")
end

-- add to board 'board' all queens from 'queen_num' to 'BOARD_SIZE'
function addqueen(board, queen_num)
  if queen_num > BOARD_SIZE then  -- all queens have been placed?
    printsolution(board)
  else  -- try to place n-th queen
    for column = 1, BOARD_SIZE do
--      if isplaceok(board, queen_num, column) and not isfullplace(board) then
      if isplaceok(board, queen_num, column) then
          board[queen_num] = column  -- place n-th queen at column 'column'
        addqueen(board, queen_num + 1)
      end
    end
  end
end

-- exercise 2.1
function isfullplace(board)
  for i = 1, BOARD_SIZE do
    if not board[i] then
      return false
    end
  end
  return true
end

-- run the program
addqueen({}, 1)
print(CHECK_TIME)