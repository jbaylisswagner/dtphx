"""
turn .txt files into html files
"""

import os

def main():

    print()
    #filename = input("Enter the story's filename (ex: example.txt): ")
    for filename in os.listdir("/Users/jbwagner/Desktop/phoenix-boom/stories"):
        if filename.endswith(".txt"):
             # print(os.path.join(directory, filename))
            print("Writing html for", filename)
            write_html(filename)

def write_html(filename):
    """
    params: string filename of text file
    writes to a html file
    """

    #filename = "/data/cs21/novels/" + filename
    txt_file = open(filename,'r')
    html_name = filename[:-4] + ".html"
    html_file = open(html_name, 'w')
    bookstring = "" # set up string accumulator

    # loop through each line (one word on each line)
    i=0
    newline = ""
    for line in txt_file:
        i = i+1
        print("line", i, line)
        if (line != "\n"):
            newline = "<p>" + line[:-2] + "</p>\n"
            print(newline)
            html_file.write(newline)

main()
