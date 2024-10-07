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

local turn = filesystem.open('turn', 'r') --io.open('turn','r')  
local pose = filesystem.open('pose', 'w') --io.open("pose.txt", 'a')
local command = 'Hello :)'
local t = os.clock()
local x = 0
local y = 0
local z = 0
local p = 0
local a = 0
local i = 0
local t0 = os.clock

while(not (command == 'exit')) do

    command = turn:read()  --"*line"
	if not isempty(command) then
		if command == "left" then
			log('left')		
			left(50)     -- in ms
        end
        if command == "right" then
        	log('right')
            right(50)
        end
       	if command == 'stop' then
       		break
       	end
       	x, y, z = getPlayerPos()
		p = getPlayer().pitch
		a = getPlayer().yaw
		t = os.clock()
		log('time = ',t)
		safeWrite(pose, string.format("%0.5f %0.5f %0.5f %0.5f %0.5f %0.5f\n", t, x, y, z, p, a))
    end
    os.execute("sleep 0.01") --sleep(1)    -- same as the above line but smarter
end

turn:close()
pose:close()
