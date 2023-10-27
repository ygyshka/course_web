NULLABLE = {'null': True, 'blank': True}
STATUS_CREATE = 'create'
STATUS_ACTIVE = 'active'
STATUS_CLOSE = 'finish'
STATUS_CODE = [
    (STATUS_CREATE, 'создана'),
    (STATUS_ACTIVE, 'запущена'),
    (STATUS_CLOSE, 'завершена'),
]


DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
PERIODICITY = [
    (DAILY, 'раз в день'),
    (WEEKLY, 'раз в неделю'),
    (MONTHLY, 'раз в месяц'),
]

EMPTY_BLOG = 'На данный момент в нашем блоге нет статей.\nОжидайте обновления контента платформы!!!'