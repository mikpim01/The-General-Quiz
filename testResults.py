from generalQuiz import db

data = db.Get.results(1)
print(str(data))

print("\n{0:^25} {1:^10}".format("Quiz Name","Score"))
print("~"*35)
for result in data:
    print("{0:^25} {1:^10}".format(result[3],result[5]+"%"))
