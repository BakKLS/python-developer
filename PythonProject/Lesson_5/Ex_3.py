# Вы разрабатываете систему мониторинга для администраторов.
# У вас есть база данных активных сессий пользователей в виде словаря.
# Вам нужно проверить каждого пользователя на предмет подозрительной активности, заблокировать нарушителей и подвести итоги проверки.
# Заблокировать - статус “blocked”. Результаты: активы не пользователи.
# users_db = {
# “hacker_pro”: {“role”: “user”, “warnings”: 3, “status”: “active”},
# “admin_main”: {“role”: “admin”, “warnings”: 0, “status”: “active”},
# “shadow_bot”: {“role”: “guest”, “warnings”: 5, “status”: “active”},
# }
# Кто-то вводит текст


users_db = {
"hacker_pro": {"role": "user", "warnings": 3, "status": "active"},
"admin_main": {"role": "admin", "warnings": 0, "status": "active"},
"shadow_bot": {"role": "guest", "warnings": 5, "status": "active"},
}

sat = set()
for user in users_db:
    if users_db[user]["warnings"] >= 3:
        users_db[user]["status"] = "blocked"
    else:
        sat.add(user)
print(users_db)
print(sat)
