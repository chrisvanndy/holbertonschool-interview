This Directory contains an interview prep algortithm "Minimum Operations".  

Given a text file with a single character "H", write a function that returns the number of opertaions required to print exactly "n" number of characters to the text file. There are only two possible operations that can be performed in the text file, copy and paste.

I chose to solve this problem in reverse. Noting that after the first copy paste operation is performed all copy paste operations effectively become the square of an number, I solved the problem by halfing the number of required characters to be printed, and confirming that the number to be printed was in fact a factor of # of characters that would be printed with the follwoing operation.