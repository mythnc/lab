-- exercise 4.7, 4.8, 4.9

local function palindrome(str)
  for i = 1, #str do
    local j = #str - i + 1
    if i >= j then
      return true
    end
    if string.sub(str, i, i) ~= string.sub(str, j, j) then
      return false
    end
  end
end

local function trim(str)
  local result = ""
  for i = 1, #str do
    local substr = string.sub(str, i, i)
    if (string.byte(substr) >= 97 and string.byte(substr) <= 122)
      or (string.byte(substr) >= 65 and string.byte(substr) <= 90) then
        result = result .. substr
    end
  end
  return result
end

local function get_utf_chars(str)
  local result = {}
  for _, c in utf8.codes(str) do
    table.insert(result, c)
  end
  return result
end

local function palindrome_utf8(chars)
  for i = 1, #chars do
    local j = #chars - i + 1
    if i >= j then
      return true
    end
    if chars[i] ~= chars[j] then
      return false
    end
  end
end

local function trim_utf8(str)
  local result = {}
  for _, c in utf8.codes(str) do
    if c < 127 then
     if (c >= 97 and c <= 122) or (c >= 65 and c <= 90) then
      table.insert(result, c)
     end
    else
      table.insert(result, c)
    end
  end
  return result
end

-- print(palindrome("step on no pets"))
-- print(palindrome("banana"))

-- print(palindrome(trim("step on no pets")))
-- print(palindrome(trim("step on no,pets")))


print(palindrome_utf8(get_utf_chars("上海自來水來自海上")))
print(palindrome_utf8(get_utf_chars("上海自來水來自海")))

print(palindrome_utf8(trim_utf8("上海自來水,來自海 上")))
print(palindrome_utf8(trim_utf8("上海自來水來自 海")))