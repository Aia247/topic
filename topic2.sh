#!/bin/bash
read -p "请输入路径（直接换行表示当前目录）:" fpath
if [ "$fpath" = "" ] 
then
    fpath=$(pwd)
fi
let "num = 0"
function file_num() {
	for dir in $(ls $1)
	do
		if [ -d $1"/"$dir ]
		then
			file_num $1"/"$dir
		else
			if [[ $dir == *_gt.json* ]]
			then
				let "num+=1"
			fi
		fi
	done
}
file_num $fpath
echo "当前目录下该文件的个数：$num"
