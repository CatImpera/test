#!/bin/bash

# 檢查 Python 腳本是否存在
if [ ! -f "headgoal_neu.py" ]; then
    echo "錯誤: Python 腳本 'headgoal_neu.py' 不存在"
    exit 1
fi

flag=0
L_list=()
for i in $(seq 13 0.5 35); do
	L_list+=($i)
done
#L_list=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23)
for i in ${L_list[@]}
	do
    # 調用 Python 腳本並傳遞參數
    result=$(python3 headgoal_neu.py "$i" "24")
	
	# 提取 L 和 R 的值
    L=$(echo "$result" | grep "L =" | awk '{print $3}')
    R=$(echo "$result" | grep "R =" | awk '{print $3}')

    # 輸出結果
    echo "L 的值: $L"
    echo "R 的值: $R"
	if [ "$flag" -eq 0 ]; then
    	echo "$L">L.txt
    	echo "$R">R.txt
    	flag=1
    else
    	echo "$L">>L.txt
    	echo "$R">>R.txt
    fi
    echo ""
	done
echo "end"
