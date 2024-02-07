files = {
    '1.txt': [
        "Начальник  полиции",
        "лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд",
        "в дежурке и других комнатах нижнего этажа раздались звонки",
        "    Когда Иенсен  --  комиссар  шестнадцатого  участка --  вышел  из своего",
        "кабинета,  звонки еще  не смолкли. Иенсен был мужчина средних лет,  обычного",
        "сложения, с лицом плоским и невыразительным. На последней ступеньке винтовой",
        "лестницы  он задержался  и  обвел взглядом помещение дежурки. Затем поправил",
        "галстук и проследовал к машине."
    ],
    '2.txt': [
        "Тревога началась в тринадцать часов ноль две минуты."
    ],
    '3.txt': [
        "    В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди",
        "потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире",
        "резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.",
        "Одеты они были хорошо, но как-то удивительно походили друг на друга и все до",
        "одного спешили. Они шли нестройными  вереницами, широко разливались, завидев",
        "красный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно",
        "озирались по сторонам и теребили портфели и сумочки.",
        "    Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту",
        "толчею."
    ]
}

file_lengths = [(filename, len(content)) for filename, content in files.items()]

file_lengths.sort(key=lambda x: x[1])

with open('result.txt', 'w') as result_file:
    for filename, length in file_lengths:
        result_file.write(filename + '\n')
        result_file.write(str(length) + '\n')
        for line in files[filename]:
            result_file.write(line + '\n')
        result_file.write('\n')