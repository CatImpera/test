local function isempty(s)
    return s == nil or s == ''
end

local file = io.open('output_avoid_command_here','r') --filesystem.open('output_avoid_command_here', 'r')
local command = 'Hello :)'

while(not (command == 'exit')) do
    command = file:read()
    if not isempty(command) then
        --io.write(string.format)
        print(command)
        --log(command)
        --if command == 'forward' then
        --    forward(40)     -- in ms
        --end
        --if command == 'back' then
        --    back(40)
        --end
        --if command == 'left' then
        --    left(40)
        --end
        --if command == 'right' then
        --    right(40)
        --end
    end
    --os.execute('sleep ' .. tonumber(0.001))
    os.execute("sleep 0.04") --sleep(1)    -- same as the above line but smarter
end


