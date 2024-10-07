local function isempty(s)
    return s == nil or s == ''
end
local function safeWrite(file, str)
    local function write()
        file.write(str)
    end

    local status, err = pcall(write)
    if not status then
        log("Error writing to pipe:", err)
        -- Handle the error, e.g., close the file, clean up, etc.
    end
end
function split(str, delimiter)
	local result = {}
	string.gsub(str, '[^'..delimiter..']+', function(token) table.insert(result, token) end )
	return result
end

local test = filesystem.open('test.txt', 'w') 
for i=1,20 do
	right(i*10)
	os.execute("sleep 0.5")
	x, y, z = getPlayerPos()
	p = getPlayer().pitch
	a = getPlayer().yaw
	t = os.clock()
	safeWrite(test, string.format("%0.5f\n",z))
end

