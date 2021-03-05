local function insert(dest_str, index, target_str)
  if index < 1 then
    return dest_str
  end

  local prefix = (index > 1) and string.sub(dest_str, 1, index - 1) or ""
  return prefix .. target_str .. string.sub(dest_str, index, -1)
end



local function insert_utf8(dest_str, char_index, target_str)
  local result = ""
  local is_insert = false
  for i, c in utf8.codes(dest_str) do
    if i == utf8.offset(dest_str, char_index) then
      result = result .. target_str
      is_insert = true
    end
    result = result .. utf8.char(c)
  end

  if not is_insert then
    result = result .. target_str
  end

  return result
end


print(insert("hello world", 7, "small ")) --> hello small world
print(insert("hello world", 11, "small ")) --> hello worldsmall
print(insert("hello world", 12, "small ")) --> hello worldsmall
print(insert("hello world", 1, "start: ")) --> start: hello world

local s = "abc"
local target_s = "d"
for i = 1, #s+1 do
  print(insert(s, i, target_s))
end

print(string.rep("-", 10))

print("ação")
print(insert_utf8("ação", 1, "!"))
print(insert_utf8("ação", 2, "!"))
print(insert_utf8("ação", 3, "!"))
print(insert_utf8("ação", 4, "!"))
print(insert_utf8("ação", 5, "!"))