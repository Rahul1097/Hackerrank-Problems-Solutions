**Text Wrap**

You are given a string s and width w .
Your task is to wrap the string into a paragraph of width 

**Function Description**

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to

**Returns**

string: a single string with newline characters ('\n') where the breaks should be

**Input Format**

The first line contains a string, .
The second line contains the width, .

**Constraints**

0 < len(string) < 1000
0 < maxwidth < len(string)

**Sample Input**

ABCDEFGHIJKLIMNOQRSTUVWXYZ

4

**Sample Output**

ABCD

EFGH

IJKL

IMNO

QRST

UVWX

YZ
