from student_manager import StudentManager

def main():
    
    #インスタンスを作る
    manager = StudentManager()  

    # 生徒追加
    manager.add_student("Kity")

    # 点数追加
    manager.add_score("Mimi", 10)
    manager.add_score("Kiki", 40)
    manager.add_score("Lala", 90)
    manager.add_score("Kity", 60)

    # 平均点取得

    # 生徒一覧
    print("登録されている生徒:")
    print(manager.list_students())

if __name__ == "__main__":
    main()
