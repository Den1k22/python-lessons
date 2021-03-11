

f = open("file_name.txt", "w")  # open file for writing

f.write("Some text with out new line ")

f.write("Some text.\nSome text.\nSome text.")

f.close()  # always close the file

# "D:\\myfiles\file_name.txt" - backslash symbol (\) is for path in windows
# "/myfiles/file_name.txt" - slash symbol (/) is for path in Mac or Linux


f = open("file_name.txt", "r")  # open file for reading

# END OF FILE (EOF) - name of the symbol which defines that file is ended

# read() - reads everything from current cursor position till EOF and returns everything in one string
# print (f.read())
# readline() - reads line from current cursor position till end of line(\n) or EOF
# print (f.readline())
# readlines() - reads each line from current cursor position till EOF and stores them as array
# print (f.readlines())

print(f.read())  # example of reading the file

f.close()  # always close the file

option = "w"
f = open("file_name", option)  # options: w - open file for writing, r - open file for reading
f.write("line to file")
f.read()  # reads everything from current cursor position till EOF and returns everything in one string
f.readline()  # readline() - reads line from current cursor position till end of line(\n) or EOF
f.close()
