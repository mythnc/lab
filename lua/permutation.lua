-- exercise 2.2

function init(n)
  seq = {}
  for i = 1, n do
      seq[i] = i
  end
  return seq
end

function swap(seq, i, j)
  local temp = seq[i]
  seq[i] = seq[j]
  seq[j] = temp
end

function reverse(seq, start_i, n)
  local i = start_i
  local j = n
  while i < j do
    swap(seq, i, j)
    i = i + 1
    j = j - 1
  end
end

-- find the first biggest value in seq[start] ~ seq[n] that great than 'value'
function get_max_index(seq, start, n, value)
  local max = n + 1
  local max_i = -1
  for i = start, n do
    -- print("value in index i - ", seq[i])
    if seq[i] > value and seq[i] < max then
      max = seq[i]
      max_i = i
    end
  end
  -- print("max_i before return", max_i)
  return max_i
end

function get_next_permutation(seq, n)
  for i = n-1, 1, -1 do
      if seq[i] < seq[i+1] then
        if i+1 < n then
          reverse(seq, i+1, n)
          -- print(table.unpack(seq))
        end
        local max_i = get_max_index(seq, i+1, n, seq[i])
        -- print(max_i)
        swap(seq, max_i, i)
        return seq
      end
  end
  return nil
end

n = 8
seq = init(n)
-- seq = {2,3, 1}
-- seq = {5,2,1,3, 4, 6}
-- print(table.unpack(seq))
-- get_next_p(seq, n)
-- print(table.unpack(seq))
while get_next_permutation(seq, n) do
  print(table.unpack(seq)) 
end
