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