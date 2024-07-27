
import datetime 

if __name__ == '__main__':
	with open("page.html", "w", encoding="utf-8") as f:
		f.write("<html><body><h1>Hello, world! At " + str(datetime.datetime.now()) + "</h1></body></html>");
    print("App finished!")

