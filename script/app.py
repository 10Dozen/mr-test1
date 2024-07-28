import os
import datetime 
import argparse

parser.add_argument('-f', action="store", dest='file', default=None)


# Read ISSUE 
# $.getJSON("https://raw.githubusercontent.com/10Dozen/mr-test1/main/site/test.json",e=>{ console.log(e)})
if __name__ == '__main__':
    args = parser.parse_args()
    if not args.file:
        print("No file... ignore")
        return
    
    if len args.file.split(os.path.sep) > 0:
        print("Some nested files... ignore")
        return
    print(args.file)
    
    print(os.environ.get('ALL_CHANGED_FILES'))

    mission_name = "CO33 Test Mission"
    description = "My custom description for the mission"
    
    tgt_dir_name = 'CO33_Test_Mission'
    tgt_dir = f"./site/{tgt_dir_name}"
    
    os.mkdir(tgt_dir)
    with open(os.path.join(tgt_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write("<html>\n")
        f.write(f"<head><script src='data.js'></script><script src='issue.js'></script><title>{mission_name}</title></head>\n")
        f.write("<body><h1>Hello, world! At " + str(datetime.datetime.now()) + "</h1></body>");
        f.write("</html>\n")

    with open(os.path.join(tgt_dir, "data.js"), "w", encoding="utf-8") as f:
        f.write('var data = {"name": 123}')
        
    with open("./envvars", "w", encoding="utf-8") as f:
        f.write("REVIEW_DIR=" + tgt_dir_name)

    with open("./.github/ISSUE_TEMPLATE.md", "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: {mission_name}\n")
        f.write('labels: ["требуется ревью"]\n')
        f.write("---\n")
        f.write("\n")
        f.write("### Миссия:\n")
        f.write("- [Ссылка]({{ env.PAGES_BASE_URL }}/{{ env.REVIEW_DIR }}/index.html)\n")
        f.write("### Описание \n")
        f.write(f"{description}\n")
        f.write("### Автор:\n")
        f.write("{{ actor }}\n")
        f.write("\n")
        
    print("App finished!")
