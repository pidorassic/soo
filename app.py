import streamlit as st
from PIL import Image

st.set_page_config(page_title="День школяра 60-х", layout="wide")

qp = st.query_params
if "page" in qp:
    try:
        target = int(qp.get("page"))
        if 0 <= target <= 11:
            st.session_state.step = target
        st.query_params.clear()
    except Exception:
        pass

if "step" not in st.session_state:
    st.session_state.step = 0

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        height: 100vh !important;
        background-color: #f5efe6 !important;
    }
    .stApp { background-color: #f5efe6 !important; color: #000000; text-align: left !important; }
    div.block-container {
        background-color: transparent !important;
        max-width: 100% !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding: 5rem 3rem 2rem 3rem !important;
    }
    @keyframes scaleFadeTransition {
        0% { opacity: 0; transform: scale(0.95); filter: blur(4px); }
        100% { opacity: 1; transform: scale(1); filter: blur(0px); }
    }
    @keyframes slideUpFade {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .element-container, .stMarkdown, .stRadio, .stImage, .stButton {
        animation: scaleFadeTransition 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .no-anim, .no-anim * { animation: none !important; transform: none !important; filter: none !important; }
    .slide-title {
        font-size: 28px !important; font-weight: 700 !important; color: #111111 !important;
        margin-bottom: 6px !important; line-height: 1.2 !important; text-align: left !important;
    }
    .question-card {
        background-color: rgba(255,255,255,0.92); border-left: 6px solid #333333;
        padding: 15px 20px; border-radius: 6px; margin-bottom: 15px;
        font-size: 20px !important; font-weight: 600 !important; color: #111111 !important;
    }
    p, label, span, .stMarkdown {
        font-size: 18px !important; font-weight: 500 !important; line-height: 1.5 !important;
        text-align: left !important; color: #1a1a1a !important;
    }
    .stButton > button {
        background-color: #e4e6eb !important; color: #000000 !important;
        font-size: 15px !important; font-weight: 600 !important;
        border: 1px solid #ced4da !important; border-radius: 6px !important;
        padding: 0.4rem 1.2rem !important;
        transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }
    .stButton > button:hover {
        background-color: #d8dadf !important; color: #000000 !important;
        border-color: #adb5bd !important; transform: translateY(-2px);
    }
    .stButton > button:active { transform: translateY(1px); }
    .lesson-card {
        background-color: rgba(255,255,255,0.92); border-left: 6px solid #333333;
        padding: 18px 20px; border-radius: 8px; width: 100% !important;
        min-height: 160px !important; display: block;
    }
    .lesson-card .lesson-title {
        font-size: 18px !important; font-weight: 700 !important; color: #222 !important;
        margin: 0 0 10px 0 !important; line-height: 1.3 !important; display: block !important;
    }
    .lesson-card .lesson-text {
        font-size: 15px !important; font-weight: 500 !important; color: #333 !important;
        line-height: 1.55 !important; margin: 0 !important; display: block !important;
    }
    div[data-testid="stImage"] img {
        max-height: 42vh !important; width: auto !important; max-width: 100% !important;
        object-fit: contain !important; border-radius: 12px !important;
        margin: 0 auto !important; display: block !important;
    }
    .hero-full {
        position: relative; width: 100%; min-height: 82vh; border-radius: 20px; overflow: hidden;
        background-image: url('https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=2000&auto=format&fit=crop');
        background-size: cover; background-position: center;
        box-shadow: 0 30px 80px rgba(0,0,0,0.35);
        display: flex; align-items: center; justify-content: center;
    }
    .hero-full::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(10,10,15,0.92) 0%, rgba(20,20,30,0.78) 40%, rgba(30,25,20,0.75) 70%, rgba(10,10,15,0.9) 100%);
        z-index: 1;
    }
    .hero-content {
        position: relative; z-index: 2; width: 100%; padding: 40px 50px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        min-height: 82vh; box-sizing: border-box;
    }
    .hero-title {
        font-size: 54px !important; font-weight: 900 !important; color: #ffffff !important;
        letter-spacing: 4px !important; line-height: 1.05 !important; margin: 0 0 8px 0 !important;
        text-align: center !important; text-shadow: 0 4px 30px rgba(0,0,0,0.6);
    }
    .hero-subtitle {
        font-size: 15px !important; font-weight: 400 !important; color: #d4c5a0 !important;
        letter-spacing: 6px !important; text-transform: uppercase !important;
        margin: 0 0 30px 0 !important; text-align: center !important;
    }
    .hero-cards {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;
        max-width: 1050px; width: 100%; margin-bottom: 14px;
    }
    .hero-cards-bottom {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;
        max-width: 1050px; width: 100%;
    }
    .hero-card-link {
        display: block; background: rgba(255,255,255,0.07);
        border: 1px solid rgba(212,197,160,0.42);
        border-radius: 14px; padding: 16px 18px;
        text-decoration: none !important; color: inherit !important;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0; cursor: pointer; min-height: 130px; box-sizing: border-box;
    }
    .hero-card-link:nth-child(1) { animation-delay: 0.3s; }
    .hero-card-link:nth-child(2) { animation-delay: 0.5s; }
    .hero-card-link:nth-child(3) { animation-delay: 0.7s; }
    .hero-card-link:hover {
        background: rgba(255,255,255,0.16); border-color: rgba(212,197,160,0.9);
        transform: translateY(-5px); box-shadow: 0 18px 40px rgba(0,0,0,0.5);
        text-decoration: none !important;
    }
    .hero-card-link .hc-icon { font-size: 26px !important; margin-bottom: 8px !important; display: block !important; line-height: 1 !important; }
    .hero-card-link .hc-title {
        font-size: 15px !important; font-weight: 800 !important; color: #ffffff !important;
        margin: 0 0 5px 0 !important; letter-spacing: 0.5px !important; line-height: 1.25 !important;
    }
    .hero-card-link .hc-desc {
        font-size: 12px !important; font-weight: 400 !important; color: #b8ac8f !important;
        line-height: 1.45 !important; margin: 0 !important;
    }
    .hero-footer {
        position: absolute; bottom: 20px; right: 30px; z-index: 2;
        font-size: 11px !important; color: #8a8270 !important; letter-spacing: 2px !important;
    }
    div[data-testid="stDialog"] > div {
        background-color: #ffffff !important; border-radius: 14px !important;
        border-left: 6px solid #333333 !important; padding: 10px 16px !important;
    }
    div[data-testid="stDialog"] h2 { color: #111111 !important; font-size: 22px !important; font-weight: 800 !important; }
    div[data-testid="stDialog"] p, div[data-testid="stDialog"] span,
    div[data-testid="stDialog"] div[data-testid="stMarkdownContainer"] {
        color: #333333 !important; font-size: 16px !important; font-weight: 500 !important; line-height: 1.6 !important;
    }
    div[data-testid="stDialog"] button[aria-label="Close"],
    div[data-testid="stDialog"] [data-testid="stDialogCloseButton"] {
        display: none !important; visibility: hidden !important;
    }
    div[data-testid="stDialog"] .stButton > button {
        background-color: #ffffff !important; color: #333333 !important; font-size: 15px !important;
        font-weight: 700 !important; border: 2px solid #333333 !important; border-radius: 6px !important;
        padding: 0.5rem 1.5rem !important; width: 100% !important;
    }
    div[data-testid="stDialog"] .stButton > button:hover {
        background-color: #333333 !important; color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
@st.dialog("📖 Доп. факт")
def show_extra_dialog():
    st.markdown(
        '<div style="font-size: 16px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 12px;">'
        'У школах діяла п’ятибальна система оцінювання.'
        '</div>'
        '<div style="font-size: 16px; font-weight: 500; color: #333333; line-height: 1.6;">'
        'Формально шкала передбачала оцінки від 1 до 5, але на практиці одиницю майже не ставили. '
        'Вона вважалася надзвичайно низькою оцінкою, яка означала не просто помилку, а повну відсутність знань або підготовки.'
        '</div>',
        unsafe_allow_html=True
    )
    st.write("")
    if st.button("✖ Закрити", key="close_dialog_btn", use_container_width=True):
        st.rerun()

with st.container(key=f"scale_box_{st.session_state.step}"):

    # ===== STEP 0 — ГЛАВНАЯ =====
    if st.session_state.step == 0:
        st.markdown(
            '<div class="hero-full">'
            '<div class="hero-content">'
            '<div class="hero-title">ДЕНЬ ШКОЛЯРА 60-Х</div>'
            '<div class="hero-subtitle">Подорож у минуле</div>'
            '<div class="hero-cards">'
            '<a class="hero-card-link" href="?page=1" target="_self">'
            '<span class="hc-icon">📜</span>'
            '<div class="hc-title">ІСТОРИЧНА ЗГАДКА</div>'
            '<div class="hc-desc">Хто такі піонери та чим займались</div>'
            '</a>'
            '<a class="hero-card-link" href="?page=2" target="_self">'
            '<span class="hc-icon">🌅</span>'
            '<div class="hc-title">ДЕНЬ ПІОНЕРА</div>'
            '<div class="hc-desc">Повний день від ранку до вечора</div>'
            '</a>'
            '<a class="hero-card-link" href="?page=7" target="_self">'
            '<span class="hc-icon">⚖️</span>'
            '<div class="hc-title">ПОРІВНЯННЯ</div>'
            '<div class="hc-desc">Піонери та сучасна молодь</div>'
            '</a>'
            '</div>'
            '<div class="hero-cards-bottom">'
            '<a class="hero-card-link" href="?page=10" target="_self">'
            '<span class="hc-icon">🎯</span>'
            '<div class="hc-title">ІНТЕРАКТИВ</div>'
            '<div class="hc-desc">Спробуй себе у ситуації 60-х років</div>'
            '</a>'
            '<a class="hero-card-link" href="?page=11" target="_self">'
            '<span class="hc-icon">🏁</span>'
            '<div class="hc-title">ЗАВЕРШЕННЯ</div>'
            '<div class="hc-desc">Подяка та фінальне слово</div>'
            '</a>'
            '<div style="visibility: hidden;"></div>'
            '</div>'
            '</div>'
            '<div class="hero-footer">Проект учнів 10-А класу</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.write("")
        col_l, col_c, col_r = st.columns([1, 1, 1])
        with col_c:
            if st.button("Почати подорож ➔", key="next_btn_0", use_container_width=True):
                st.session_state.step = 1
                st.rerun()

    # ===== STEP 1 — ІСТОРИЧНА ЗГАДКА =====
    elif st.session_state.step == 1:
        st.markdown('<div class="slide-title">ІСТОРИЧНА ЗГАДКА</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 800; color: #111111; margin-bottom: 22px; line-height: 1.3;">'
            'ХТО ТАКІ ПІОНЕРИ?'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">📌 Хто це такі</div>'
            '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
            'Піонери — це радянська дитяча організація для школярів віком від 9 до 14 років. '
            'Вона мала повну назву — Всесоюзна піонерська організація імені В. І. Леніна.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">🎒 Чим вони займалися</div>'
            '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
            'Піонери об’єднувалися в загони за класами. Вони ходили в походи, брали участь '
            'у змаганнях і концертах, відвідували гуртки та допомагали в громадських справах.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">🔴 Символіка та ритуали</div>'
            '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
            'У піонерів були свої символи: червоний галстук, урочисті лінійки та салют. '
            'Щоб стати піонером, треба було скласти присягу на церемонії вступу.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 19px; font-weight: 600; color: #111111; margin-bottom: 8px;">📖 Мета організації</div>'
            '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.6; margin-bottom: 22px;">'
            'Піонерство було частиною радянської системи виховання. Через нього дітям '
            'передавали офіційні цінності та залучали до ідеологічних заходів.'
            '</div>',
            unsafe_allow_html=True
        )
        st.write("")
        col_back, col_home, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_1"):
                st.session_state.step = 0
                st.rerun()
        with col_home:
            if st.button("🏠 На головну", key="home_btn_1"):
                st.session_state.step = 0
                st.rerun()

    # ===== STEP 2 — РАНОК =====
    elif st.session_state.step == 2:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · РАНОК</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 700; color: #111111; margin-bottom: 12px;">⏰ 07:00. Підйом та зарядка</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 18px; font-weight: 500; color: #1a1a1a; line-height: 1.6; margin-bottom: 20px;">'
            'У 60-х роках ранок школяра починався о 7-й годині. Спочатку — ранкова гігієна, '
            'потім — обов’язкова зарядка під радіо. Радіоточка була майже в кожній оселі, '
            'і рівно о 07:10 лунала мелодія, під яку вся родина робила вправи.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="background-color: rgba(255,255,255,0.92); border-left: 6px solid #333333; padding: 16px 22px; border-radius: 6px; margin-bottom: 20px;">'
            '<div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 8px;">📌 Сніданок</div>'
            '<div style="font-size: 16px; color: #333; line-height: 1.5;">'
            'Зазвичай простій: каша, яйця, сир, хліб із маслом, чай або молоко. '
            'Ніяких довгих сніданків — усе швидко, щоб встигнути до школи.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
        st.write("")
        col_back, col_next, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_2"):
                st.session_state.step = 0
                st.rerun()
        with col_next:
            if st.button("Далі ➔", key="next_btn_2"):
                st.session_state.step = 3
                st.rerun()

    # ===== STEP 3 — ДОРОГА ДО ШКОЛИ =====
    elif st.session_state.step == 3:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ДОРОГА ДО ШКОЛИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 700; color: #111111; margin-bottom: 12px;">🎒 07:40. Форма та портфель</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 18px; font-weight: 500; color: #1a1a1a; line-height: 1.6; margin-bottom: 20px;">'
            'Школяр 60-х виходив з дому приблизно о 07:40. Усі були однаково вдягнені: '
            'хлопці — у темних брюках і піджаку, дівчата — у коричневій сукні з білим або '
            'чорним фартухом. На плечі — шкіряний портфель, у якому зошити, підручники '
            'та пенал із ручкою-пером.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="background-color: rgba(255,255,255,0.92); border-left: 6px solid #333333; padding: 16px 22px; border-radius: 6px; margin-bottom: 20px;">'
            '<div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 8px;">🚶 Шлях до школи</div>'
            '<div style="font-size: 16px; color: #333; line-height: 1.5;">'
            'Більшість дітей ходили до школи пішки — часто по кілька кварталів. '
            'Дорогою зустрічалися з друзями, обговорювали новини, готувалися до уроків.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
        st.write("")
        col_back, col_next, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_3"):
                st.session_state.step = 2
                st.rerun()
        with col_next:
            if st.button("Далі ➔", key="next_btn_3"):
                st.session_state.step = 4
                st.rerun()

    # ===== STEP 4 — У ШКОЛІ =====
    elif st.session_state.step == 4:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · У ШКОЛІ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 8px;">🔔 08:00. Уроки почалися</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 16px; font-weight: 500; color: #1a1a1a; line-height: 1.5; margin-bottom: 15px;">'
            'Попереду — уроки, перерви, відповіді біля дошки й останній дзвоник.'
            '</div>',
            unsafe_allow_html=True
        )
        col_left, col_right = st.columns([1, 1], gap="large")
        with col_left:
            st.markdown(
                '<div class="no-anim lesson-card">'
                '<div class="lesson-title">📚 Уроки</div>'
                '<div class="lesson-text">'
                'Одне заняття тривало 45 хвилин. Писали чорнильницями-непроливайками та '
                'ручками з металевим пером. За помарочку в зошиті могли знизити оцінку.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
        with col_right:
            st.markdown(
                '<div class="no-anim lesson-card">'
                '<div class="lesson-title">👔 Шкільна форма</div>'
                '<div class="lesson-text">'
                'Дівчата — коричнева сукня з білим або чорним фартухом. '
                'Хлопці — сорочка, брюки та піджак. Форма була обов’язковою.'
                '</div>'
                '</div>',
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
        col_back, col_next, col_extra, _ = st.columns([1, 1, 1, 3])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_4"):
                st.session_state.step = 3
                st.rerun()
        with col_next:
            if st.button("Далі ➔", key="next_btn_4"):
                st.session_state.step = 5
                st.rerun()
        with col_extra:
            if st.button("📖 Доп. інфо", key="extra_btn_4"):
                show_extra_dialog()

    # ===== STEP 5 — ОБІД І ГУРТКИ =====
    elif st.session_state.step == 5:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ОБІД І ГУРТКИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 700; color: #111111; margin-bottom: 12px;">🍽 14:00. Обід та позаурочні справи</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 18px; font-weight: 500; color: #1a1a1a; line-height: 1.6; margin-bottom: 20px;">'
            'Після занять школярі поверталися додому на обід. У 60-х обід був простою, '
            'але ситною стравою — борщ, суп, картопля з котлетою або каша. Потім — '
            'короткий відпочинок, і знову до справ.'
            '</div>',
            unsafe_allow_html=True
        )
        col_left, col_right = st.columns([2, 1], gap="large")
        with col_left:
            st.markdown(
                '<div class="no-anim lesson-card">'
                '<div class="lesson-title">📌 Піонерські справи після уроків</div>'
                '<div class="lesson-text">'
                '• Збори загону та піонерські лінійки<br>'
                '• Збір макулатури та металобрухту<br>'
                '• Допомога старшим (суботники, шефство над молодшими)<br>'
                '• Спортивні секції — футбол, легка атлетика<br>'
                '• Творчі гуртки — драма, музика, малювання'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size: 16px; font-weight: 500; color: #555; line-height: 1.5; margin-top: 18px;">'
                '💡 У 60-х після школи дитина майже ніколи не сиділа вдома. '
                'Гуртки, збори, секції — усе це було безкоштовним і доступним у школі або при будинку піонерів.'
                '</div>',
                unsafe_allow_html=True
            )
        with col_right:
            st.image(
                "https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop",
                use_container_width=True
            )
        st.write("")
        col_back, col_next, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_5"):
                st.session_state.step = 4
                st.rerun()
        with col_next:
            if st.button("Далі ➔", key="next_btn_5"):
                st.session_state.step = 6
                st.rerun()

    # ===== STEP 6 — ВЕЧІР =====
    elif st.session_state.step == 6:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ВЕЧІР</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 700; color: #111111; margin-bottom: 12px;">🌙 19:00. Домашні завдання та відпочинок</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 18px; font-weight: 500; color: #1a1a1a; line-height: 1.6; margin-bottom: 20px;">'
            'Увечері після вечері — час на домашнє завдання. Потім читання книжок, '
            'радіопередачі або настільні ігри з родиною. Телевізор був не в кожній оселі, '
            'тому вечори часто проводили разом — слухали радіо, читали вголос, обговорювали новини.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="background-color: rgba(255,255,255,0.92); border-left: 6px solid #333333; padding: 16px 22px; border-radius: 6px; margin-bottom: 20px;">'
            '<div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 8px;">🌙 Відбій</div>'
            '<div style="font-size: 16px; color: #333; line-height: 1.5;">'
            'Спати лягали рано — о 21:00–22:00. Наступного дня знову підйом о 7-й, '
            'зарядка під радіо, і все по колу.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
        st.write("")
        col_back, col_home, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_6"):
                st.session_state.step = 5
                st.rerun()
        with col_home:
            if st.button("🏠 На головну", key="home_btn_6"):
                st.session_state.step = 0
                st.rerun()

    # ===== STEP 7 — ПОРІВНЯННЯ (введение) =====
    elif st.session_state.step == 7:
        st.markdown('<div class="slide-title">ПОРІВНЯННЯ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 800; color: #111111; margin-bottom: 22px; line-height: 1.3;">'
            'ПІОНЕРИ ТА СУЧАСНА МОЛОДЬ'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.7; margin-bottom: 22px;">'
            'Піонери 60-х та сучасна молодь жили в різних світах. Одні виховувались у колективі, '
            'де головним було спільне благо та дисципліна. Інші — у світі, де цінується свобода '
            'вибору, самовираження та доступ до будь-якої інформації.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 19px; font-weight: 500; color: #333333; line-height: 1.7; margin-bottom: 22px;">'
            'Але в обох поколінь є свої сильні сторони. Давайте порівняємо, що було цінного '
            'у піонерів, а що — у сучасної молоді. Це не про те, хто кращий, а про те, '
            'що кожна епоха формує свої унікальні риси.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="background-color: rgba(255,255,255,0.92); border-left: 6px solid #333333; padding: 16px 22px; border-radius: 6px; margin-bottom: 20px;">'
            '<div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 8px;">📌 Про що поговоримо</div>'
            '<div style="font-size: 16px; color: #333; line-height: 1.6;">'
            '• Що хорошого було у піонерів<br>'
            '• Що хорошого є у сучасної молоді<br>'
            '• Чому вчитися одне в одного'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
        st.write("")
        col_back, col_next, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_7"):
                st.session_state.step = 0
                st.rerun()
        with col_next:
            if st.button("Далі ➔", key="next_btn_7"):
                st.session_state.step = 8
                st.rerun()

    # ===== STEP 8 — ЩО ХОРОШОГО У ПІОНЕРІВ =====
    elif st.session_state.step == 8:
        st.markdown('<div class="slide-title">ПОРІВНЯННЯ · ПІОНЕРИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 800; color: #111111; margin-bottom: 22px; line-height: 1.3;">'
            '✅ ЩО ХОРОШОГО БУЛО У ПІОНЕРІВ'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="no-anim lesson-card">'
            '<div class="lesson-title">📌 Позитивні риси піонерства</div>'
            '<div class="lesson-text">'
            '• <b>Дисципліна та відповідальність</b> — змалку привчали до порядку та обов’язків<br>'
            '• <b>Колективізм</b> — учили працювати в команді, допомагати одне одному<br>'
            '• <b>Повага до старших</b> — шанобливе ставлення до батьків, учителів, ветеранів<br>'
            '• <b>Фізичний розвиток</b> — спорт, походи, активний відпочинок на природі<br>'
            '• <b>Участь у житті громади</b> — суботники, допомога, збір макулатури<br>'
            '• <b>Менше залежності від ґаджетів</b> — більше живого спілкування та ігор у дворі<br>'
            '• <b>Безкоштовні гуртки</b> — доступні для всіх дітей незалежно від достатку'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.write("")
        col_back, col_next, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_8"):
                st.session_state.step = 7
                st.rerun()
        with col_next:
            if st.button("Далі ➔", key="next_btn_8"):
                st.session_state.step = 9
                st.rerun()

    # ===== STEP 9 — ЩО ХОРОШОГО У СУЧАСНОЇ МОЛОДІ =====
    elif st.session_state.step == 9:
        st.markdown('<div class="slide-title">ПОРІВНЯННЯ · СУЧАСНА МОЛОДЬ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 22px; font-weight: 800; color: #111111; margin-bottom: 22px; line-height: 1.3;">'
            '🌟 ЩО ХОРОШОГО Є У СУЧАСНОЇ МОЛОДІ'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="no-anim lesson-card">'
            '<div class="lesson-title">📌 Позитивні риси сучасної молоді</div>'
            '<div class="lesson-text">'
            '• <b>Свобода вибору</b> — можливість самостійно обирати шлях, професію, захоплення<br>'
            '• <b>Доступ до знань</b> — інтернет дає змогу вчитися будь-чому у будь-який час<br>'
            '• <b>Толерантність</b> — відкритість до різних думок, культур, людей<br>'
            '• <b>Технологічна грамотність</b> — швидко опановують нові технології та гаджети<br>'
            '• <b>Креативність</b> — здатність створювати нове: контент, проєкти, стартапи<br>'
            '• <b>Підприємливість</b> — вміння заробляти, реалізовувати ідеї<br>'
            '• <b>Глобальна співпраця</b> — спілкування та робота з людьми з усього світу'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.write("")
        col_back, col_home, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад", key="back_btn_9"):
                st.session_state.step = 8
                st.rerun()
        with col_home:
            if st.button("🏠 На головну", key="home_btn_9"):
                st.session_state.step = 0
                st.rerun()

    # ===== STEP 10 — ІНТЕРАКТИВ =====
    elif st.session_state.step == 10:
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
                st.success("✅ **07:35.** Ти влітаєш до школи майже перед дзвінком. Урок не пропущено.")
                st.info("💡 **Наслідок:** Дисципліну дотримано, але через відсутність сніданку важко зосередитися.")
            elif choice.startswith("Б"):
                st.error("❌ **08:20.** Ти приходиш уже на другий урок. Перший пропущено.")
                st.warning("⚠️ **Штраф:** Класний керівник викликає батьків до школи, доведеться писати пояснювальну.")
            elif choice.startswith("В"):
                st.error("❌ **08:00.** Мама виміряла температуру — нормальна.")
                st.warning("⚠️ **Штраф:** Довелося все одно йти до школи, але зі соромом за спробу збрехати.")
            elif choice.startswith("Г"):
                st.error("❌ **07:40.** Ти приходиш після дзвінка.")
                st.warning("⚠️ **Штраф:** Запізнення зафіксували в журналі, вчитель робить зауваження перед класом.")
        st.write("")
        col_back, col_home, _ = st.columns([1, 1, 4])
        with col_back:
            if st.button("⬅ Назад",
                         
