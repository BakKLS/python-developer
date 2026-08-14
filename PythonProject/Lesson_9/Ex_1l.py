def process_telemetry(device_id: str, status: str , *args: int | float) -> str | float:
    # 1. Проверка критического статуса
    if status == "critical":
        return f"Критический сбой оборудования [{device_id}]!"


    if not args:
        return 0


    return me(args)

print(process_telemetry("X-RAY-01", 12.5, 14.0, 15.5))