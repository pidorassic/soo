
    elif st.session_state.step == 6:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ВЕЧІР</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:12px;">🌙 19:00. Домашні завдання та відпочинок</div>'
            '<div style="font-size:18px;font-weight:500;color:#1a1a1a;line-height:1.6;margin-bottom:20px;">Увечері — час на домашнє завдання. Потім читання книжок або настільні ігри з родиною.</div>'
            '<div style="background:rgba(255,255,255,0.92);border-left:6px solid #333;padding:16px 22px;border-radius:6px;margin-bottom:20px;">'
            '<div style="font-size:17px;font-weight:700;color:#222;margin-bottom:8px;">🌙 Відбій</div>'
            '<div style="font-size:16px;color:#333;line-height:1.5;">Спати лягали рано — о 21:00–22:00.</div></div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:18px 24px;margin-bottom:14px;">'
            '<div class="lesson-title">📖 Домашнє завдання</div>'
            '<div class="lesson-text">Уроки готували за підручниками та зошитами. Писали пером — тому акуратність була дуже важливою. Іноді допомагали старші брати чи сестри.</div></div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:18px 24px;margin-bottom:14px;">'
            '<div class="lesson-title">📚 Читання книжок</div>'
            '<div class="lesson-text">У 60-х не було інтернету, а телевізор — не в кожній родині. Книжки були головним джерелом знань і розваг. Читали вголос, обговорювали прочитане.</div></div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:18px 24px;">'
            '<div class="lesson-title">📻 Радіо та настільні ігри</div>'
            '<div class="lesson-text">Ввечері по радіо транслювали концерти та радіовистави. А ще грали в шахи, шашки, доміно — всією родиною.</div></div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_6"):
                st.session_state.step = 5
                st.rerun()
        with c2:
            if st.button("🏠 На головну", key="home_btn_6"):
                st.session_state.step = 0
                st.rerun()
    elif st.session_state.step == 7:
        st.markdown('<div class="slide-title">ПОРІВНЯННЯ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:22px;">ПІОНЕРИ ТА СУЧАСНА МОЛОДЬ</div>'
            '<div style="font-size:18px;font-weight:500;color:#333;line-height:1.7;margin-bottom:20px;">Піонери 60-х та сучасна молодь жили в різних світах. Одні виховувались у колективі, де головним було спільне благо та дисципліна.</div>'
            '<div style="font-size:18px;font-weight:500;color:#333;line-height:1.7;">Інші — у світі, де цінується свобода вибору. Давайте порівняємо.</div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_7"):
                st.session_state.step = 0
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_7"):
                st.session_state.step = 8
                st.rerun()

    elif st.session_state.step == 8:
        st.markdown('<div class="slide-title">ПОРІВНЯННЯ · ПІОНЕРИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:22px;">✅ ЩО ХОРОШОГО БУЛО У ПІОНЕРІВ</div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:26px 30px;">'
            '<div style="font-size:18px;font-weight:500;color:#333;line-height:2.0;margin:0;">'
            '• <b>Дисципліна та відповідальність</b><br>'
            '• <b>Колективізм</b> — учили працювати в команді<br>'
            '• <b>Повага до старших</b><br>'
            '• <b>Фізичний розвиток</b> — спорт, походи<br>'
            '• <b>Участь у житті громади</b><br>'
            '• <b>Менше залежності від ґаджетів</b><br>'
            '• <b>Безкоштовні гуртки</b> — для всіх дітей'
            '</div></div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_8"):
                st.session_state.step = 7
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_8"):
                st.session_state.step = 9
                st.rerun()

    elif st.session_state.step == 9:
        st.markdown('<div class="slide-title">ПОРІВНЯННЯ · СУЧАСНА МОЛОДЬ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:22px;">🌟 ЩО ХОРОШОГО Є У СУЧАСНОЇ МОЛОДІ</div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:26px 30px;">'
            '<div style="font-size:18px;font-weight:500;color:#333;line-height:2.0;margin:0;">'
            '• <b>Свобода вибору</b><br>'
            '• <b>Доступ до знань</b> — інтернет<br>'
            '• <b>Толерантність</b><br>'
            '• <b>Технологічна грамотність</b><br>'
            '• <b>Креативність</b> — контент, проєкти<br>'
            '• <b>Підприємливість</b><br>'
            '• <b>Глобальна співпраця</b>'
            '</div></div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_9"):
                st.session_state.step = 8
                st.rerun()
        with c2:
            if st.button("🏠 На головну", key="home_btn_9"):
                st.session_state.step = 0
                st.rerun()

    elif st.session_state.step == 10:
        st.markdown('<div class="slide-title">МОДА ТА КУЛЬТУРА · МУЗИКА, КІНО, ІГРИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:22px;">🎵 Що слухали, дивилися та в що грали</div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;margin-bottom:14px;">'
            '<div class="lesson-title" style="font-size:18px;">🎸 Музика</div>'
            '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
            '• The Beatles, The Rolling Stones — світові хіти<br>'
            '• Радянська естрада — Муслим Магомаєв, Едіта П\'єха<br>'
            '• Пісні під гітару у дворі<br>'
            '• Радіо та вінілові платівки'
            '</div></div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;margin-bottom:14px;">'
            '<div class="lesson-title" style="font-size:18px;">🎬 Кіно</div>'
            '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
            '• «Я шагаю по Москве», «Операция Ы»<br>'
            '• «Кавказька полонянка», «Діамантова рука»<br>'
            '• Кінотеатри та літні майданчики'
            '</div></div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;">'
            '<div class="lesson-title" style="font-size:18px;">🎲 Ігри</div>'
            '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
            '• Класики, гумовий стрибок, піжмурки<br>'
            '• Футбол у дворі, велосипеди<br>'
            '• Шахи, шашки, настільні ігри'
            '</div></div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_10"):
                st.session_state.step = 9
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_10"):
                st.session_state.step = 11
                st.rerun()

    elif st.session_state.step == 11:
        st.markdown('<div class="slide-title">МОДА ТА КУЛЬТУРА · ОДЯГ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:22px;">👗 Як одягалися у 60-х</div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;margin-bottom:14px;">'
            '<div class="lesson-title" style="font-size:18px;">👔 Шкільна форма</div>'
            '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
            '• Дівчата — коричнева сукня з білим або чорним фартухом<br>'
            '• Хлопці — сорочка, брюки та піджак<br>'
            '• Білі комірці та манжети пришивали окремо'
            '</div></div>'
            '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;">'
            '<div class="lesson-title" style="font-size:18px;">👖 Повсякденний одяг</div>'
            '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
            '• Прості сукні та спідниці для дівчат<br>'
            '• Сорочки, светри, штани для хлопців<br>'
            '• Одяг шили або перешивали вдома'
            '</div></div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_11"):
                st.session_state.step = 10
                st.rerun()
        with c2:
            if st.button("🏠 На головну", key="home_btn_11"):
                st.session_state.step = 0
                st.rerun()
    elif st.session_state.step == 12:
        st.markdown('<div class="slide-title">ІНТЕРАКТИВ · ТЕСТ 1</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:18px;">🌅 РАНОК ПІОНЕРА</div>'
            '<div class="question-card">'
            '<b>Ситуація:</b> Дзвенить будильник о 07:00. Мама вже на кухні, по радіо грає мелодія для зарядки.<br><br>'
            '<b>Питання:</b> Що робитимеш?'
            '</div>',
            unsafe_allow_html=True
        )
        choice = st.radio(
            "Оберіть варіант:",
            [
                "А) Зроблю зарядку під радіо разом з родиною, потім — сніданок",
                "Б) Посплю ще 15 хвилин, потім швидко зберусь",
                "В) Відразу побіжу до школи без сніданку",
                "Г) Полежу в ліжку з телефоном"
            ],
            key="test1_choice",
            label_visibility="collapsed"
        )
        st.write("")
        if st.button("Зробити вибір", key="test1_btn"):
            if choice.startswith("А"):
                st.success("✅ **07:15.** Ти бадьорий, зробив зарядку, поснідав кашею. На уроці уважний і активний. **Ідеальний ранок піонера!**")
            elif choice.startswith("Б"):
                st.warning("⚠️ **07:15.** Ти схопився з ліжка, одягнувся нашвидкоруч, не встиг поснідати. На уроці думаєш про їжу, а не про математику.")
            elif choice.startswith("В"):
                st.error("❌ **07:05.** Ти вибіг з дому голодним. На третій годині живіт бурчить так, що чує весь клас. Вчителька робить зауваження.")
            elif choice.startswith("Г"):
                st.error("❌ **08:30.** Ти спізнився на перший урок! У 60-х телефону не було, але навіть якби був — урок пропущено. Класний керівник викликає батьків до школи.")
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_12"):
                st.session_state.step = 11
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_12"):
                st.session_state.step = 13
                st.rerun()

    elif st.session_state.step == 13:
        st.markdown('<div class="slide-title">ІНТЕРАКТИВ · ТЕСТ 2</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:18px;">📚 У ШКОЛІ</div>'
            '<div class="question-card">'
            '<b>Ситуація:</b> Учитель дав контрольну роботу. Треба написати твір на пів сторінки.<br><br>'
            '<b>Питання:</b> Чим будеш писати?'
            '</div>',
            unsafe_allow_html=True
        )
        choice = st.radio(
            "Оберіть варіант:",
            [
                "А) Кульковою ручкою",
                "Б) Олівцем",
                "В) Чорнильницею та ручкою з пером",
                "Г) Друкарською машинкою"
            ],
            key="test2_choice",
            label_visibility="collapsed"
        )
        st.write("")
        if st.button("Зробити вибір", key="test2_btn"):
            if choice.startswith("А"):
                st.error("❌ **Двійка.** У 60-х кулькові ручки були рідкістю, вчителька каже: «Це несерйозно, треба писати пером». Твір не зараховують.")
            elif choice.startswith("Б"):
                st.warning("⚠️ **Трійка.** Олівцевий текст виглядає блідо, а вчителька вимагає чорнило. Оцінку знижують за неохайність.")
            elif choice.startswith("В"):
                st.success("✅ **П'ятірка!** Ти акуратно вмочаєш перо в чорнильницю-непроливайку, пишеш рівні літери. За охайність — окрема похвала.")
            elif choice.startswith("Г"):
                st.error("❌ **Неможливо.** У школі 60-х друкарських машинок не було. Тебе висміють, а контрольну доведеться переписувати пером.")
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_13"):
                st.session_state.step = 12
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_13"):
                st.session_state.step = 14
                st.rerun()

    elif st.session_state.step == 14:
        st.markdown('<div class="slide-title">ІНТЕРАКТИВ · ТЕСТ 3</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:18px;">🎒 ПІСЛЯ УРОКІВ</div>'
            '<div class="question-card">'
            '<b>Ситуація:</b> Уроки закінчились о 14:00. Ти вдома, пообідав. Попереду — вільний час до вечері.<br><br>'
            '<b>Питання:</b> Що робитимеш?'
            '</div>',
            unsafe_allow_html=True
        )
        choice = st.radio(
            "Оберіть варіант:",
            [
                "А) Піду на збори загону, потім збір макулатури",
                "Б) Сидітиму вдома, гратиму в комп'ютерні ігри",
                "В) Піду на футбольне поле з друзями",
                "Г) Дивитимусь телевізор цілий вечір"
            ],
            key="test3_choice",
            label_visibility="collapsed"
        )
        st.write("")
        if st.button("Зробити вибір", key="test3_btn"):
            if choice.startswith("А"):
                st.success("✅ **Молодець!** Ти отримуєш подяку від класного керівника, а твій загін — перше місце за зібраний папір. Ти справжній піонер!")
            elif choice.startswith("Б"):
                st.error("❌ **Хибний шлях.** У 1960-х комп'ютерів вдома не було! А якби були — піонери не сиділи б за ними, а займалися суспільно корисними справами.")
            elif choice.startswith("В"):
                st.success("✅ **Добре!** Спортивна секція — це теж піонерська справа. Ти тренуєшся, а ввечері — весела гра у дворі.")
            elif choice.startswith("Г"):
                st.warning("⚠️ **Так собі.** Телевізор у 60-х був рідкістю, і дивитися його годинами вважалось неробством. Батьки кажуть: «Краще б книжку почитав!»")
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_14"):
                st.session_state.step = 13
                st.rerun()
        with c2:
            if st.button("🏠 На головну", key="home_btn_14"):
                st.session_state.step = 0
                st.rerun()

    elif st.session_state.step == 15:
        st.markdown(
            '<div style="text-align:center;font-size:42px;font-weight:900;color:#111;'
            'margin:30px 0 20px 0;letter-spacing:4px;">ДЯКУЄМО ЗА УВАГУ!</div>',
            unsafe_allow_html=True
        )
        try:
            with open("end.jpg", "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()
            st.markdown(
                '<div style="width:100%;display:flex;justify-content:center;align-items:center;margin:10px 0 20px 0;">'
                '<img src="data:image/jpeg;base64,' + img_b64 + '" '
                'style="max-height:50vh;max-width:100%;width:auto;border-radius:12px;display:block;">'
                '</div>',
                unsafe_allow_html=True
            )
        except Exception:
            st.markdown(
                '<div style="text-align:center;font-size:20px;color:#888;'
                'margin:40px 0;">Файл end.jpg не знайдено</div>',
                unsafe_allow_html=True
            )
        st.markdown(
            '<div style="text-align:center;font-size:20px;font-weight:600;color:#333;'
            'margin-top:10px;">Сподіваємося, вам сподобалася ця подорож у минуле!</div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("🏠 На головну", key="home_btn_15", use_container_width=True):
                st.session_state.step = 0
                st.rerun()
