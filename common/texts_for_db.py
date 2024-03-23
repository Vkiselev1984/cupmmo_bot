from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Юридические услуги', 'Оформление документов']

description_for_info_pages = {
    "main": "Добро пожаловать!",
    "about": "Центр юридической помощи Москвы и Московской области.\nРежим работы - круглосуточно.",
    "payment": as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "При оформлении договора",
        "В отделениях банков",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Варианты оформления документов:"),
            "В офице Центра",
            "С выездом специалиста по адресу",
            "На сайте Центра",
            marker="✅ ",
        ),
        as_marked_section(Bold("Нельзя:"), "Почта", marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Каталог:',
    'cart': 'Вы не сделали выбор!'
}
