file = io.open("pose.txt", "a")
io.output(file)
local t = os.clock()
local x = 0
local y = 0
local z = 0
local p = 0
local a = 0
local i = 0
while true do
    x, y, z = getPlayerPos()
    p = getPlayer().pitch
    a = getPlayer().yaw
    t = os.clock()
    getScreen().save(string.format("./images/%d.jpg", i), "jpg")
    io.write(string.format("%0.5f %0.5f %0.5f %0.5f %0.5f %0.5f\n", t, x, y, z, p, a))
    i = i + 1
    sleep(1)
end
