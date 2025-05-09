from surrealdb import Surreal # type: ignore


# الاتصال بقاعدة البيانات
def connect_db():
    db = Surreal("http://localhost:8000")
    db.signin({"username": "torootdo", "password": "torootdo"})
    db.use("todo", "todo")
    return db

# تسجيل مستخدم جديد
def register_user(db, username, password, age, email, firstname, lastname):
    
    # التحقق من عدم وجود مستخدم بنفس الاسم
    existing = db.query(f"SELECT * FROM user WHERE username = '{username}'")
    if existing[0]['result']:
        print("Username already exists!")
        return None
    
    # إنشاء المستخدم
    db.query(f"CREATE user SET username = '{username}', password = '{password}', email = '{email}', age = {age}, firstname = '{firstname}', lastname = '{lastname}'")


# تسجيل الدخول
def login_user(db, username, password):    
    result = db.query(f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'")
    if not result['result']:
        print("Invalid credentials!")
        return None
    return username

# # إضافة مهمة
# def add_task(db, user_id):
#     title = input("Task title: ")
#     description = input("Task description: ")
#     db.create(f"{user_id}", {
#         'title': title,
#         'description': description,
#         'completed' : False,
#         'username': user_id
#     })
#     print("Task added!")

# # عرض المهام
# def show_tasks(db, user_id):
#     tasks = db.query(f"SELECT * FROM {user_id}")
#     if not tasks[0]['result']:
#         print("No tasks found.")
#         return
    
#     task = tasks[0]['result']

#     for idx in range(len(tasks[0]['result'])):
#         status = True if task[idx]['completed'] else False
#         print(f"{idx}. [{status}] {task[idx]['title']} - {task[idx]['description']}")

# # تحديث حالة المهمة
# def update_task(db, user_id):
#     show_tasks(db, user_id)
#     task_id = input("Enter task number to update: ")
    
#     tasks = db.query(f"SELECT * FROM {user_id}")
#     if not tasks[0]['result'] or int(task_id) > len(tasks[0]['result']):
#         print("Invalid task number!")
#         return
    
#     task = tasks[0]['result'][int(task_id)]
#     new_status = not task['completed']
#     db.update(task['id'], {'title': task['title'],
#         'description': task['description'],
#         'completed' : new_status,
#         'username': user_id
#         })
#     print("Task updated!")

# حذف مهمة
# def delete_task(db, user_id):
#     show_tasks(db, user_id)
#     task_id = input("Enter task number to delete: ")
    
#     tasks = db.query(f"SELECT * FROM {user_id}")
#     if not tasks[0]['result'] or int(task_id) > len(tasks[0]['result']):
#         print("Invalid task number!")
#         return
    
#     task = tasks[0]['result'][int(task_id)]
#     db.delete(task['id'])
#     print("Task deleted!")

# القائمة الرئيسية
def main(choice, username, password, age, email, firstname, lastname):
    db = connect_db()
    
    if choice == '1':
        register_user(db, username, password, email, firstname, lastname)
    elif choice == '2':
        login_user(db, username, password)

# تشغيل التطبيق
if __name__ == "__main__":
    main()