
# we can also create a new file by running the command below, just changing the name
write_file = open("file1.txt", "w")

# when we use W it override the whole file
# A- append adds text to the end of the file
print(write_file.write(" Olya"))
write_file.close()


