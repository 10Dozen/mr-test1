import os
import datetime 

if __name__ == '__main__':
	with open("./site/page.html", "w", encoding="utf-8") as f:
		f.write("<html><body><h1>Hello, world! At " + str(datetime.datetime.now()) + "</h1></body></html>");
    
	with open("./.github/ISSUE_TEMPLATE.md", "w", encoding="utf-8") as f:
		f.write("---\n")
		f.write("title: My Custom Mission name\n")
		f.write('labels: ["требуется ревью"]\n')
		f.write("---\n")
		f.write("\n")
		f.write("#### Миссия:\n")
		f.write("- [Ссылка](https://10dozen.github.io/mr-test1/page.html)\n")
		f.write("#### Описание \n")
		f.write("Description\n")
		f.write("#### Автор:\n")
		f.write("{{ actor }}\n")
		f.write("\n")

	print("App finished!")
