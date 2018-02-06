from generalQuiz import db
from shutil import get_terminal_size

width = get_terminal_size()[0]-1
data = db.Get.results(1)
print(str(data))

print("\n{0:^25} {1:^10}".format("Quiz Name","Score"))
print("~"*width)
for result in data:
    print("{0:^25} {1:^10}".format(result[3],result[5]+"%"))
