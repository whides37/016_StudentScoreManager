import json
import statistics

class StudentManager:

    # JSON を読み込む
    def __init__(self, json_path="students_data.json"):
        with open(json_path, "r", encoding="utf-8") as f:
            self.students = json.load(f)

        self.json_path = json_path

    # JSON に保存する関数
    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(self.students, f, ensure_ascii=False, indent=4)

    #追加
    def add_student(self,name):
        if name in self.students:
            raise ValueError("既に登録されています")
        # self.students[name] = {}  # 空の情報を持つ学生として登録
        self.students[name] = []  # 点数を入れるリストにする
        self.save()


    #削除
    def remove_student(self,name):
        if name not in self.students:
            raise ValueError("登録なしです")
        del self.students[name]
        self.save()

    #点数登録
    def add_score(self,name, score):
        if name not in self.students:
            raise ValueError("登録のない生徒です")
        if not isinstance(score,int):
            raise ValueError("点数は半角数字で入力してください")
        self.students[name].append(score)
        self.save()

    # 平均点
    def get_all_average(self):
        all_scores = [score for scores in self.students.values() for score in scores]
        if not all_scores:
            return 0
        return statistics.mean(all_scores)

    #学生リスト
    def list_students(self):
        return "\n".join(self.students.keys())
