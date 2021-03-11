-- Exercise 4.5 & Exercise 4.6

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

local function remove_utf8(str, init_pos, length)
  local result = ""
  for i, c in utf8.codes(str) do
    if not (i >= utf8.offset(str, init_pos) and i < utf8.offset(str, init_pos+length)) then
      result = result .. utf8.char(c)
    end
  end
  return result
end

local function remove2_utf8(str, init_pos, length)
  return string.sub(str, 1, utf8.offset(str, init_pos-1)) .. string.sub(str, utf8.offset(str, init_pos+length))
end


print(remove("hello world", 7, 4))
print(remove2("hello world", 7, 4))

print(remove_utf8("ação", 2, 2))
print(remove2_utf8("ação", 2, 2))
