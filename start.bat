setlocal ENABLEDELAYEDEXPANSION
set PATH=%PATH%;./lib/native/windows
java -cp FightingICE.jar;./lib/lwjgl.jar;./lib/lwjgl_util.jar;./lib/gameLib.jar;./lib/fileLib.jar;./lib/jinput.jar;./lib/commons_csv.jar;./lib/javatuples-1.2.jar;./lib/py4j0.10.4.jar Main -n 10 --c1 ZEN --c2 ZEN --a1 Thunder01 --a2 Thunder01Edit --limithp 400 400 --inverted-player 1 --fastmode --disable-window -df
endlocal
exit