import streamlit as st

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS: отступы сверху, убираем скролл и настраиваем стили
st.markdown(
    """
    <style>
    /* Принудительно убираем скроллбар, чтобы контент строго умещался на одном экране */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        height: 100vh !important;
    }

    .stApp {
        background-color: #ffffff;
        color: #000000;
        text-align: left !important;
    }
    
    div.block-container {
        background-color: #ffffff;
        max-width: 1250px !important;
        margin-left: 2rem !important;
        margin-right: auto !important;
        padding-top: 3rem !important; /* Отступ сверху от шапки браузера */
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
    }

    /* Элегантный плавный эффект: мягкое увеличение масштаба (zoom) и проявление */
    @keyframes scaleFadeTransition {
        0% {
            opacity: 0;
            transform: scale(0.95);
            filter: blur(4px);
        }
        100% {
            opacity: 1;
            transform: scale(1);
            filter: blur(0px);
        }
    }

    /* Применяем этот эффект ко всем элементам нового слайда */
    .element-container, .stMarkdown, .stRadio, .stImage, .stButton {
        animation: scaleFadeTransition 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .slide-title {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #111111 !important;
        margin-bottom: 15px !important;
        line-height: 1.3 !important;
        text-align: left !important;
    }

    /* Карточка для вопроса */
    .question-card {
        background-color: #f8f9fa;
        border-left: 6px solid #333333;
        padding: 20px 25px;
        border-radius: 6px;
        margin-bottom: 20px;
        font-size: 22px !important;
        font-weight: 600 !important;
        color: #111111 !important;
    }

    /* Увеличиваем размер и жирность основного текста */
    p, label, span, .stMarkdown {
        font-size: 20px !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
        text-align: left !important;
        color: #1a1a1a !important;
    }

    /* Стиль для ВСЕХ кнопок Streamlit с мягким откликом */
    .stButton > button {
        background-color: #e4e6eb !important;
        color: #000000 !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        border: 1px solid #ced4da !important;
        border-radius: 6px !important;
        padding: 0.4rem 1.2rem !important;
        transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }
    
    .stButton > button:hover {
        background-color: #d8dadf !important;
        color: #000000 !important;
        border-color: #adb5bd !important;
        transform: translateY(-2px);
    }

    .stButton > button:active {
        transform: translateY(1px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Инициализация шагов
if "step" not in st.session_state:
    st.session_state.step = 0

# Уникальный контейнер для анимации смены слайдов
with st.container(key=f"scale_box_{st.session_state.step}"):

    # Шаг 0: Приветствие от 10 "А" (Большое фото справа, текст слева, заполнено всё)
    if st.session_state.step == 0:
        col_left, col_right = st.columns([1, 1.2], gap="large")
        
        with col_left:
            st.markdown(
                """
                <div>
                    <div style="font-size: 34px; font-weight: 800; color: #111111; margin-bottom: 12px; line-height: 1.2;">
                        Вітаємо вас!<br>Проект підготовлено учнями 10 «А» класу.
                    </div>
                    <div style="font-size: 18px; font-weight: 500; color: #444444; line-height: 1.5;">
                        Запрошуємо вас здійснити захоплюючу подорож на кілька десятиліть назад. Ми пропонуємо поринути в атмосферу минулого століття та на власні очі побачити, яким було повсякденне життя підлітків у 60-х роках.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style="margin-top: 25px; padding: 15px 20px; background-color: #f8f9fa; border-left: 5px solid #555; border-radius: 4px;">
                    <div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 5px;">📌 Що на вас чекає у цій подорожі:</div>
                    <div style="font-size: 16px; color: #555; line-height: 1.4;">
                        • Ранкові звички та шкільна форма<br>
                        • Особливості навчання за чорнильницями<br>
                        • Інтерактивний тест на знання побуту 60-х років
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_right:
            # Увеличено фото и смещено правее за счет пропорций колонок
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=900&auto=format&fit=crop", width=620)
            
            st.write("")
            if st.button("Далі ➔", key="next_btn_0"):
                st.session_state.step += 1
                st.rerun()

    else:
        # Шаги 1-10 (Обычные слайды и тесты)
        if st.session_state.step == 1:
            st.markdown('<div class="slide-title">Ранок</div>', unsafe_allow_html=True)
            st.write("Кожен день радянського школяра у 60-х роках розпочинався дуже рано. Ще до того, як зійде сонце або лунала шкільна дзвінка пора, у квартирах лунала радіотрансляція з обов'язковою ранковою зарядкою. Одяг — виключно випрасувана форма, білі комірці та манжети, які пришивали окремо. Портфелі з цупкої шкіри збиралися суворо з вечора, а взуття ретельно начищалося до блиску.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=650)

        elif st.session_state.step == 2:
            st.markdown('<div class="slide-title">Уроки</div>', unsafe_allow_html=True)
            st.write("У навчальному процесі панувала сувора дисципліна та порядок. Школярі писали справжніми чорнильницами-непроливайками та дерев'яними ручками з металевими пером, що вимагало неабиякої акуратності, адже за помарочку в зошиті могли знизити оцінку. Жодних гаджетів чи калькуляторів — лише таблиця множення, логарифмічні лінійки, живі дискусії на перервах та дружні розмови біля стінгазет у коридорах.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=650)

        elif st.session_state.step == 3:
            st.markdown('<div class="slide-title">Позаурочний час</div>', unsafe_allow_html=True)
            st.write("Після завершення уроків життя школярів не зупинялося. Позаурочний час був сповнений колективної праці та творчості: піонерські та комсомольські збори, збір макулатури та металобрухту цілими класами, активна участь у різноманітних гуртках (авіамоделювання, драма, спортивні секції). Підлітки 60-х щиро вірили в майбутнє, захоплювалися космосом після польоту Гагаріна та завжди трималися разом.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=650)

        elif st.session_state.step == 4:
            st.markdown('<div class="slide-title">Тест: Запитання 1 з 6</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">Чим школярі у 1960-х роках писали в зошитах?</div>', unsafe_allow_html=True)
            q1 = st.radio("Оберіть варіант:", ["Кульковими ручками", "Пір'яними ручками та чорнильницями", "Простими олівцями"], key="q1", label_visibility="collapsed")
            st.write("")
            if st.button("Перевірити відповідь"):
                if q1 == "Пір'яними ручками та чорнильницями":
                    st.success("✅ Вірно!")
                else:
                    st.error("❌ Невірно. Правильна відповідь: Пір'яними ручками та чорнильницями")
                st.info("💡 **Пояснення:** У той час кулькові ручки ще не були масовими, тому писали дерев'яними ручками зі змінними металевими перами, мачаючи їх у чорнильниці-непроливайки.")

        elif st.session_state.step == 5:
            st.markdown('<div class="slide-title">Тест: Запитання 2 з 6</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">Що обов\'язково лунало у квартирах школярів перед виходом до школи вранці?</div>', unsafe_allow_html=True)
            q2 = st.radio("Оберіть варіант:", ["Ранкова радіозарядка", "Рок-н-рол", "Новини погоди з Європи"], key="q2", label_visibility="collapsed")
            st.write("")
            if st.button("Перевірити відповідь"):
                if q2 == "Ранкова радіозарядка":
                    st.success("✅ Вірно!")
                else:
                    st.error("❌ Невірно. Правильна відповідь: Ранкова радіозарядка")
                st.info("💡 **Пояснення:** День починався рано з радіотрансляції, під яку всі члени родини, включно зі школярами, виконували обов'язкові комплекси вправ.")

        elif st.session_state.step == 6:
            st.markdown('<div class="slide-title">Тест: Запитання 3 з 6</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">Який елемент шкільної форми був обов\'язковим і вимагав постійного окремого догляду?</div>', unsafe_allow_html=True)
            q3 = st.radio("Оберіть варіант:", ["Яскраві кепки", "Білі комірці та манжети", "Шкіряні жилети"], key="q3", label_visibility="collapsed")
            st.write("")
            if st.button("Перевірити відповідь"):
                if q3 == "Білі комірці та манжети":
                    st.success("✅ Вірно!")
                else:
                    st.error("❌ Невірно. Правильна відповідь: Білі комірці та манжети")
                st.info("💡 **Пояснення:** До форми щодня пришивали свіжі білі комірці та манжети, а ввечері їх відпирали та прасували, щоб виглядати охайно.")

        elif st.session_state.step == 7:
            st.markdown('<div class="slide-title">Тест: Запитання 4 з 6</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">Яка історична подія викликала неймовірний інтерес до космосу серед підлітків 60-х?</div>', unsafe_allow_html=True)
            q4 = st.radio("Оберіть варіант:", ["Висадка на Місяць американців", "Політ Юрія Гагаріна в космос", "Запуск першого телескопу"], key="q4", label_visibility="collapsed")
            st.write("")
            if st.button("Перевірити відповідь"):
                if q4 == "Політ Юрія Гагаріна в космос":
                    st.success("✅ Вірно!")
                else:
                    st.error("❌ Невірно. Правильна відповідь: Політ Юрія Гагаріна в космос")
                st.info("💡 **Пояснення:** Політ у 1961 році перевернув уяву молоді, після чого майже кожен другий мріяв стати космонавтом, а гуртки авіамоделювання стали надзвичайно популярними.")

        elif st.session_state.step == 8:
            st.markdown('<div class="slide-title">Тест: Запитання 5 з 6</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">Яка громадська робота чи збір були звичними для радянських школярів?</div>', unsafe_allow_html=True)
            q5 = st.radio("Оберіть варіант:", ["Збір макулатури та металобрухту", "Продаж газет на вулиці", "Догляд за міськими парковками"], key="q5", label_visibility="collapsed")
            st.write("")
            if st.button("Перевірити відповідь"):
                if q5 == "Збір макулатури та металобрухту":
                    st.success("✅ Вірно!")
                else:
                    st.error("❌ Невірно. Правильна відповідь: Збір макулатури та металобрухту")
                st.info("💡 **Пояснення:** Шкільні класи змагалися між собою у зборі макулатури та металобрухту, це було частиною колективного виховання та піонерського руху.")

        elif st.session_state.step == 9:
            st.markdown('<div class="slide-title">Тест: Запитання 6 з 6</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">Чим школярі зазвичай займалися у вільний від уроків час замість гаджетів?</div>', unsafe_allow_html=True)
            q6 = st.radio("Оберіть варіант:", ["Грали у відеоігри на приставках", "Відвідували гуртки (драматичні, спортивні, моделювання) та спілкувалися у дворах", "Дивилися цілодобово телевізор"], key="q6", label_visibility="collapsed")
            st.write("")
            if st.button("Перевірити відповідь"):
                if q6 == "Відвідували гуртки (драматичні, спортивні, моделювання) та спілкувалися у дворах":
                    st.success("✅ Вірно!")
                else:
                    st.error("❌ Невірно. Правильна відповідь: Відвідували гуртки та спілкувалися у дворах")
                st.info("💡 **Пояснення:** За відсутності інтернету та смартфонів соціальне життя підлітків проходило в живій командній роботі, гуртках та активних іграх на вулиці.")

        elif st.session_state.step == 10:
            st.markdown('<div style="text-align: center; font-size: 34px; font-weight: 700; color: #111111; margin-bottom: 15px;">Дякуємо за увагу!</div>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.image("https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?q=80&w=500&auto=format&fit=crop", width=220)
            st.markdown('<div style="text-align: center; font-size: 24px; font-weight: 600; margin-top: 15px; color: #111111;">Презентацію підготували учні та учениці 10 «А» класу</div>', unsafe_allow_html=True)
            st.markdown('<div style="text-align: center; font-size: 18px; color: #555555; margin-top: 10px;">Сподіваємося, вам сподобалася ця подорож у минуле!</div>', unsafe_allow_html=True)

        # Стандартная кнопка "Далі" для всех остальных слайдов (кроме первого)
        st.write("")
        if st.button("Далі ➔"):
            st.session_state.step += 1
            if st.session_state.step > 10:
                st.session_state.step = 0  # Возврат на начало презентации
            st.rerun()
