#!/bin/bash
java -cp FightingICE.jar:lib/gameLib.jar:lib/lwjgl.jar:lib/lwjgl_util.jar:lib/javatuples-1.2.jar:lib/commons_csv.jar:lib/jinput.jar:lib/fileLib.jar:/usr/share/py4j/py4j0.10.4.jar -Djava.library.path="lib/native/linux" Main -n 10 --c1 ZEN --c2 ZEN --a1 Thunder01 --a2 Thunder01Edit --limithp 400 400 --inverted-player 1 --fastmode -df
