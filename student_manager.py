import json
import statistics

class StudentManager:

    # JSONを読み込む
    def __init__(self, json_path="students_data.json"):
        self.json_path = json_path
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                self.students = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = {}

    # JSONに保存
    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(self.students, f, ensure_ascii=False, indent=4)

    # 新規学生追加
    def add_student(self, name):
        if name in self.students:
            raise ValueError(f"{name} は既に登録されています")
        self.students[name] = {"国語": 0, "数学": 0, "社会": 0}
        self.save()

    # 点数登録
    def add_score(self, name, subject, score):
        if name not in self.students:
            # 生徒がいない場合は新規作成
            self.add_student(name)
        
        if subject not in ["国語", "数学", "社会"]:
            raise ValueError("教科は '国語', '数学', '社会' のいずれかを指定してください")
            
        if not isinstance(score, int):
            raise ValueError("点数は半角数字で入力してください")
        
        if not (0 <= score <= 100):
            raise ValueError("点数は0から100の間で入力してください")

        self.students[name][subject] = score
        self.save()

    # 削除
    def remove_student(self, name):
        if name not in self.students:
            raise ValueError("登録なしです")
        del self.students[name]
        self.save()

    # 平均点（全生徒・全教科）
    def get_all_average(self):
        all_scores = []
        for scores in self.students.values():
            for score in scores.values():
                all_scores.append(score)

        if not all_scores:
            return 0
        return round(statistics.mean(all_scores))
