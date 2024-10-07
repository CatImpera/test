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

local file = filesystem.open('output_avoid_command_here', 'r')
local command = 'Hello :)'

local file_pose = filesystem.open('output_pose_here', 'w')

local t = os.clock()
local x = 0
local y = 0
local z = 0
local p = 0
local a = 0
local i = 0

while(not (command == 'exit')) do

    command = file:read()
    if not isempty(command) then
        --io.write(string.format)
        --print(command)
        --log(command)
        if command == 'forward' then
            forward(40)     -- in ms
        end
        if command == 'back' then
            back(40)
        end
        if command == 'left' then
            left(40)
        end
        if command == 'right' then
            right(40)
        end
    end

    x, y, z = getPlayerPos()
    p = getPlayer().pitch
    a = getPlayer().yaw
    t = os.clock()
    --file_pose.write(string.format("%0.5f %0.5f %0.5f %0.5f %0.5f %0.5f\n", t, x, y, z, p, a))
    safeWrite(file_pose, string.format("%0.5f %0.5f %0.5f %0.5f %0.5f %0.5f\n", t, x, y, z, p, a))
    i = i + 1

    --os.execute('sleep ' .. tonumber(0.001))
    sleep(1)    -- same as the above line but smarter
end

