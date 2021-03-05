-- Exercise 4.5

local function remove(str, init_pos, length)
  local result = ""
  for i = 1, #str do
    if not (i >= init_pos and i <= init_pos + length - 1) then
      result = result .. string.sub(str, i, i)
    end
  end
  return result
end

local function remove2(str, init_pos, length)
  return string.sub(str, 1, init_pos-1) .. string.sub(str, init_pos+length)
end

print(remove("hello world", 7, 4))
print(remove2("hello world", 7, 4))
