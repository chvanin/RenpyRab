# Определение персонажей игры.
# Главный герой
define alex = Character('Алекс', color="#5d0f91")

# Общие персонажи
define zk = Character('Заклятие кошмара', color="#b32929")
define lilith = Character('Лилит', color="#800080")  

# Персонажи пути Теневого охотника
define shade = Character('Шейд', color="#2f4f4f")  
define varan = Character('Варан', color="#8b0000")  
define kira = Character('Кира', color="#4169e1")  

# Персонажи пути Кристального стража
define aurora = Character('Аврора', color="#00bfff")
define crystal = Character('Кристалл-архивариус', color="#20b2aa")
define sapphire = Character('Сапфир', color="#0000cd") 
define obsidian = Character('Обсидиан', color="#2f2f2f")

# Второстепенные персонажи
define max_merchant = Character('Торговец Макс', color="#daa520")  
define chaser = Character("Бандит", color="#0855a1")

# Для повествования 
define narrator = Character(None)

# Определяем изображения персонажей
image Alex1 = "Alex.png"
image ZK1 = "zk_image.png"
image Lilith1 = "Lilit.png"
image Shade1 = "Varan.png"
image Varan1 = "Varan.png"
image Kira1 = "Kira.png"
image Aurora1 = "Aurora.png"
image Crystal = "Crystal.png"
image Sapphire1 = "Sapphire.png"
image Obsidian1 = "Obsidian.png"
image Max_merchant1 = "Max.png"
image Chaser1 = "Chaser.png"

# Булева переменная, отвечающая за роман с Кирой
default romance_with_kira = False

init python:
    import random

    def random_event(success_rate=0.5, success_label=None, failure_label=None):
        """
        Универсальная функция для обработки случайных событий.
        
        :param success_rate: Вероятность успеха (значение от 0 до 1).
        :param success_label: Метка, куда перейти в случае успеха.
        :param failure_label: Метка, куда перейти в случае неудачи.
        """
        # Генерация случайного числа от 0 до 1
        if random.random() < success_rate:
            if success_label:
                renpy.jump(success_label)  # Переход на метку успеха
            return "успех"
        else:
            if failure_label:
                renpy.jump(failure_label)  # Переход на метку неудачи
            return "неудача"

# Пролог
label start:

    scene startpoema with fade

    narrator "Япония в VIII–IX веках."

    narrator "Феодалы стали полагаться на своих собственных воинов для защиты земель и обеспечения безопасности."

    scene poema2 with fade

    narrator "По провинциям бушует голод и смерть народа."

    narrator "Выживет сильнейший... Ночь, трущобы."

    scene poema5 with fade

    narrator "Алекс, раненый и истощённый, бредёт по узким переулкам. Его преследователи не отстают."

    scene poema3 with fade

    show Chaser1 at right
    chaser "Мы знаем, что ты здесь, мальчишка! Прекрати бегать! От нас не уйдёшь."
    hide Chaser1

    scene poema4 with fade

    narrator "Громкий хохот и шаги становятся всё ближе. Алекс спотыкается и падает. Кровь из раны пачкает землю."

    show Alex1 at left
    alex "Не сейчас... Я ещё жив..."
    hide Alex1

    narrator "Силы покидают его. Холодная земля принимает его без сознания. Но именно в этот момент мир меняется."

    scene poema6 with fade

    narrator "Всё вокруг становится чёрным. Тишина сменяется гулом неземных голосов. Алекс открывает глаза, но перед ним нет ничего, кроме пустоты... и тени."

    show ZK1 at right
    zk "Алекс... Я наблюдал за тобой. Ты стоишь на краю пропасти между жизнью и смертью."
    hide ZK1

    show Alex1 at left
    alex "Кто здесь? Что это за место?"
    hide Alex1

    scene poema7 with fade

    show ZK1 at right
    zk "Это неважно. Важно лишь то, что ты хочешь жить. Я могу дать тебе силу. Но помни, плата за мою помощь будет высокой."
    hide ZK1

    narrator "Перед Алексом начинает формироваться фигура из густого мрака. Красные глаза сверкают, пронизывая его душу."

    show Alex1 at left
    alex "Силу? Какую силу? И зачем ты мне помогаешь?"
    hide Alex1

    show ZK1 at right
    zk "Ты будешь моим проводником. Мир ещё не готов увидеть истинное лицо Кошмара, но через тебя оно заговорит. Ты выберешь путь, который изменит твою судьбу."
    hide ZK1

    scene poema8 with fade

    narrator "Заклятие Кошмара протягивает перед Алексом две руки. В одной — клубок тьмы, в другой — сияющий кристалл."

    show ZK1 at right
    zk "Тени или кристаллы? Уничтожение или созидание? Решай, Алекс."
    hide ZK1

    show Alex1 at left
    narrator "Холод сковывает его тело, но огонь в душе разгорается. Его выбор станет судьбоносным."
    hide Alex1

    menu:

        "Принять Путь Теней":
            jump arrow_shadow

        "Принять Путь Кристаллов":
            jump arrow_crystal

    return


# Ветка 1.1 выбор пути 
label arrow_shadow:
    scene poema10 with fade

    show Alex1 at left
    alex "Что за... Где я? Это место — словно из моего кошмара."
    hide Alex1

    show Lilith1 at right
    lilith "Твои сны недалеко ушли от реальности."
    lilith "Я Лилит. Добро пожаловать в Мир Теней. Здесь, среди бесконечной тьмы, каждый шаг становится выбором."
    lilith "И я могу помочь тебе понять его, если ты доверишься мне."
    hide Lilith1

    scene poema11 with fade

    show Alex1 at left
    alex "Ты знаешь, кто я?"
    hide Alex1

    show Lilith1 at right
    lilith "Я знаю больше, чем ты думаешь. Но это не так важно сейчас. Твоя сила была получена от Дара Кошмара. И она может убить тебя, если её не обуздать."
    hide Lilith1

    scene poema12 with fade

    show Shade1 at right
    shade "Она говорит только половину правды, как всегда."
    shade "Приветствую, я Шейд. Ты должен научиться управлять своими тенями, Алекс. Без знаний они поглотят тебя, и ты станешь рабом Кошмара или монстром."
    hide Shade1

    show Alex1 at left
    alex "Подождите, что ты, что она, знаете, что для меня лучше... Но зачем вам это? Почему вы хотите мне помочь?"
    hide Alex1

    scene poema13 with fade

    show Shade1 at right
    shade "Потому что я видел, как эти силы разрушали миры. Ты должен выжить, чтобы сделать выбор, который они не сделали."
    hide Shade1

    show Lilith1 at right
    lilith "Или ты можешь последовать за мной, Алекс. Я покажу тебе, как использовать свою силу так, чтобы не стать пешкой ни теней, ни их Создателей."
    hide Lilith1

    narrator "Лилит и Шейд протягивают свои руки, чтобы помочь встать на ноги Алексу. Какую руку помощи вы выберете?"

    menu:
        "Пойти с Лилит":
            jump lilith_path

        "Остаться с Шейдом":
            jump shade_path
    return

label lilith_path:
    scene poema14 with fade

    show Lilith1 at right
    lilith "Хорошо, что ты выбрал меня, а не безумца Шейда с его экспериментами над монстрами."
    lilith "Сейчас мы пойдём на рынок, чтобы ты подумал, что нам делать дальше."
    hide Lilith1

    narrator "Сумеречный Базар."

    scene poema15 with fade

    show Alex1 at left
    alex "Так это... Сумеречный Базар? Но что это за место? Оно... живое. Я чувствую, как всё вокруг шепчет. Или это просто мои мысли?"
    hide Alex1

    show Lilith1 at right
    lilith "Твои чувства не обманывают тебя. Этот рынок — не просто место, это переплетение миров."
    lilith "Каждая лавка, каждый торговец, каждый предмет здесь несёт в себе больше, чем кажется. Но будь осторожен, Алекс."
    lilith "Это место подчиняется своим законам. Здесь всё имеет свою цену, и иногда она может быть выше, чем ты готов заплатить."
    hide Lilith1

    show Alex1 at left
    alex "И что мне здесь делать? Я потерян. Этот мир... он пугает меня. Почему ты решила привести меня сюда?"
    hide Alex1

    show Lilith1 at right
    lilith "Потому что ты стоишь на пороге перемен, Алекс. Ты получил силу, которая может стать твоим благословением или проклятием."
    lilith "Я привела тебя сюда, чтобы ты мог сделать свой первый выбор. Сумеречный Базар предлагает три пути."
    lilith "Первый путь — путь силы. Ты можешь приобрести артефакты, которые мгновенно усилят тебя. Но сила без опыта может стать опасной."
    lilith "Второй путь — знания. Здесь хранятся древние тайны, которые раскроют перед тобой суть этого мира. Но знания могут быть тяжёлым бременем."
    lilith "И, наконец, третий путь — независимость. Ты можешь отказаться от помощи и попробовать справиться сам. Это путь самых храбрых... или самых безрассудных."
    hide Lilith1

    show Alex1 at left
    alex "И какой путь ты советуешь мне выбрать? Ты ведь, кажется, знаешь этот мир лучше, чем кто-либо ещё."
    hide Alex1

    show Lilith1 at right
    lilith "Я знаю этот мир, Алекс. И я знаю цену каждого пути. Но советов я не даю. Этот выбор принадлежит только тебе."
    lilith "Я могу лишь направить тебя, но идти по выбранному пути придётся тебе самому."
    hide Lilith1

    menu:
        "Путь силы: Купить артефакт":
            jump buy_artifact

        "Путь знаний: Узнать секреты мира":
            jump seek_secrets

        "Путь независимости: Отказаться от помощи":
            jump independent_path

    return


##############################################################################
# ОСНОВНОЙ СЮЖЕТ
##############################################################################


label buy_artifact:
    scene poema16 with fade

    show Alex1 at left
    alex "Если этот путь даст мне силу, чтобы выжить в этом мире, то я готов рискнуть."
    hide Alex1

    show Lilith1 at right
    lilith "Тогда иди за мной. Я покажу тебе лавку, где сила продаётся тем, кто готов за неё заплатить."
    hide Lilith1

    scene poema19 with fade

    show Lilith1 at right
    lilith "Это Торговец Макс. Он известен своей жадностью, но товары у него первоклассные."
    hide Lilith1

    show Max_merchant1 at right
    max_merchant "Добро пожаловать, странник. Ты пришёл в поисках силы, не так ли?"
    max_merchant "Здесь у меня всё, что нужно, от клинков, которые разрубают тьму, до амулетов, защищающих от её чар. Чем могу помочь?"
    hide Max_merchant1

    show Alex1 at left
    alex "А если я ошибусь в выборе? Что тогда?"
    hide Alex1

    show Lilith1 at right
    lilith "Ошибки — это часть пути. Но я скажу тебе одно, Алекс: любой выбор лучше, чем бездействие."
    hide Lilith1

    show Alex1 at left
    alex "Я хочу пройти испытание меча."
    hide Alex1

    show Max_merchant1 at right
    max_merchant "Что же, ваше решение вполне разумно, желаю вам удачи в битве."
    hide Max_merchant1

    scene poema20 with fade

    narrator "Алекса перемещают на платформу, где огромный монстр-медведь сразу же побежал на Алекса."

    menu:
        "Атаковать монстра":
            jump battle_minigame

    return

##############################################################################
# КЛАССЫ И ПЕРЕМЕННЫЕ ДЛЯ МИНИ-ИГРЫ
##############################################################################
init python:
    persistent.battle_completed = False
    import random

    # Размер экрана 1920×1080 (логика мини-игры)
    SCREEN_W = 1920
    SCREEN_H = 1080

    class Player(object):
        def __init__(self, x, y, size=30, speed=8):
            self.x = x
            self.y = y
            self.size = size      # Размер квадрата игрока
            self.speed = speed    # "Шаг" за одно нажатие клавиши

        def move_left(self):
            self.x -= self.speed
            self.x = max(0, self.x)  # Ограничение слева

        def move_right(self):
            self.x += self.speed
            self.x = min(SCREEN_W - self.size, self.x)  # Ограничение справа

        def move_up(self):
            self.y -= self.speed
            self.y = max(0, self.y)  # Ограничение сверху

        def move_down(self):
            self.y += self.speed
            self.y = min(SCREEN_H - self.size, self.y)  # Ограничение снизу

        def get_rect(self):
            return (self.x, self.y, self.x + self.size, self.y + self.size)

    class Bullet(object):
        def __init__(self, x, y, size=20, speed=5, direction="top_down"):
            """
            direction может быть:
            "top_down", "bottom_up", "left_right", "right_left".
            """
            self.x = x
            self.y = y
            self.size = size
            self.speed = speed
            self.direction = direction

        def update(self):
            if self.direction == "top_down":
                self.y += self.speed
            elif self.direction == "bottom_up":
                self.y -= self.speed
            elif self.direction == "left_right":
                self.x += self.speed
            elif self.direction == "right_left":
                self.x -= self.speed

        def get_rect(self):
            return (self.x, self.y, self.x + self.size, self.y + self.size)

    # Глобальные переменные
    player = None
    bullets = []
    game_time = 0.0
    game_over = False

    def check_collision(rect1, rect2):
        """
        Проверяем пересечение двух прямоугольников.
        rect: (x1, y1, x2, y2)
        """
        return not (rect1[2] < rect2[0] or 
                    rect1[0] > rect2[2] or 
                    rect1[3] < rect2[1] or
                    rect1[1] > rect2[3])

    def spawn_bullets():
        global bullets

        spawn_type = random.choice(["single", "triple"])
        # Выбираем направление
        direction = random.choice(["top_down", "bottom_up", "left_right", "right_left"])

        if spawn_type == "single":
            # Спавним 1 пулю
            x, y = get_initial_position(direction)
            bullet = Bullet(x, y, size=20, speed=8, direction=direction)
            bullets.append(bullet)
        else:
            # Спавним 3 пули в небольшом ряду/разбросе
            # Пример: если летят сверху вниз, двигаем x.
            #         если летят слева направо, двигаем y.
            base_x, base_y = get_initial_position(direction)

            # Шаг между пулями (зависит от направления)
            offset = 30

            for i in range(3):
                if direction in ["top_down", "bottom_up"]:
                    # Смещаем по оси X
                    x = base_x + i * offset
                    y = base_y
                else:
                    # Смещаем по оси Y
                    x = base_x
                    y = base_y + i * offset

                bullet = Bullet(x, y, size=20, speed=5, direction=direction)
                bullets.append(bullet)

    def get_initial_position(direction):
        """
        В зависимости от направления, возвращаем начальные координаты (x, y).
        
        top_down:    (x=random,  y чуть выше экрана)
        bottom_up:   (x=random,  y чуть ниже экрана)
        left_right:  (x чуть левее экрана, y=random)
        right_left:  (x чуть правее экрана, y=random)
        """
        if direction == "top_down":
            # Появляется вверху (y < 0)
            x = random.randint(0, SCREEN_W - 20)
            y = -40
        elif direction == "bottom_up":
            # Появляется внизу (y > SCREEN_H)
            x = random.randint(0, SCREEN_W - 20)
            y = SCREEN_H + 40
        elif direction == "left_right":
            # Появляется слева (x < 0)
            x = -40
            y = random.randint(0, SCREEN_H - 20)
        else:  # "right_left"
            # Появляется справа (x > SCREEN_W)
            x = SCREEN_W + 40
            y = random.randint(0, SCREEN_H - 20)
        return (x, y)

    def bullet_out_of_screen(b):
        """
        Возвращает True, если пуля b ушла за границы экрана.
        Для top_down:     если b.y > SCREEN_H
        Для bottom_up:    если b.y + b.size < 0
        Для left_right:   если b.x > SCREEN_W
        Для right_left:   если b.x + b.size < 0
        """
        if b.direction == "top_down":
            return b.y > SCREEN_H
        elif b.direction == "bottom_up":
            return b.y + b.size < 0
        elif b.direction == "left_right":
            return b.x > SCREEN_W
        elif b.direction == "right_left":
            return b.x + b.size < 0
        else:
            return False

    def update_minigame():
        # Обновляем логику мини-игры в новом контексте
        renpy.call_in_new_context("minigame_update")

##############################################################################
# ЭКРАН МИНИ-ИГРЫ
##############################################################################

screen bullet_hell():
    # Фон 1920×1080 (должен лежать в папке game/)
    add "minigame_background.jpg"

    # Игрок (красный квадрат)
    add Solid((255, 0, 0, 255)):
        xpos player.x
        ypos player.y
        size (player.size, player.size)

    # Пули (зелёные квадраты)
    for b in bullets:
        add "05.png":
            xpos b.x
            ypos b.y
            size (b.size, b.size)
            rotate (80 if b.direction in ["left_right","right_left"] else 0)

    # Клавиши: один шаг движения по нажатию
    key "K_LEFT" action Function(player.move_left)
    key "K_RIGHT" action Function(player.move_right)
    key "K_UP" action Function(player.move_up)
    key "K_DOWN" action Function(player.move_down)

    # Таймер каждые 0.05 сек -> обновляем мини-игру
    timer 0.05 repeat True action Function(update_minigame)

##############################################################################
# ОБНОВЛЕНИЕ СОСТОЯНИЯ МИНИ-ИГРЫ
##############################################################################

label minigame_update:
    python:
        global game_time, game_over, bullets, player

        game_time += 0.05

        # С шансом ~7% на каждом "тике" спавним пулю (или три)
        if random.random() < 0.:
            spawn_bullets()

        # Двигаем все пули
        for b in bullets:
            b.update()

        # Проверяем выход за экран и коллизии
        new_bullets = []
        for b in bullets:
            if not bullet_out_of_screen(b):
                new_bullets.append(b)
                # Проверяем столкновение
                if check_collision(player.get_rect(), b.get_rect()):
                    game_over = True

        bullets = new_bullets

        # Ограничиваем движение игрока в 1920×1080 (уже обработано в методах move)
        # Дополнительная проверка на границы, если нужно
        if player.x < 0:
            player.x = 0
        if player.x + player.size > SCREEN_W:
            player.x = SCREEN_W - player.size
        if player.y < 0:
            player.y = 0
        if player.y + player.size > SCREEN_H:
            player.y = SCREEN_H - player.size

        # Проверяем проигрыш / победу
        if game_over:
            renpy.jump("defeat")
        elif game_time >= 30.0:
            renpy.jump("victory")

    return

##############################################################################
# ЗАПУСК МИНИ-ИГРЫ
##############################################################################

label battle_minigame:
    # Инициализация
    $ player = Player((SCREEN_W - 30)//2, (SCREEN_H - 30)//2, size=30, speed=8)
    $ bullets = []
    $ game_time = 0.0
    $ game_over = False

    # Показываем экран
    call screen bullet_hell

    return

##############################################################################
# СЦЕНЫ ПОБЕДЫ / ПОРАЖЕНИЯ
##############################################################################

label victory:
    scene poema21 with fade

    narrator "Твой клинок разрубает воздух с невероятной скоростью, и монстр рухнул замертво."

    show Alex1 at left
    alex "Я справился! Этот меч действительно мощный."
    hide Alex1

    show Lilith1 at right
    lilith "Впечатляюще, Алекс. Теперь ты готов к следующему шагу."
    hide Lilith1

    narrator "С громким рыком монстр рухнул на землю, и платформа заполнилась тишиной. Алекс стоял над его телом, тяжело дыша, но с гордостью в глазах."

    show Alex1 at left
    alex "Я... Я сделал это. Я победил. Этот меч... его сила невероятна."
    hide Alex1

    jump end_game

label defeat:
    scene poema22 with fade

    narrator "Монстр с рычанием бросается на тебя. Ты чувствуешь, как его когти врезаются в твои плечи, сбивая тебя с ног."
    narrator "Боль пронзает всё твоё тело, и ты понимаешь, что не сможешь подняться."

    show Alex1 at left
    alex "Нет... Я... ещё не готов. Это не может быть концом..."
    hide Alex1

    narrator "Твоё тело падает на платформу. Холод теней обнимает тебя, унося последний отблеск жизни из твоих глаз."
    narrator "Вдали ты едва слышишь голос Лилит, но он уже не может удержать тебя."

    show Lilith1 at right
    lilith "Алекс... Ты был слишком молод, слишком неопытен. Этот мир забрал ещё одну душу, слишком рано, чтобы понять её силу."
    hide Lilith1

    narrator "Лилит смотрит на твоё безжизненное тело. Её лицо остаётся спокойным, но в глазах тлеет искра скорби."
    narrator "Она уходит, оставляя твоё тело в тенях. Но на этом история не заканчивается..."

    jump end_game2

label end_game:
    scene poema23 with fade

    show Lilith1 at right
    lilith "Не только меч, Алекс. Ты смог использовать его силу, потому что нашёл её в себе."
    lilith "Не каждый, кто берёт оружие в руки, может выстоять против такого врага. Ты доказал, что достоин быть здесь."
    hide Lilith1

    show Alex1 at left
    alex "Достоин? Я даже не знаю, что это значит в этом месте. Но эта победа... она что-то значит для меня. Впервые я почувствовал, что у меня есть шанс."
    hide Alex1

    show Lilith1 at right
    lilith "Ты сделал первый шаг, Алекс. Но впереди ещё много преград. Этот мир не простит ошибок, но теперь у тебя есть всё, чтобы выжить."
    hide Lilith1

    show Alex1 at left
    alex "Звучит так, будто ты хочешь меня чему-то научить. Почему? Почему ты хочешь мне помочь?"
    hide Alex1

    show Lilith1 at right
    lilith "Ты — редкий случай. Я вижу в тебе нечто большее, чем просто уцелевшего. Я вижу того, кто может изменить этот мир. И, быть может... быть может, я хочу быть рядом, когда это случится."
    hide Lilith1

    show Alex1 at left
    alex "Ты действительно веришь в меня? После всего, что я пережил, это звучит странно. Но я думаю... я думаю, мне это нужно."
    hide Alex1

    show Lilith1 at right
    lilith "Тогда давай заключим сделку, Алекс. Я помогу тебе раскрыть твой потенциал. Я буду твоим проводником в этом мире. Но взамен... я хочу быть частью твоей судьбы."
    hide Lilith1

    show Alex1 at left
    alex "Сделка заключена. Вместе мы справимся. Ты и я."
    hide Alex1

    narrator "Так начался новый этап в пути Алекса. Он обретал не только силу, но и спутницу, готовую идти с ним до конца. Их союз становился крепче с каждым шагом, и вместе они были готовы бросить вызов теням этого мира."

    $ renpy.movie_cutscene("poema33.webm")
    $ persistent.battle_completed = True
    $ renpy.full_restart()

label end_game2:
    scene poema25 with fade

    narrator "Спустя много времени Лилит возвращается на место твоей гибели. Платформа теперь поросла чёрными цветами, питающимися магией теней."

    show Lilith1 at right
    lilith "Я знала, что ты не справишься. Но всё же надеялась... Ты был другим. Особенным."
    hide Lilith1

    narrator "Она опускается на колени, касаясь земли, под которой покоятся остатки твоей сущности."

    show Lilith1 at right
    lilith "Возможно, ты был лучшим из нас. Возможно, этот мир мог измениться благодаря тебе... Но теперь это уже не важно."
    hide Lilith1

    narrator "Её голос срывается. Она долго сидит молча, наблюдая, как тени играют вокруг неё."
    narrator "Наконец, Лилит встаёт, утирая слёзы, которые она не позволяет никому видеть, и уходит, оставляя твою могилу охранять тени."

    scene poema24 with fade

    narrator "Ты погиб, но твоя история продолжает жить в воспоминаниях тех, кто видел твою попытку изменить этот мир."

    $ renpy.movie_cutscene("poema34.webm")
    $ persistent.battle_completed = True
    $ renpy.full_restart()
    

# Ветка 1.1.2 Путь знаний: Узнать секреты мира
label seek_secrets:
    scene poema17 with fade

    show Alex1 at left
    alex "Я выбрал путь знаний. Мне нужно понять этот мир, чтобы найти свой путь."
    hide Alex1

    show Lilith1 at right
    lilith "Мудрое решение, Алекс. Знание — это сила, но оно также может быть тяжёлым бременем."
    lilith "Мы направимся в Храм Знаний, где хранятся древние тайны этого мира."
    hide Lilith1

    scene poema26 with fade

    narrator "Лилит ведёт Алекса через извилистые улочки, пока они не достигают величественного храма, украшенного символами древних цивилизаций."

    show Crystal at right
    crystal "Добро пожаловать, искатель истины. Я — Кристалл-архивариус. Здесь ты найдёшь ответы на свои вопросы."
    hide Crystal

    show Alex1 at left
    alex "Спасибо. Я готов учиться и постигать секреты этого мира."
    hide Alex1

    show Crystal at right
    crystal "Тогда начнём с основ. Позволь мне показать тебе хроники этого места и тех, кто пытался изменить его судьбу."
    hide Crystal

    scene poema27 with fade

    narrator "Кристалл-архивариус открывает перед Алексом свиток знаний, наполненный древними письменами и изображениями."

    show Alex1 at left
    alex "Это невероятно... Я чувствую, как знания наполняют моё сознание."
    hide Alex1

    show Lilith1 at right
    lilith "Теперь, когда ты получил доступ к этим тайнам, пришло время установить связь с Дарами Кошмара. Это позволит тебе использовать полученные знания."
    hide Lilith1

    jump connection_dar

label connection_dar:
    scene poema28 with fade

    narrator "Лилит проводит ритуал, призывая Дар Кошмара. Тёмная энергия наполняет пространство вокруг Алекса."

    show ZK1 at right
    zk "Алекс, ты готов принять то, что тебе предстоит?"
    hide ZK1

    show Alex1 at left
    alex "Да, я готов. Я стремлюсь понять и изменить этот мир."
    hide Alex1

    narrator "Дар Кошмара протягивает руку, предлагая Эмбрион — источник великой силы и знания."

    menu:
        "Принять Эмбрион от Дара Кошмара":
            $ result = random_event(success_rate=0.5, success_label="success_end", failure_label="failure_end")

        "Отказаться от предложения":
            jump failure_end 

    return

label success_end:
    scene poema29 with fade

    show ZK1 at right
    zk "Ты сделал правильный выбор, Алекс. Этот Эмбрион усилит тебя и позволит достичь божественного уровня."
    hide ZK1

    narrator "Энергия Эмбриона проникает в тело Алекса, трансформируя его сущность."

    show ZK1 at right
    zk "Теперь ты и я — боги этого мира. Вместе мы будем управлять его судьбой."
    hide ZK1

    narrator "Лилит наблюдает за трансформацией, понимая, что её роль изменилась."

    show Lilith1 at right
    lilith "Я буду вашим посредником между существами и вами, новыми правителями этого мира. Пусть наше сотрудничество принесёт гармонию и порядок."
    hide Lilith1

    narrator "Алекс и Дар Кошмара обретали божественную силу, готовые вести мир к новой эре. Лилит осталась рядом, поддерживая баланс между тьмой и светом."

    $ renpy.movie_cutscene("poema32.webm")
    return

label failure_end:
    scene poema30 with fade

    show ZK1 at right
    zk "Ты слишком много знаешь, Алекс. Это угрожает балансу этого мира."
    hide ZK1

    narrator "Дар Кошмара атакует Алекса, его сила оказывается слишком великой для смертного."

    show Alex1 at left
    alex "Нет... Это не может быть концом..."
    hide Alex1

    narrator "Твоё тело падает на платформу. Холод теней обнимает тебя, унося последний отблеск жизни из твоих глаз."

    show Lilith1 at right
    lilith "Прощай, Алекс. Возможно, когда-нибудь наши пути пересекутся снова."
    hide Lilith1

    narrator "Лилит исчезает в густых болотах, её судьба остаётся неизвестной. Легенды гласят, что она однажды встретила Дар Кошмара, но её истинная роль остаётся тайной."

    $ renpy.movie_cutscene("poema31.webm")
    return

# Ветка 1.3 Путь независимости: Отказаться от помощи
label independent_path:
    scene poema18 with fade

    show Alex1 at left
    alex "Я решил не полагаться на чужую помощь. Я справлюсь сам."
    hide Alex1

    narrator "Алекс отказывается от предложения Лилит и решает идти своим путём."

    narrator "По пути он наталкивается на лагерь бандитов."

    jump meet_bandits

label meet_bandits:
    scene poema37 with fade

    narrator "Лагерь бандитов выглядит агрессивно. В центре стоит Главарь, который замечает приближающегося Алекса."

    show Chaser1 at right
    chaser "Кто ты такой, что вторгаешься на нашу территорию?"
    hide Chaser1

    show Alex1 at left
    alex "Я не ищу проблем, но если ты настаиваешь, я не отступлю."
    hide Alex1

    show Chaser1 at right
    chaser "Хорошо, если ты действительно не боишься, предлагаю дуэль. Если победишь, мы уйдём и больше не будем тебе мешать. Если проиграешь, станешь одним из нас."
    hide Chaser1

    menu:
        "Принять вызов на дуэль":
            jump duel_challenge

        "Отказаться и попытаться убежать":
            jump duel_challenge

    return

label duel_challenge:
    scene poema38 with fade

    narrator "Главарь поднимает свой меч, и начинается дуэль."

    menu:
        "Атаковать Главаря":
            $ result = random_event(success_rate=0.5, success_label="duel_victory", failure_label="duel_defeat")

    return

label duel_victory:
    scene poema39 with fade

    narrator "Твой удар оказался точным. Главарь падает, и лагерь бандитов поражён твоим мастерством."

    show Alex1 at left
    alex "Я доказал свою силу. Теперь я могу помочь вам и этим людям."
    hide Alex1

    narrator "Бандиты, впечатлённые твоей победой, решают присоединиться к тебе."

    narrator "Вместе вы реорганизуете лагерь, превращая его в безопасное поселение для попаданцев."

    narrator "Алекс стал лидером этого нового сообщества, обеспечивая защиту и процветание для всех его членов."

    jump end_game3

label duel_defeat:
    scene poema40 with fade

    narrator "Главарь уверенно отбивает твою атаку и наносит решающий удар."

    narrator "Ты чувствуешь, как сила покидает тебя, и осознаёшь, что проиграл."

    narrator "Главарь заканчивает твою жизнь, оставляя лагерь бандитов без лидера."

    show Lilith1 at right
    narrator "Лилит, которая наблюдала за происходящим, пытается спасти тебя, но её также убивают."
    hide Lilith1

    narrator "Теперь лагерь бандитов находится под властью жестокого нового лидера, а судьба Лилит остаётся неизвестной."

    jump end_game4

label end_game3:
    scene poema41 with fade

    narrator "С реорганизацией лагеря начинается новая эра. Поселение процветает, привлекая новых попаданцев, ищущих убежище и защиту."

    narrator "Алекс становится уважаемым лидером, чьи решения приносят мир и порядок в этот хаотичный мир."

    show Lilith1 at right
    narrator "Лилит остаётся рядом, помогая поддерживать баланс и направлять развитие поселения."
    hide Lilith1

    narrator "Так началась новая глава в истории этого мира, где сила, знание и независимость нашли своё равновесие."

    $ renpy.movie_cutscene("poema35.webm")

    return

label end_game4:
    scene poema42 with fade

    narrator "Смерть Алекса стала трагическим концом его пути. Лилит, потерявшегося без его поддержки, оказывается в опасности."

    show Lilith1 at right
    narrator "Бандиты убивают Лилит, не оставляя ей шансов на спасение."
    hide Lilith1

    narrator "Алекс погиб, но его попытка изменить мир оставила след в легендах и воспоминаниях тех, кто знал о его пути."

    $ renpy.movie_cutscene("poema36.webm")

    return


# Ветка 1.1.1: Путь Шейда — Обучение у Шейда
label shade_path:
    scene poema45 with fade

    show Alex1 at left
    alex "Хорошо... Я выбираю путь теней. Если эти силы родились из кошмара, то я хочу понять их глубже."
    hide Alex1

    show Shade1 at right
    shade "Мудрое решение, Алекс. Если ты хочешь выжить в этом мире, тебе придётся научиться играть по его правилам."
    shade "Следуй за мной. Я покажу тебе Храм Теней — святилище, где даже тьма обретает форму и волю."
    hide Shade1

    narrator "Шейд указывает Алексу идти вслед за ним, и они отправляются вглубь долины теней."

    jump shadow_temple

label shadow_temple:
    scene poema46 with fade

    narrator "Храм Теней возвышается посреди растрескавшейся земли. Мрачные статуи, словно воплощения кошмаров, смотрят пустыми глазами на пришедших."

    show Shade1 at right
    shade "Добро пожаловать в сердце тени. Это место таит в себе знания, способные как спасти твою душу, так и погубить её."
    shade "Ты можешь принять моё наставничество и научиться использовать тьму себе на благо..."
    shade "Или отказаться от него, но тогда последствия будут целиком на твоей совести."
    hide Shade1

    show Alex1 at left
    alex "И что, если я соглашусь на твоё обучение?"
    hide Alex1

    show Shade1 at right
    shade "Тогда твои силы возрастут. Но в то же время тебе придётся быть готовым к тяжёлым испытаниям, которые поглотили уже многих."
    hide Shade1

    menu:
        "Принять наставничество Шейда":
            jump accept_mentorship

        "Отказаться от наставничества Шейда":
            jump refuse_mentorship

label accept_mentorship:
    scene poema47 with fade

    show Alex1 at left
    alex "Я принимаю твои условия. Мне нужна сила, чтобы выжить и понять этот мир."
    hide Alex1

    show Shade1 at right
    shade "Решение принято. Твоё обучение начнётся немедленно."
    shade "Приготовься к тому, что мрак не всегда поддаётся контролю. Тебе придётся бороться не только с врагами снаружи, но и с собственными страхами."
    hide Shade1

    narrator "С этого момента Алекс начинает тренировки под руководством Шейда, изучая тайны управления тенями."

    jump master_student_relationship

label master_student_relationship:
    scene poema48 with fade

    narrator "Проходят недели, полные изнурительных тренировок. Алекс повторяет одни и те же приёмы снова и снова, ощущая, как тьма в нём растёт и подчиняется его воле."

    show Alex1 at left
    alex "Невероятно... Раньше я и не подозревал, на что способна тень. Но отчего же я постоянно чувствую холод, словно она вытягивает из меня тепло?"
    hide Alex1

    show Shade1 at right
    shade "Тьма всегда требует плату. Иногда эту цену мы замечаем не сразу. Но поверь мне, Алекс, скоро ты поймёшь, что без жертв ничего не достигается."
    shade "Когда почувствуешь, что готов — мы проведём ритуал. Это окончательно укрепит твою связь с тенью и выведет твои способности на новый уровень."
    hide Shade1

    narrator "Алекс не знает, к чему приведёт его дальнейший путь, но решимость в его глазах говорит сама за себя."

    jump deal_with_darkness

label deal_with_darkness:
    scene poema49 with fade

    narrator "Наконец, Шейд говорит, что настало время ритуала. В глубине Храма Теней они находят алтарь, окружённый мерцающими призрачными факелами."

    show Shade1 at right
    shade "Этот ритуал свяжет нас ещё крепче. Если ты действительно готов к силе теней, то позволь мне проникнуть в твоё сознание..."
    shade "И, в свою очередь, я впущу тебя в своё. Мы сможем объединить силы, став куда мощнее, чем по отдельности."
    hide Shade1

    show Alex1 at left
    alex "Но что будет со мной после этого? С моей личностью?"
    hide Alex1

    show Shade1 at right
    shade "Всё зависит от твоей воли, Алекс. В темноте легко потерять себя... или обрести истинное «я»."
    hide Shade1

    narrator "Шейд протягивает руку Алексу, приглашая к ритуалу. Тени сгущаются вокруг них."

    menu:
        "Заключить сделку с тьмой":
            $ random_event(success_rate=0.5, success_label="success_end_shade_monster", failure_label="failure_end_shade_monster")

        "Отказаться от сделки":
            jump refuse_deal_darkness

label success_end_shade_monster:
    scene poema50 with fade

    narrator "Тени оплетают Алекса и Шейда, сливая их воедино. Их тела начинают искажаться и трансформироваться."

    show Shade1 at right
    shade "Алекс... Я чувствую, как наша сила возрождается... Мы теперь одно существо."
    hide Shade1

    show Alex1 at left
    alex "Наш разум... наши желания... Всё... ОДНО..."
    hide Alex1

    narrator "Из алтаря поднимается чудовище с двумя головами — в одной мерцает сознание Алекса, в другой слышится холодный шёпот Шейда."
    narrator "С этого дня они обитают в глубинах пещеры недалеко от Храма, заманивая путников во тьму и питаясь их страхами и плотью."

    narrator "Люди, случайно оказавшиеся рядом, рассказывают о двухголовом монстре, который бродит в ночи и ищет новые жертвы."

    return

label failure_end_shade_monster:
    scene poema51 with fade

    narrator "Во время ритуала Алекс чувствует, что тьма Шейда перетягивает одеяло на себя."

    show Alex1 at left
    alex "Нет... Что происходит? Шейд, не так же мы договаривались..."
    hide Alex1

    show Shade1 at right
    shade "Ты оказался слабее, чем я думал. Теперь твоя душа — часть меня, а твоя воля сломлена."
    hide Shade1

    narrator "Шейд преобразуется в чудовищного монстра. Слияние проходит, но разум Алекса исчезает в глубинах сознания, полностью захваченный волей Шейда."
    narrator "Этот монстр становится марионеткой самого Кошмара, неся смерть и разрушение всем, кто осмелится встать у него на пути."

    return

label refuse_deal_darkness:
    scene poema52 with fade

    show Alex1 at left
    alex "Прости, Шейд, но я не готов. Мне не нравится эта полная зависимость от тьмы."
    hide Alex1

    show Shade1 at right
    shade "Глупец... Ты не понимаешь, что теряешь. Без этого ритуала ты никогда не достигнешь истинной силы!"
    hide Shade1

    narrator "Шейд мгновенно переходит в атаку, пока Алекс пытается осмыслить происходящее. Одним быстрым ударом Шейд пронзает сердце Алекса."

    show Alex1 at left
    alex "Шейд... Зачем...?"
    hide Alex1

    show Shade1 at right
    shade "Тени не прощают слабости. Твоё обучение было ошибкой — я потратил время впустую."
    hide Shade1

    narrator "Алекс падает без сил, и его кровь впитывается в алтарь. Последним, что он видит, — холодный взгляд Шейда, исчезающего в тьме."

    narrator "Так заканчивается путь Алекса в Мире Теней, прежде чем он успевает по-настоящему раскрыть свою силу."

    return

label refuse_mentorship:
    scene poema53 with fade

    show Alex1 at left
    alex "Извини, но я не могу доверять тебе настолько, чтобы стать твоим учеником. Я выберу иной путь."
    hide Alex1

    show Shade1 at right
    shade "Ты даже не представляешь, насколько это плохая идея."
    hide Shade1

    narrator "Шейд резко поворачивается к Алексу и наносит удар, наполненный тёмной энергией. Алекс не успевает защититься."

    show Alex1 at left
    alex "А-а... слишком... быстро..."
    hide Alex1

    show Shade1 at right
    shade "Жаль, Алекс. Тени забирают тех, кто отвергает их силу."
    hide Shade1

    narrator "Алекс оседает на землю, а Шейд уходит прочь, оставляя его умирать среди руин Храма Теней."

    return



###############################################################################
# ВЕТКА "ПУТЬ КРИСТАЛЛОВ"
###############################################################################

label arrow_crystal:
    scene poema54 with fade

    show Alex1 at left
    alex "Я выбрал Путь Кристаллов. Если сияние этой силы способно рассеять мрак, я готов идти за тобой, Аврора."
    hide Alex1

    show Aurora1 at right
    aurora "Ты принял непростое решение, Алекс. Воспользоваться силой Кристаллов — значит принять на себя огромную ответственность."
    aurora "Тебе предстоит многое узнать об Ордене и его истории. Не всё так однозначно, как кажется на первый взгляд. Следуй за мной в Храм Кристаллов."
    hide Aurora1

    narrator "Взгляд Авроры полон скрытой тревоги. Алекс замечает, что даже её уверенная поступь слегка замедляется, будто она вспоминает нечто тягостное. Несмотря на сомнения, он решается продолжить путь."

    jump crystal_temple

label crystal_temple:
    scene poema55 with fade

    narrator "Перед глазами Алекса величественно возвышается Храм Кристаллов. Его сверкающие колонны отражают солнечные лучи, а стены словно живые, пропитанные чистой энергией."

    show Alex1 at left
    alex "Невероятно… Я даже не представлял, что подобное место может существовать."
    hide Alex1

    show Aurora1 at right
    aurora "Здесь, в этом священном зале, принимаются решения, которые влияют на жизнь многих людей и существ, населивших этот мир."
    aurora "Но сейчас самое важное — понять, готов ли ты следовать за Ораденом. Некоторые считают его предводителем, несущим свет, а другие видят в его методах жестокость."
    hide Aurora1

    show Alex1 at left
    alex "Методы? Ты имеешь в виду, что он делает что-то незаконное или неправильное?"
    hide Alex1

    show Aurora1 at right
    aurora "Скажем так, иногда, чтобы защитить мир, он готов переступить через моральные принципы. Но выбор пути всегда за тобой."
    hide Aurora1

    narrator "Аврора обводит зал задумчивым взглядом и на мгновение умолкает. Алекс чувствует, что она борется с внутренними переживаниями."

    show Aurora1 at right
    aurora "Теперь у тебя есть два пути. Ты можешь проверить слова тех, кто сомневается в чистоте намерений Орадена, или же принести клятву и стать верным стражем Храма."
    hide Aurora1

    menu:
        "Сомневаться в Орадене":
            jump doubt_oraden
        "Поклясться в верности Ордену":
            jump oath_guardian

label doubt_oraden:
    scene poema56 with fade

    show Alex1 at left
    alex "Я не могу так просто отдать свою жизнь в руки тому, чьих истинных мотивов я не знаю. Я хочу узнать правду."
    hide Alex1

    show Aurora1 at right
    aurora "В таком случае тебе лучше обратиться к архивам. Там хранятся древние знания о том, откуда взялись Кристаллы и что связывает их с тем, чего мы боимся больше всего — Кошмаром."
    hide Aurora1

    show Alex1 at left
    alex "Но зачем скрывать эту информацию? Разве будет плохо, если все узнают правду?"
    hide Alex1

    show Aurora1 at right
    aurora "Иногда правда может подорвать доверие к Ордену, а значит, подорвать его силу. Ораден верит, что не все должны знать о тёмном источнике сил Кристаллов."
    hide Aurora1

    narrator "С этими словами Алекс уходит в полутёмный зал, где хранятся бесчисленные свитки, манускрипты и старинные книги. Пыль ложится на его одежду, пока он, склонившись над ветхими страницами, ищет ключи к пониманию тайны."

    show Alex1 at left
    alex "Вот оно… «Кристаллы были рождены из первородной энергии, которая некогда принадлежала Дару Кошмара…»"
    alex "Значит, свет, который я считал чистым, на самом деле связан с тьмой. И Орден использует эту силу."
    hide Alex1

    show Sapphire1 at right
    sapphire "Ты открыл глаза на истину, Алекс. Но помни: знание — лишь начало пути."
    hide Sapphire1

    show Alex1 at left
    alex "Ты… кто ты такая?"
    hide Alex1

    show Sapphire1 at right
    sapphire "Я Сапфир, архивариус. Я храню эти свитки от непрошеных глаз. Далеко не каждый, кто узнаёт правду, способен смириться с ней."
    sapphire "Мы боимся, что страх перед источником силы разрушит Орден изнутри. А если Орден падёт, Кошмар освободится."
    hide Sapphire1

    narrator "Сапфир исчезает в тени, но её слова остаются в голове Алекса. Он чувствует, как изнутри его начинает разъедать вопрос: действительно ли ради высшей цели можно скрывать столь важную правду?"

    jump meeting_kira

label oath_guardian:
    scene poema57 with fade

    show Alex1 at left
    alex "Я верю в призыв Ордена. Если мы хотим защитить мир от тьмы, то я готов принести клятву и стать стражем."
    hide Alex1

    show Aurora1 at right
    aurora "Тогда пройди испытание, которое покажет, насколько твой дух силён. Наша вера и кристальная энергия станут твоей опорой."
    hide Aurora1

    narrator "В течение нескольких дней Алекс подвергается различным тренировкам и проверкам. Он сражается с теневыми существами, которые пробиваются сквозь магические барьеры Храма."
    narrator "В одном из боёв он обнаруживает в себе способность к телекинезу: он невольно отбрасывает врагов в сторону, лишь сконцентрировавшись на Кристалле в своей руке."

    show Obsidian1 at right
    obsidian "Я наблюдал за тобой, Алекс. Твои способности проявляются с пугающей быстротой. Но помни: даже самый чистый свет может отбрасывать тёмную тень."
    hide Obsidian1

    show Alex1 at left
    alex "Кто ты?"
    hide Alex1

    show Obsidian1 at right
    obsidian "Я — Обсидиан, страж границы между нашим миром и пространством Кошмара. Я должен следить, чтобы ни одна из сторон не пересекла черту."
    obsidian "Чем сильнее ты становишься, тем глубже будет твоя тень."
    hide Obsidian1

    narrator "Слова Обсидиана звучат как предупреждение. Алекс понимает, что истинная сложность пути — не только победить тьму, но и не стать её частью."

    jump meeting_kira


label meeting_kira:

    scene poema58 with fade

    narrator "В саду Храма, среди разноцветных кристаллических деревьев, Алекс встречает девушку в доспехах, которая точит меч. У неё уверенный взгляд и решительные черты лица."

    show Kira1 at right
    kira "Ты — Алекс, верно? Новенький, о котором все говорят. Говорят, ты уже успел блеснуть на тренировках."
    hide Kira1

    show Alex1 at left
    alex "Да, хотя мне ещё многому нужно научиться. А ты… Кира, если не ошибаюсь?"
    hide Alex1

    show Kira1 at right
    kira "Всё верно. Я служу Ордену уже не первый год, но никогда не перестаю задавать вопросы. Мне кажется, что в наших рядах много неясностей."
    kira "Я тоже долго сомневалась, стоит ли идти против воли Орадена, ведь он ведёт нас к победе над тьмой. Но иногда у меня возникают подозрения, что эта победа может иметь слишком высокую цену."
    hide Kira1

    show Alex1 at left
    alex "Аврора говорила, что у меня есть выбор — довериться Орадену или усомниться в нём. Я до конца не понимаю, что происходит внутри Ордена."
    hide Alex1

    show Kira1 at right
    kira "И ты продолжала служить, несмотря на сомнения?"
    kira "Да, служила… но искала собственные ответы. Если хочешь, можем объединиться. Вдвоём проще докопаться до истины."
    hide Kira1

    menu:
        "Начать роман с Кирой":
            $ romance_with_kira = True
            jump kira_romance
        "Игнорировать Киру":
            $ romance_with_kira = False
            jump ignore_kira

label kira_romance:
    scene poema59 with fade

    show Alex1 at left
    alex "Мне нравится твой настрой. Вместе мы точно сможем разгадать все тайны Ордена и защитить его от любых угроз."
    hide Alex1

    show Kira1 at right
    kira "Я рада слышать это. Твои глаза горят любопытством, а сердце, кажется, жаждет справедливости. Мне это импонирует."
    hide Kira1

    narrator "Они обмениваются долгим взглядом, в котором чувствуется не просто боевое товарищество, но и пробуждающаяся близость. Возможно, это лишь начало их общей истории."

    jump dar_koshmara_path

label ignore_kira:
    scene poema59 with fade

    show Alex1 at left
    alex "Хорошее предложение, но сейчас я должен сам разобраться в происходящем. Иногда одиночество помогает сконцентрироваться."
    hide Alex1

    show Kira1 at right
    kira "Что ж, это твой выбор. Но если тебе понадобится помощь — просто скажи."
    hide Kira1

    narrator "Алекс отворачивается, чувствуя, что ему нужно время, чтобы самому всё осознать. Возможно, он лишается сильного союзника, но его решимость твёрже стали."

    jump dar_koshmara_path

label dar_koshmara_path:
    scene poema60 with fade

    narrator "Вскоре Алекс узнаёт о жутком месте, которое называют Даром Кошмара: там, согласно преданиям, берёт своё начало тёмная энергия, сдерживаемая барьерами Ордена."
    narrator "Если Кира присоединилась к Алексу (romance_with_kira = True), они идут туда вместе, а если нет, то Алекс отправляется один. Их цель — попытаться уничтожить источник тьмы или хотя бы ослабить его влияние."

    show Alex1 at left
    alex "Пейзаж здесь мрачен… Словно сама земля иссушена ужасом."
    hide Alex1

    if romance_with_kira:
        show Kira1 at right
        kira "Я чувствую холод, и он исходит не от погоды. Здесь словно каждый камень пропитан страхом."
        alex "Будь наготове. Если что-то пойдёт не так, отступаем и сообщаем в Храм."
        hide Kira1

    show Obsidian1 at right
    obsidian "Думаешь, так легко уничтожить корни самой тьмы? Твои способности велики, Алекс, но, возможно, этого недостаточно."
    hide Obsidian1

    show Alex1 at left
    alex "Обсидиан? Как ты здесь оказался? Я думал, ты остаёшься на границе."
    hide Alex1

    show Obsidian1 at right
    obsidian "Тень тоньше, чем ты предполагаешь. Я слежу, чтобы никто не пересёк опасную грань… Ни свет, ни тьма. И ты тоже."
    hide Obsidian1

    narrator "Слова Обсидиана звучат таинственно и немного пугающе, но Алекс не может позволить себе роскошь отступать."

    $ random_event(success_rate=0.5, success_label="dar_defeated", failure_label="dar_victory")
    return

label dar_defeated:
    scene poema61 with fade

    if romance_with_kira:
        show Kira1 at right
        kira "Мы сделали это! Я чувствую, как тьма отступает. Пусть и не навсегда, но мы дали миру передышку."
        alex "Спасибо, что была рядом, Кира. Без тебя я бы, возможно, не справился."
        hide Kira1
    else:
        show Alex1 at left
        alex "Кажется, тьма отступает… Я даже не верю, что в одиночку смог дойти до конца."
        hide Alex1

    narrator "Дар Кошмара повержен, и хотя Алекс видит, что остался шрам на земле, источающий остатки тьмы, он знает, что сделал всё возможное для защиты мира."

    jump alex_leader

label dar_victory:
    scene poema62 with fade

    show ZK1 at right
    zk "Глупцы… Вы думали, что сможете одолеть изначальную тьму? Дар Кошмара не так легко уничтожить."
    hide ZK1

    narrator "Силы тьмы стремительно окутывают всё вокруг. Алекс внезапно ощущает сковывающую слабость. Кристаллы меркнут, а шёпот ужаса заполняет воздух."

    if romance_with_kira:
        show Kira1 at right
        narrator "Кира кричит, пытаясь оттащить Алекса в безопасное место, но тьма опутывает её разум. Последнее, что Алекс видит — как её глаза затмевает безумная чёрная вспышка."
        hide Kira1
    else:
        show Alex1 at left
        narrator "Алекс чувствует, как его сознание поглощает бездна. Всё, что было дорогим, медленно растворяется во тьме."
        hide Alex1

    return


label alex_leader:
    scene poema63 with fade

    show Aurora1 at right
    aurora "Алекс, твои подвиги не остались незамеченными. Ты доказал, что можешь вести за собой людей и управлять силой Кристаллов так, чтобы не поддаться тьме."
    aurora "Отныне ты возглавишь Орден. Но помни, что это не только честь, но и ответственность, от которой нет обратного пути."
    hide Aurora1

    show Alex1 at left
    alex "Я сделаю всё, чтобы не повторить ошибок прошлого. Мы сохраним равновесие, каким бы трудным ни был путь."
    hide Alex1

    show Aurora1 at right
    aurora "Я верю в тебя. Ты не только сильный воин, но и человек, который умеет слышать других."
    hide Aurora1

    narrator "С этими словами Аврора склоняет голову в знак уважения. Члены Ордена признают Алекса своим новым лидером, возлагая на него надежды на долгожданный мир."

    jump dar_final_battle

label dar_final_battle:
    scene poema64 with fade

    narrator "Спустя время ходят слухи, что Дар Кошмара вновь набирает силу. Алекс, теперь уже в роли главы Ордена, мобилизует стражей и готовит решающее наступление."
    narrator "В назначенный час Алекс и его соратники встречаются лицом к лицу с воплощением Кошмара. Силы тьмы колышутся вокруг них, грозя уничтожить всё на своём пути."

    show Obsidian1 at right
    obsidian "Ты изменился, Алекс. В твоих глазах я вижу и свет, и тень. Это может стать твоим оружием… или погубить тебя."
    hide Obsidian1

    show Alex1 at left
    alex "Я научился на своих ошибках. Я знаю, что нельзя полностью уничтожить тьму, но можно удерживать её от поглощения всего живого."
    hide Alex1

    if romance_with_kira:
        show Kira1 at right
        kira "Мы сразимся вместе, Алекс. Я не позволю тьме забрать тебя… нас."
        hide Kira1

    $ random_event(success_rate=0.5, success_label="final_victory", failure_label="final_defeat")
    return

label final_victory:
    scene poema65 with fade

    show Alex1 at left
    alex "Достаточно. Мы оба — часть одного мира. Уничтожить тебя значит нарушить баланс, но я могу изгнать тебя туда, откуда тебе не так просто будет выбраться."
    hide Alex1

    show ZK1 at right
    zk "Ты мудр, Алекс, хотя я видел многие цивилизации, которые считали себя мудрыми…"
    hide ZK1

    show Alex1 at left
    alex "Исчезни. И помни: если вернёшься, мы будем готовы."
    hide Alex1

    narrator "Кристаллы вокруг начинают сиять ярче, формируя световой вихрь. Кошмар отступает, с отдалённым эхом зловещего смеха. Алекс понимает, что это не конец, но они выиграли время."

    if romance_with_kira:
        show Kira1 at right
        kira "Ты поступил правильно. Не всегда нужно уничтожать врага до основания — иногда достаточно вернуть его за грань дозволенного."
        hide Kira1

        show Alex1 at left
        alex "Согласен. Но мы остаёмся на стороже."
        hide Alex1

    narrator "Их имена вписываются в историю как тех, кто смог сдержать невиданную тьму, не утратив человеческого облика и сострадания."
    return

label final_defeat:
    scene poema66 with fade

    show Alex1 at left
    alex "Ты оставил слишком много ран на этом мире. Хватит! Я положу конец твоему влиянию раз и навсегда!"
    hide Alex1

    narrator "Мощная энергия Кристаллов срывается с рук Алекса. Вспышка света озаряет всё пространство, и Кошмар испускает предсмертный рёв."

    if romance_with_kira:
        show Kira1 at right
        kira "Алекс, берегись! Слишком много силы — это может разрушить тебя самого!"
        hide Kira1

        show Alex1 at left
        alex "Это цена, которую я готов заплатить… Прощай, Кошмар!"
        hide Alex1
    else:
        narrator "Тело Алекса объято слепящим светом. Он сознательно жертвует частичкой себя, чтобы обуздать чудовищную силу, уничтожая Кошмара."

    narrator "Когда свет гаснет, Кошмар растворяется в воздухе. Алекс тяжело дышит, и никто, кроме него, не знает, что ему пришлось пережить в тот миг. Но мир спасён."

    if romance_with_kira:
        show Kira1 at right
        kira "Ты жив? О, слава Кристаллам!"
        hide Kira1

        show Alex1 at left
        alex "Да… но я чувствую пустоту внутри. Как будто часть меня исчезла вместе с Кошмаром."
        hide Alex1

        show Kira1 at right
        kira "Ты герой, Алекс. И я буду рядом, чтобы помочь тебе найти себя заново."
        hide Kira1
    else:
        narrator "Алекс понимает, что отныне его жизнь никогда не будет прежней. Он чувствует на себе тяжесть огромной жертвы, но знает, что выбор был сделан ради мира."

    narrator "С тех пор имя Алекса, победителя Кошмара, живёт в легендах, вдохновляя новых стражей и напоминая о хрупком равновесии света и тьмы."
    return







