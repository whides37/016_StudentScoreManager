class StudentManager:

    def __init__(self):
        self.students = {}

    #追加
    def add_student(self,name):
        if name in self.students:
            raise ValueError("既に登録されています")
        else:
            self.students[name] = {}  # 空の情報を持つ学生として登録

    #削除
    def remove_student(self,name):
        if name not in self.students:
            raise ValueError("登録なしです")
        del self.students[name]

    #点数登録
    def add_score(self,name, score):
        if name not in self.students:
            raise ValueError("登録のない生徒です")
        if not isinstance(score,int):
            raise ValueError("点数は半角数字で入力してください")
        else:
            self.students[name].append(score)