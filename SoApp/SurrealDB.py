from surrealdb import Surreal
import asyncio

# الاتصال بقاعدة البيانات
async def connect_db():
    db = Surreal("http://localhost:8000")
    await db.connect()
    await db.signin({"user": "torootdo", "pass": "torootdo"})
    await db.use("todo", "todo")
    return db

# تسجيل مستخدم جديد
async def register_user(db, username, password, email, firstname, lastname):
    
    # التحقق من عدم وجود مستخدم بنفس الاسم
    existing = await db.query(f"SELECT * FROM user WHERE username = '{username}'")
    if existing[0]['result']:
        print("Username already exists!")
        return None
    
    # إنشاء المستخدم
    user = await db.create("user", {
        "username": username,
        "password": password,
        "email" : email,
        "firstname" : firstname,
        "lastname" : lastname
    })
    await db.query(f"DEFINE TABLE {username};")
    print("Registration successful!")
    return user['username']

# تسجيل الدخول
async def login_user(db, username, password):    
    result = await db.query(f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'")
    if not result[0]['result']:
        print("Invalid credentials!")
        return None
    return username

# # إضافة مهمة
# async def add_task(db, user_id):
#     title = input("Task title: ")
#     description = input("Task description: ")
#     await db.create(f"{user_id}", {
#         'title': title,
#         'description': description,
#         'completed' : False,
#         'username': user_id
#     })
#     print("Task added!")

# # عرض المهام
# async def show_tasks(db, user_id):
#     tasks = await db.query(f"SELECT * FROM {user_id}")
#     if not tasks[0]['result']:
#         print("No tasks found.")
#         return
    
#     task = tasks[0]['result']

#     for idx in range(len(tasks[0]['result'])):
#         status = True if task[idx]['completed'] else False
#         print(f"{idx}. [{status}] {task[idx]['title']} - {task[idx]['description']}")

# # تحديث حالة المهمة
# async def update_task(db, user_id):
#     await show_tasks(db, user_id)
#     task_id = input("Enter task number to update: ")
    
#     tasks = await db.query(f"SELECT * FROM {user_id}")
#     if not tasks[0]['result'] or int(task_id) > len(tasks[0]['result']):
#         print("Invalid task number!")
#         return
    
#     task = tasks[0]['result'][int(task_id)]
#     new_status = not task['completed']
#     await db.update(task['id'], {'title': task['title'],
#         'description': task['description'],
#         'completed' : new_status,
#         'username': user_id
#         })
#     print("Task updated!")

# حذف مهمة
# async def delete_task(db, user_id):
#     await show_tasks(db, user_id)
#     task_id = input("Enter task number to delete: ")
    
#     tasks = await db.query(f"SELECT * FROM {user_id}")
#     if not tasks[0]['result'] or int(task_id) > len(tasks[0]['result']):
#         print("Invalid task number!")
#         return
    
#     task = tasks[0]['result'][int(task_id)]
#     await db.delete(task['id'])
#     print("Task deleted!")

# القائمة الرئيسية
async def main(choice, username, password, email, firstname, lastname):
    db = await connect_db()
    
    if choice == '1':
        await register_user(db, username, password, email, firstname, lastname)
    elif choice == '2':
        await login_user(db, username, password)

# تشغيل التطبيق
if __name__ == "__main__":
    asyncio.run(main())