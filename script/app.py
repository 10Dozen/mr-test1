import os
import datetime 

if __name__ == '__main__':
	with open("./site/page.html", "w", encoding="utf-8") as f:
		f.write("<html><body><h1>Hello, world! At " + str(datetime.datetime.now()) + "</h1></body></html>");
    os.environ['ISSUE_TITLE'] = 'Test mission'
    os.environ['ISSUE_LINK_TO_PAGE'] = 'page.html'
    os.environ['ISSUE_DESC'] = 'Test mission description'
	print("App finished!")

