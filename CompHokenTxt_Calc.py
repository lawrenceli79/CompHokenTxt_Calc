import sys
import re

strFile1 = sys.argv[1]
strFile2 = sys.argv[2]

BLOCK_END = "---------------------------------------------------------------\n"

def FindLine(lines:list[str], strRegex:str, start:int) -> int:
    for i in range(start, len(lines)):
        line = lines[i]
        if re.search(strRegex, line):
            return i
    return -1

def CompareBlockCore(lines1:list[str], start1:int, lines2:list[str], start2:int, strEndLine:str):
    bSame = True
    nMaxCnt1 = len(lines1)-start1
    nMaxCnt2 = len(lines2)-start2
    nMaxCnt = min(nMaxCnt1,nMaxCnt2)

    for i in range(0, nMaxCnt):
        line1 = lines1[i+start1]
        line2 = lines2[i+start2]
        if (line1==strEndLine and line2==strEndLine):
            break
        elif (line1==strEndLine or line2==strEndLine):
            bSame = False
            break
        elif (line1!=line2):
            bSame = False
            break
    return bSame

def CompareBlock(lines1:list[str], lines2:list[str], tag:str) -> bool:
    start1 = FindLine(lines1, tag, 0)
    start2 = FindLine(lines2, tag, 0)
    bSame = CompareBlockCore(lines1, start1+1, lines2, start2+1, BLOCK_END)
    return bSame

def PrintOut(strFile1:str,strFile2:str,strBlock:str,bSame:bool):
    strStatus = "Same" if bSame else "Diff"
    print("{},{},{},{}\n".format(strFile1,strFile2,strBlock,strStatus))


with open(strFile1, 'r', errors='ignore') as f1, open(strFile2, 'r', errors='ignore') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    bSame = CompareBlock(lines1, lines2, "^保険計算後")
    PrintOut(strFile1, strFile2, "保険計算後", bSame)
