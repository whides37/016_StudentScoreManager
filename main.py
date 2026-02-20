from student_manager import StudentManager

def main():

    manager = StudentManager()

    # 点数追加・更新
    # Mimiの各教科の点数を登録
    manager.add_score("Mimi", "国語", 85)
    manager.add_score("Mimi", "数学", 100)
    manager.add_score("Mimi", "社会", 75)
    
    # 他の生徒の点数も適当に登録
    manager.add_score("Kiki", "国語", 40)
    manager.add_score("Kiki", "数学", 60)
    manager.add_score("Kiki", "社会", 50)
    
    manager.add_score("Lala", "国語", 90)
    manager.add_score("Lala", "数学", 95)
    manager.add_score("Lala", "社会", 92)

    # 全体平均
    print(f"全体平均: {manager.get_all_average()}点")

    # 最高点・最低点
    max_student, max_sub, max_val = manager.get_max_score()
    print(f"最高点: {max_student} ({max_sub}) - {max_val}点")
    
    min_student, min_sub, min_val = manager.get_min_score()
    print(f"最低点: {min_student} ({min_sub}) - {min_val}点")

    # ランキング
    print("\nランキング (平均点順):")
    for name, avg in manager.get_ranking():
        print(f"{name}: {avg:.1f}点")

    # 生徒一覧
    print("\n登録されている生徒の詳細:")
    print(manager.list_students())

if __name__ == "__main__":
    main()