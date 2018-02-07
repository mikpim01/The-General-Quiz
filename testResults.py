from generalQuiz import db
from shutil import get_terminal_size

width = get_terminal_size()[0]-1
data = db.Get.results(1)
size = int(width/5)

print("\n{qName:^{sizeTwo}} {score:^{size}} {diff:^{size}} {date:^{size}}".format(size=str(size), sizeTwo=str(size*2), qName="Quiz Name", diff="Difficulty", score="Score", date="Date"))
print("~"*width)
for result in data:
    print("{qName:^{sizeTwo}} {score:^{size}} {diff:^{size}} {date:^{size}}".format(size=str(size), sizeTwo=str(size*2), qName=str(result[3]), diff=str(result[6]), score=str(result[5])+"%", date=str(result[7])))
