import streamlit as st

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS: полная анимация для каждого элемента и нажатия кнопки "Далі"
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
        text-align: left !important;
    }
    
    div.block-container {
        background-color: #ffffff;
        max-width: 1000px !important;
        margin-left: 2rem !important;
        margin-right: auto !important;
        padding-left: 0rem !important;
    }

    /* Мощная плавная анимация появления для каждого шага и элемента */
    @keyframes smoothAppear {
        0% {
            opacity: 0;
            transform: translateY(20px) scale(0.98);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* Применяем анимацию ко всему содержимому страницы и блокам */
    .element-container, .stMarkdown, .stRadio, .stImage, .stButton {
        animation: smoothAppear 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
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
        font-size: 21px !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
        text-align: left !important;
        color: #1a1a1a !important;
    }

    /* Стиль для ВСЕХ кнопок Streamlit с анимацией нажатия */
    .stButton > button {
        background-color: #e4e6eb !important;
        color: #000000 !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        border: 1px solid #ced4da !important;
        border-radius: 6px !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Эффект при наведении мыши на кнопку */
    .stButton > button:hover {
        background-color: #d8dadf !important;
        color: #000000 !important;
        border-color: #adb5bd !important;
        transform: translateY(-2px) scale(1.02);
    }

    /* Эффект при клике на кнопку */
    .stButton > button:active {
        transform: translateY(1px) scale(0.97);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Инициализация шагов (0-3: слайды презентации, 4-9: 6 вопросов теста, 10: завершающий слайд)
if "step" not in st.session_state:
    st.session_state.step = 0

# Шаг 0: Приветствие от 10 "А"
if st.session_state.step == 0:
    st.markdown('<div align="center" style="font-size: 34px; font-weight: 700; color: #111111; margin-bottom: 20px; line-height: 1.3;">Вітаємо вас! Проект підготовлено учнями 10 «А» класу.</div>', unsafe_allow_html=True)
    st.write("Запрошуємо вас здійснити захоплюючу подорож на кілька десятиліть назад. Ми пропонуємо поринути в атмосферу минулого століття та на власні очі побачити, яким було повсякденне життя, турботи, мрії та захоплення звичайних підлітків у 60-х роках.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 1: Утро
elif st.session_state.step == 1:
    st.markdown('<div class="slide-title">Ранок</div>', unsafe_allow_html=True)
    st.write("Кожен день радянського школяра у 60-х роках розпочинався дуже рано. Ще до того, як зійде сонце або лунала шкільна дзвінка пора, у квартирах лунала радіотрансляція з обов'язковою ранковою зарядкою. Одяг — виключно випрасувана форма, білі комірці та манжети, які пришивали окремо. Портфелі з цупкої шкіри збиралися суворо з вечора, а взуття ретельно начищалося до блиску.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 2: Уроки
elif st.session_state.step == 2:
    st.markdown('<div class="slide-title">Уроки</div>', unsafe_allow_html=True)
    st.write("У навчальному процесі панувала сувора дисципліна та порядок. Школярі писали справжніми чорнильницами-непроливайками та дерев'яними ручками з металевими пером, що вимагало неабиякої акуратності, адже за помарочку в зошиті могли знизити оцінку. Жодних гаджетів чи калькуляторів — лише таблиця множення, логарифмічні лінійки, живі дискусії на перервах та дружні розмови біля стінгазет у коридорах.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 3: Внеклассная жизнь
elif st.session_state.step == 3:
    st.markdown('<div class="slide-title">Позаурочний час</div>', unsafe_allow_html=True)
    st.write("Після завершення уроків життя школярів не зупинялося. Позаурочний час був сповнений колективної праці та творчості: піонерські та комсомольські збори, збір макулатури та металобрухту цілими класами, активна участь у різноманітних гуртках (авіамоделювання, драма, спортивні секції). Підлітки 60-х щиро вірили в майбутнє, захоплювалися космосом після польоту Гагаріна та завжди трималися разом.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 4: Тест - Питання 1
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

# Шаг 5: Тест - Питання 2
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

# Шаг 6: Тест - Питання 3
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

# Шаг 7: Тест - Питання 4
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

# Шаг 8: Тест - Питання 5
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

# Шаг 9: Тест - Питання 6
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

# Шаг 10: Завершающий слайд
elif st.session_state.step == 10:
    st.markdown('<div style="text-align: center; font-size: 36px; font-weight: 700; color: #111111; margin-bottom: 20px;">Дякуємо за увагу!</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?q=80&w=600&auto=format&fit=crop", width=250)
        
    st.markdown('<div style="text-align: center; font-size: 26px; font-weight: 600; margin-top: 25px; color: #111111;">Презентацію підготували учні та учениці 10 «А» класу</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-size: 20px; color: #555555; margin-top: 15px;">Сподіваємося, вам сподобалася ця подорож у минуле!</div>', unsafe_allow_html=True)

# Кнопка переключения шагов (Далі)
st.write("")
if st.button("Далі"):
    st.session_state.step += 1
    if st.session_state.step > 10:
        st.session_state.step = 0  # Возврат на начало презентации
    st.rerun()
