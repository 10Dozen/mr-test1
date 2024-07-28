import os
import datetime 

if __name__ == '__main__':
	with open("./site/page.html", "w", encoding="utf-8") as f:
		f.write("<html><body><h1>Hello, world! At " + str(datetime.datetime.now()) + "</h1></body></html>");
    
    with open("./envvars", "w", encoding="utf-8") as f:
        f.write("ISSUE_TITLE=My Mission Title\n")
        f.write("ISSUE_LINK_TO_PAGE=page.html\n")
        f.write("ISSUE_DESC=Mission description\n")

	print("App finished!")
