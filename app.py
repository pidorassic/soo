import streamlit as st
from PIL import Image

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        height: 100vh !important;
    }

    .stApp {
        background-color: #ffffff;
        color: #000000;
        text-align: left !important;
    }
    
    div.block-container {
        background-color: #ffffff;
        max-width: 100% !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding-top: 5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 4rem !important;
        padding-right: 4rem !important;
    }

    @keyframes scaleFadeTransition {
        0% { opacity: 0; transform: scale(0.95); filter: blur(4px); }
        100% { opacity: 1; transform: scale(1); filter: blur(0px); }
    }

    .element-container, .stMarkdown, .stRadio, .stImage, .stButton {
        animation: scaleFadeTransition 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .no-anim, .no-anim * {
        animation: none !important;
        transform: none !important;
        filter: none !important;
    }

    .slide-title {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: #111111 !important;
        margin-bottom: 6px !important;
        line-height: 1.2 !important;
        text-align: left !important;
    }

    .question-card {
        background-color: #f8f9fa;
        border-left: 6px solid #333333;
        padding: 15px 20px;
        border-radius: 6px;
        margin-bottom: 15px;
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #111111 !important;
    }

    p, label, span, .stMarkdown {
        font-size: 18px !important;
        font-weight: 500 !important;
        line-height: 1.5 !important;
        text-align: left !important;
        color: #1a1a1a !important;
    }

    .stButton > button {
        background-color: #e4e6eb !important;
        color: #000000 !important;
        font-size: 15px !important;
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

    /* Карточки на слайде У ШКОЛІ — компактнее */
    .lesson-card {
        background-color: #f8f9fa;
        border-left: 6px solid #333333;
        padding: 18px 20px;
        border-radius: 8px;
        width: 100% !important;
        min-height: 160px !important;
        display: block;
    }
    .lesson-card .lesson-title {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #222 !important;
        margin: 0 0 10px 0 !important;
        padding: 0 !important;
        line-height: 1.3 !important;
        display: block !important;
    }
    .lesson-card .lesson-text {
        font-size: 15px !important;
        font-weight: 500 !important;
        color: #333 !important;
        line-height: 1.55 !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }

    /* Фото — ограничиваем по высоте */
    div[data-testid="stImage"] img {
        max-height: 42vh !important;
        width: auto !important;
        max-width: 100% !important;
        object-fit: contain !important;
        border-radius: 12px !important;
        margin: 0 auto !important;
        display: block !important;
    }

    /* ===== Растягиваем слайд "ІСТОРИЧНА ЗГАДКА" на всю ширину ===== */
    .full-width-text {
        width: 100% !important;
        max-width: 100% !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .full-width-text p,
    .full-width-text div {
        width: 100% !important;
        max-width: 100% !important;
        font-size: 17px !important;
        font-weight: 500 !important;
        color: #333 !important;
        line-height: 1.7 !important;
        margin: 0 0 16px 0 !important;
        text-align: justify !important;
    }

    /* ===== Стилизация нативного st.dialog ===== */
    div[data-testid="stDialog"] > div {
        background-color: #ffffff !important;
        border-radius: 14px !important;
        border-left: 6px solid #333333 !important;
        padding: 10px 16px !important;
    }
    div[data-testid="stDialog"] h2,
    div[data-testid="stDialog"] [data-testid="stMarkdownContainer"] h2 {
        color: #111111 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
    }
    div[data-testid="stDialog"] p,
    div[data-testid="stDialog"] span,
    div[data-testid="stDialog"] div[data-testid="stMarkdownContainer"],
    div[data-testid="stDialog"] div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stDialog"] div[data-testid="stMarkdownContainer"] span {
        color: #333333 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
    }

    div[data-testid="stDialog"] button[aria-label="Close"],
    div[data-testid="stDialog"] button[aria-label="close"],
    div[data-testid="stDialog"] [data-testid="stDialogCloseButton"],
    div[data-testid="stDialog"] [data-testid="stModalCloseButton"] {
        display: none !important;
        visibility: hidden !important;
    }

    div[data-testid="stDialog"] .stButton > button {
        background-color: #ffffff !important;
        color: #333333 !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        border: 2px solid #333333 !important;
        border-radius: 6px !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    div[data-testid="stDialog"] .stButton > button:hover {
        background-color: #333333 !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== ДИАЛОГОВОЕ ОКНО =====
@st.dialog("📖 Доп. факт")
def show_extra_dialog():
    st.markdown(
        """
        <div style="font-size: 16px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 12px;">
            У школах діяла п’ятибальна система оцінювання.
        </div>
        <div style="font-size: 16px; font-weight: 500; color: #333333; line-height: 1.6;">
            Формально шкала передбачала оцінки від 1 до 5, але на практиці 
            одиницю майже не ставили. Вона вважалася надзвичайно низькою 
            оцінкою, яка означала не просто помилку, а повну відсутність 
            знань або підготовки.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    if st.button("✖ Закрити", key="close_dialog_btn", use_container_width=True):
        st.rerun()

# Инициализация состояния
if "step" not in st.session_state:
    st.session_state.step = 0

with st.container(key=f"scale_box_{st.session_state.step}"):

    if st.session_state.step == 0:
        col_left, col_right = st.columns([1, 1.4], gap="large")
        
        with col_left:
            st.markdown(
                """
                <div style="padding-right: 15px;">
                    <div style="font-size: 32px; font-weight: 800; color: #111111; margin-bottom: 10px; line-height: 1.2;">
                        Вітаємо вас!<br>Проект підготовлено учнями 10 «А» класу.
                    </div>
                    <div style="font-size: 17px; font-weight: 500; color: #444444; line-height: 1.4;">
                        Запрошуємо вас здійснити захоплюючу подорож на кілька десятиліть назад. Ми пропонуємо поринути в атмосферу минулого століття та на власні очі побачити, яким було повсякденне життя підлітків у 60-х роках.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style="margin-top: 15px; padding: 12px 18px; background-color: #f8f9fa; border-left: 5px solid #555; border-radius: 4px;">
                    <div style="font-size: 16px; font-weight: 700; color: #222; margin-bottom: 4px;">📌 Що на вас чекає у цій подорожі:</div>
                    <div style="font-size: 15px; color: #555; line-height: 1.3;">
                        • Ранкові звички та шкільна форма<br>
                        • Особливості навчання за чорнильницями<br>
                        • Інтерактивний вибір життєвої ситуації 60-х років
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_right:
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop", use_container_width=True)
            
            st.write("")
            if st.button("Далі ➔", key="next_btn_0"):
                st.session_state.step += 1
                st.rerun()

    else:
        # === НОВЫЙ СЛАЙД: ІСТОРИЧНА ЗГАДКА (растянут на всю ширину) ===
        if st.session_state.step == 1:
            st.markdown('<div class="slide-title">ІСТОРИЧНА ЗГАДКА</div>', unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 22px; font-weight: 800; color: #111111; margin-bottom: 22px; line-height: 1.3;">
                    ХТО ТАКІ ПІОНЕРИ?
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Текст растянут на всю ширину, выравнен по ширине
            st.markdown(
                """
                <div class="full-width-text">
                    <p>У СРСР існувала Всесоюзна піонерська організація імені В. І. Леніна — дитяча організація для школярів приблизно від 9 до 14 років.</p>
                    
                    <p>Піонери об’єднувалися у загони, зазвичай за класами. Вони брали участь у походах, змаганнях, концертах, роботі гуртків і громадських заходах. Часто це були організовані школою або місцевими установами активності, у яких школярі мали брати участь.</p>
                    
                    <p>Організація мала власну символіку та ритуали: червоний галстук, урочисті лінійки, салют і церемонію вступу з піонерською присягою. Для багатьох дітей це було обов’язковою частиною шкільного життя, а не особистим вибором.</p>
                    
                    <p>Піонерство було частиною радянської системи виховання. Через організацію дітям прищеплювали офіційні радянські цінності, знайомили їх із державною символікою та героями й залучали до ідеологічних заходів.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.write("")
            if st.button("Далі ➔", key="next_btn_1"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 2:
            st.markdown('<div class="slide-title">РАНОК — ПОЧАТОК ДНЯ</div>', unsafe_allow_html=True)
            
            st.markdown(
                """
                <div style="font-size: 22px; font-weight: 700; color: #111111; margin-bottom: 12px;">
                    ⏰ 07:00. дзвенить будильник
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style="font-size: 18px; font-weight: 500; color: #1a1a1a; line-height: 1.6; margin-bottom: 20px;">
                    Зазвичай сніданок був простим і швидким. Уранці потрібно було просто 
                    встигнути поїсти до виходу, тому ніхто не накривав святковий стіл 
                    і не готував складних страв. На столі могли бути: каша, яйця, сир, 
                    хліб із маслом, бутерброди, чай, молоко або какао.
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style="background-color: #f8f9fa; border-left: 6px solid #333333; 
                            padding: 16px 22px; border-radius: 6px; margin-bottom: 20px;">
                    <div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 8px;">
                        📌 Ранкова рутина та шкільна форма
                    </div>
                    <div style="font-size: 16px; color: #333; line-height: 1.5;">
                        Після пробудження — вмитися, одягнутися, поснідати й зібратися 
                        на уроки. Багато школярів носили шкільну форму: хлопці — брюки 
                        та піджак, дівчата — сукню з фартухом.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style="font-size: 16px; font-weight: 500; color: #555; line-height: 1.5; margin-bottom: 20px;">
                    💡 У різних родинах сніданок залежав від того, які продукти були вдома 
                    і скільки часу залишилось до виходу.
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
            st.write("")
            if st.button("Далі ➔", key="next_btn_2"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 3:
            st.markdown('<div class="slide-title">У ШКОЛІ</div>', unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 8px;">
                    🔔 08:00. Лунає дзвоник
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                <div style="font-size: 16px; font-weight: 500; color: #1a1a1a; line-height: 1.5; margin-bottom: 15px;">
                    Попереду — уроки, перерви, відповіді біля дошки й останній дзвоник.
                </div>
                """,
                unsafe_allow_html=True
            )
            
            col_left, col_right = st.columns([1, 1], gap="large")
            
            with col_left:
                st.markdown(
                    """
                    <div class="no-anim lesson-card">
                        <div class="lesson-title">📚 Уроки</div>
                        <div class="lesson-text">
                            Вони проходили приблизно так само, як ти можеш уявити звичайний 
                            урок сьогодні, тривало одне заняття 45 хвилин, були перерви, 
                            контрольні та домашнє завдання.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            with col_right:
                st.markdown(
                    """
                    <div class="no-anim lesson-card">
                        <div class="lesson-title">👔 Обовʼязкова шкільна форма</div>
                        <div class="lesson-text">
                            Для дівчат типовою була сукня коричневого кольору з білим 
                            або чорним фартухом.<br><br>
                            Для хлопців — сорочка, брюки та піджак.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            st.write("")
            col_photo_l, col_photo_c, col_photo_r = st.columns([1, 2, 1])
            with col_photo_c:
                st.image(
                    "https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop",
                    use_container_width=True
                )
            
            st.write("")
            col_btn1, col_btn2, _ = st.columns([1, 1, 4])
            with col_btn1:
                if st.button("Далі ➔", key="next_btn_3"):
                    st.session_state.step += 1
                    st.rerun()
            with col_btn2:
                if st.button("📖 Доп. інфо", key="extra_btn_3"):
                    show_extra_dialog()

        elif st.session_state.step == 4:
            st.markdown('<div class="slide-title">Позаурочний час</div>', unsafe_allow_html=True)
            st.write("Після завершення уроків життя школярів не зупинялося. Позаурочний час був сповнений колективної праці та творчості: піонерські та комсомольські збори, збір макулатури та металобрухту цілими класами, активна участь у різноманітних гуртках (авіамоделювання, драма, спортивні секції). Підлітки 60-х щиро вірили в майбутнє, захоплювалися космосом після польоту Гагаріна та завжди трималися разом.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
            st.write("")
            if st.button("Далі ➔", key="next_btn_4"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 5:
            st.markdown('<div class="slide-title">Інтерактивна ситуація</div>', unsafe_allow_html=True)
            st.markdown('<div class="question-card">До початку першого уроку залишилося зовсім мало часу. Що робитимеш?</div>', unsafe_allow_html=True)
            
            choice = st.radio(
                "Оберіть варіант дії:",
                [
                    "А) Швидко збираюся і біжу до школи, навіть без нормального сніданку.",
                    "Б) Вирішую пропустити перший урок і прийти пізніше.",
                    "В) Кажу батькам, що погано почуваюся, щоб залишитися вдома.",
                    "Г) Спокійно йду до школи, навіть якщо трохи запізнюся."
                ],
                key="choice_60s",
                label_visibility="collapsed"
            )
            
            st.write("")
            if st.button("Зробити вибір"):
                if choice.startswith("А"):
                    st.success("✅ **07:35.** Ти влітаєш до школи майже перед дзвінком. Урок не пропущено — ти встиг, але до обіду ще дуже далеко.")
                    st.info("💡 **Наслідок:** Дисципліну дотримано, але через відсутність сніданку на уроках важко зосередитися, а живіт починає бурчати вже на середині математики.")
                elif choice.startswith("Б"):
                    st.error("❌ **08:20.** Ти приходиш уже на другий урок. Перший урок пропущено, а відсутність потрібно пояснити.")
                    st.warning("⚠️ **Наслідок (Штраф):** Просто вирішити «сьогодні не піду» у 60-х було неможливо. Класний керівник викликає батьків до школи, а тобі доведеться писати пояснювальну записку та відробляти пропущену тему після уроків.")
                elif choice.startswith("В"):
                    st.error("❌ **08:00.** Мама: «Якщо тобі справді погано — підемо до лікаря. А якщо ні — збирайся та йди до школи».")
                    st.warning("⚠️ **Наслідок (Штраф):** Мама швидко розкрила хитрощі та виміряла температуру (яка виявилася нормальною). Довелося все одно йти до школи, але тепер ще й зі соромом за спробу збрехати та допитом від батьків увечері.")
                elif choice.startswith("Г"):
                    st.error("❌ **07:40.** Ти приходиш після дзвінка.")
                    st.warning("⚠️ **Наслідок (Штраф):** Запізнення вже зафіксували в классному журналі. Вчитель робить публічне зауваження перед усім класом, а староста записує тебе у шкільну стінгазету ганьби («порушники дисципліни»).")

            st.write("")
            if st.button("Далі ➔", key="next_btn_5"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 6:
            st.markdown(
                """
                <style>
                div[data-testid="stVerticalBlock"] {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    width: 100%;
                }
                .stImage {
                    display: flex;
                    justify-content: center;
                    width: 100%;
                }
                img {
                    max-height: 60vh !important;
                    width: auto !important;
                    display: block !important;
                    margin: 0 auto !important;
                    border-radius: 12px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown('<div style="text-align: center; font-size: 38px; font-weight: 800; color: #111111; margin-bottom: 20px; width: 100%;">Дякуємо за увагу!</div>', unsafe_allow_html=True)
            
            try:
                img = Image.open("end.jpg")
                st.image(img)
            except Exception:
                st.error("Файл 'end.jpg' не знайдено.")
            
            st.markdown('<div style="text-align: center; font-size: 24px; font-weight: 700; margin-top: 20px; color: #111111; width: 100%;">Сподіваємося, вам сподобалася ця подорож у минуле!</div>', unsafe_allow_html=True)

            if st.button("На початок ➔", key="restart_btn"):
                st.session_state.step = 0
                st.rerun()
