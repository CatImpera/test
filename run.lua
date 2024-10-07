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

local turn = filesystem.open('turn', 'r') --io.open('turn','r')  
local pose = filesystem.open('pose', 'w') --io.open("pose.txt", 'a')
local go = 0
local value = 0
local list = ''
local t = os.clock()
local x = 0
local y = 0
local z = 0
local p = 0
local a = 0
local i = 0
local t0 = 0
local flag = false

while(not (command == 'exit')) do
	local command = 'Hello :)'
	local tmp = 'hashi'
    command = turn:read()  --"*line"
    --log('flag = ', flag)
    if flag == true then
    	--log('time = ', os.clock()-t0)
    end
	if not isempty(command) then
		if (not flag) then
			flag = true
			t0 = os.clock()
		end
		--log('len = '..string.len(command)..'command = '..command)
		--log('command[1] = ',string.sub(command, 1, 1), 'command[2] = ', string.sub(command, 2, 2))
		go = string.sub(command, 1, 1)
		value = tonumber(string.sub(command, 2, 3))
		t = os.clock()
		if go == "L" then
			--log('left = '..value)	
			log('time = ',t, 'value = ', value)		
			left(value*5)     -- in ms
        end
        if go == "R" then
        	--log('right = '..value)
        	log('time = ',t, 'value = ', value)
            right(value*5)
        end
        if go == "F" then
        	log('time = ',t, 'value = forward')
        	forward(200)
        end
       	if go == 'S' then
       		break
       	end
       	x, y, z = getPlayerPos()
		p = getPlayer().pitch
		a = getPlayer().yaw
		t = os.clock()
		--log('time = ',t, 'value = ', value)
		--log('Z = ', z)
		safeWrite(pose, string.format("%0.5f %0.5f %0.5f %0.5f %0.5f %0.5f\n", t, x, y, z, p, a))
    end
    --os.execute("sleep 0.01") --sleep(1)    -- same as the above line but smarter
end

turn:close()
pose:close()
