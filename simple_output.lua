flag = 1
speed = 200
target = 182.5
while(true) do
   	x, y, z = getPlayerPos()
   	log("z-target=",math.abs(z-target))
   	if((math.abs(z-target)/2)>2) then
   		speed = 200
   		log('speed = 200')
   	--elseif((math.abs(z-target)/2)>3) then
   		--speed = 160
   		--log('speed = 160')
   	--elseif((math.abs(z-target)/2)>2) then
   		--speed = 120
   		--log('speed = 120')
   	elseif((math.abs(z-target)/2)>1) then
   		speed = 80
   		log('speed = 80')
   	elseif((math.abs(z-target)/2)>0) then
   		speed = 40
   		log('speed = 40')
   	else
   		speed = 0
   		log('speed = 0')
   	end
   	if(z<target) then
		right(speed)
	end
	if(z>target) then
		left(speed)
	end
	os.execute("sleep 0.2")
end
for i = 1, 6 do
    for i = 1,10 do
    	
    end
    speed = speed-40
end

-- 40   171.710
--150   172.357
