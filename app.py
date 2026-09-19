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
        background-color: #f5efe6 !important;
    }

    .stApp {
        background-color: #f5efe6 !important;
        color: #000000;
        text-align: left !important;
    }
    
    div.block-container {
        background-color: transparent !important;
        max-width: 100% !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    @keyframes scaleFadeTransition {
        0% { opacity: 0; transform: scale(0.95); filter: blur(4px); }
        100% { opacity: 1; transform: scale(1); filter: blur(0px); }
    }

    @keyframes slideUpFade {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes titleFadeIn {
        0% { opacity: 0; transform: scale(0.9); letter-spacing: 10px; }
        100% { opacity: 1; transform: scale(1); letter-spacing: 2px; }
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
        background-color: rgba(255, 255, 255, 0.92);
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

    .lesson-card {
        background-color: rgba(255, 255, 255, 0.92);
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

    div[data-testid="stImage"] img {
        max-height: 42vh !important;
        width: auto !important;
        max-width: 100% !important;
        object-fit: contain !important;
        border-radius: 12px !important;
        margin: 0 auto !important;
        display: block !important;
    }

    /* ============================================================ */
    /* ===== СТАРТОВЫЙ СЛАЙД — ТЁМНЫЙ КИНЕМАТОГРАФИЧНЫЙ ГЕРОЙ ===== */
    /* ============================================================ */

    .hero-wrapper {
        position: relative;
        width: 100%;
        max-width: 1400px;
        margin: 0 auto;
        min-height: 82vh;
        border-radius: 18px;
        overflow: hidden;
        background-image: url('https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4);
    }

    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            135deg,
            rgba(10, 10, 15, 0.9) 0%,
            rgba(20, 20, 30, 0.78) 40%,
            rgba(30, 25, 20, 0.72) 70%,
            rgba(10, 10, 15, 0.88) 100%
        );
        display: flex;
        flex-direction: column;
        padding: 50px 60px;
        box-sizing: border-box;
    }

    .hero-title {
        font-size: 58px !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        letter-spacing: 2px !important;
        line-height: 1.05 !important;
        margin: 0 0 8px 0 !important;
        text-shadow: 0 4px 30px rgba(0, 0, 0, 0.6);
        animation: titleFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .hero-subtitle {
        font-size: 18px !important;
        font-weight: 400 !important;
        color: #d4c5a0 !important;
        letter-spacing: 6px !important;
        text-transform: uppercase !important;
        margin: 0 0 30px 0 !important;
        animation: titleFadeIn 1.4s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;
        opacity: 0;
    }

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
        max-width: 620px;
        margin-top: auto;
    }

    .hero-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(212, 197, 160, 0.35);
        border-radius: 12px;
        padding: 16px 18px;
        backdrop-filter: blur(8px);
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        animation: slideUpFade 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0;
    }

    .hero-card:hover {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(212, 197, 160, 0.7);
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }

    .hero-card:nth-child(1) { animation-delay: 0.5s; }
    .hero-card:nth-child(2) { animation-delay: 0.7s; }
    .hero-card:nth-child(3) { animation-delay: 0.9s; }
    .hero-card:nth-child(4) { animation-delay: 1.1s; }

    .hero-card .card-icon {
        font-size: 22px !important;
        margin-bottom: 4px !important;
        display: block !important;
    }

    .hero-card .card-title {
        font-size: 17px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        margin: 0 0 3px 0 !important;
        letter-spacing: 0.5px !important;
    }

    .hero-card .card-desc {
        font-size: 12.5px !important;
        font-weight: 400 !important;
        color: #b8ac8f !important;
        line-height: 1.4 !important;
        margin: 0 !important;
    }

    .hero-footer {
        position: absolute;
        bottom: 25px;
        right: 35px;
        font-size: 12px !important;
        color: #8a8270 !important;
        letter-spacing: 1px !important;
        font-weight: 400 !important;
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
        # === СТАРТОВЫЙ СЛАЙД — ТЁМНЫЙ ГЕРОЙ ===
        # ВАЖНО: HTML без отступов слева, иначе Streamlit воспримет как код!
        st.markdown(
            '<div class="hero-wrapper">'
            '<div class="hero-overlay">'
            '<div class="hero-title">ДЕНЬ<br>ШКОЛЯРА 60-Х</div>'
            '<div class="hero-subtitle">Подорож у минуле</div>'
            '<div class="cards-grid">'
            '<div class="hero-card">'
            '<span class="card-icon">🌅</span>'
            '<div class="card-title">Ранок</div>'
            '<div class="card-desc">Початок дня, сніданок та форма</div>'
            '</div>'
            '<div class="hero-card">'
            '<span class="card-icon">📚</span>'
            '<div class="card-title">Уроки</div>'
            '<div class="card-desc">Школа, чорнильниці та дисципліна</div>'
            '</div>'
            '<div class="hero-card">'
            '<span class="card-icon">🎒</span>'
            '<div class="card-title">Позаурочний час</div>'
            '<div class="card-desc">Гуртки, піонери та колектив</div>'
            '</div>'
            '<div class="hero-card">'
            '<span class="card-icon">🎯</span>'
            '<div class="card-title">Інтерактив</div>'
            '<div class="card-desc">Спробуй себе у ситуації 60-х</div>'
            '</div>'
            '</div>'
            '<div class="hero-footer">Проект учнів 10-А класу</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        
        st.write("")
        col_btn_l, col_btn_c, col_btn_r = st.columns([1, 1, 1])
        with col_btn_c:
            if st.button("Почати подорож ➔", key="next_btn_0", use_container_width=True):
                st.session_state.step += 1
                st.rerun()

    else:
        # === ІСТОРИЧНА ЗГАДКА ===
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
            
            st.markdown(
                '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">'
                '📌 Хто це такі'
                '</div>'
                '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
                'Піонери — це радянська дитяча організація для школярів віком від 9 до 14 років. '
                'Вона мала повну назву — Всесоюзна піонерська організація імені В. І. Леніна.'
                '</div>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">'
                '🎒 Чим вони займалися'
                '</div>'
                '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
                'Піонери об’єднувалися в загони за класами. Вони ходили в походи, брали участь '
                'у змаганнях і концертах, відвідували гуртки та допомагали в громадських справах. '
                'Усе це організовувала школа або місцеві установи.'
                '</div>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">'
                '🔴 Символіка та ритуали'
                '</div>'
                '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
                'У піонерів були свої символи: червоний галстук, урочисті лінійки та салют. '
                'Щоб стати піонером, треба було скласти присягу на церемонії вступу. '
                'Для більшості дітей це було не власним вибором, а обов’язковою частиною шкільного життя.'
                '</div>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">'
                '📖 Мета організації'
                '</div>'
                '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
                'Піонерство було частиною радянської системи виховання. Через нього дітям '
                'передавали офіційні цінності, знайомили з державними символами та героями '
                'й залучали до ідеологічних заходів.'
                '</div>',
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
                <div style="background-color: rgba(255, 255, 255, 0.92); border-left: 6px solid #333333; 
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
