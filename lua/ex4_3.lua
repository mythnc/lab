local function insert(dest_str, index, target_str)
  if index < 1 then
    return dest_str
  end

  local prefix = (index > 1) and string.sub(dest_str, 1, index - 1) or ""
  return prefix .. target_str .. string.sub(dest_str, index, -1)
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
