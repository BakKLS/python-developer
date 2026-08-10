# Задание 1 *
# Напишите рекурсивную функцию find_file(folder,
# target_filename), которая ищет полный путь к
# целевому файлу в словаре-дереве и возвращает строку с
# путем или None.
# file_system = {
# "documents": {
# "work": {
# "project_notes.txt": "content",
# "budget.xlsx": "content"
# },
# "personal": {
# "passport.pdf": "content"
# }
# },
# "photos": {
# "vacation.jpg": "content"
# }
# }


def find_file(folder: dict, target_filename: str) -> str | None:

    for name, content in folder.items():

        if isinstance(content, str):

            if name == target_filename:
                return name


        elif isinstance(content, dict):

            subpath = find_file(content, target_filename)


            if subpath is not None:

                return f"{name}/{subpath}"


    return None


file_system = {
    "documents": {
        "work": {
            "project_notes.txt": "content",
            "budget.xlsx": "content"
        },
        "personal": {
            "passport.pdf": "content"
        }
    },
    "photos": {
        "vacation.jpg": "content"
    }
}


print(find_file(file_system, "budget.xlsx"))
print(find_file(file_system, "vacation.jpg"))
print(find_file(file_system, "secret_plan.docx"))