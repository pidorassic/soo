import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="День школяра 60-х", layout="wide")

qp = st.query_params
if "page" in qp:
    try:
        target = int(qp.get("page"))
        if 0 <= target <= 15:
            st.session_state.step = target
        st.query_params.clear()
    except Exception:
        pass

if "step" not in st.session_state:
    st.session_state.step = 0

total_steps = 15
progress_pct = int((st.session_state.step / total_steps) * 100)

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
        max-width: 100% !important; width: 100% !important;
        margin: 0 auto !important;
        padding: 5rem 3rem 2rem 3rem !important;
    }
    .progress-bar-fixed {
        position: fixed; top: 0; left: 0; width: 100%; height: 5px;
        background: rgba(255,255,255,0.15); z-index: 999999;
    }
    .progress-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #d4af6a 0%, #e8c88a 50%, #d4af6a 100%);
        box-shadow: 0 0 12px rgba(212, 175, 106, 0.8);
        transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        border-radius: 0 3px 3px 0;
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
        font-size: 18px !important; font-weight: 500 !important; color: #111111 !important;
        line-height: 1.6 !important;
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
    .stButton > button:active { transform: translateY(2px) scale(0.97) !important; }
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
        max-height: 58vh !important; width: 100% !important; max-width: 100% !important;
        object-fit: cover !important; border-radius: 12px !important;
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
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0; cursor: pointer; min-height: 130px; box-sizing: border-box;
        position: relative; overflow: hidden;
    }
    .hero-card-link::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at center, var(--glow, transparent) 0%, transparent 70%);
        opacity: 0; transition: opacity 0.4s ease; pointer-events: none; z-index: 0;
    }
    .hero-card-link:hover::before { opacity: 1; }
    .hero-card-link > * { position: relative; z-index: 1; }
    .hero-card-link:nth-child(1) { --glow: rgba(212, 175, 106, 0.35); }
    .hero-card-link:nth-child(2) { --glow: rgba(220, 53, 69, 0.35); }
    .hero-card-link:nth-child(3) { --glow: rgba(13, 110, 253, 0.35); }
    .hero-card-link:nth-child(4) { --glow: rgba(255, 193, 7, 0.35); }
    .hero-card-link:nth-child(5) { --glow: rgba(25, 135, 84, 0.35); }
    .hero-card-link:nth-child(6) { --glow: rgba(111, 66, 193, 0.35); }
    .hero-card-link:nth-child(1) { animation-delay: 0.3s; }
    .hero-card-link:nth-child(2) { animation-delay: 0.45s; }
    .hero-card-link:nth-child(3) { animation-delay: 0.6s; }
    .hero-card-link:nth-child(4) { animation-delay: 0.75s; }
    .hero-card-link:nth-child(5) { animation-delay: 0.9s; }
    .hero-card-link:hover {
        background: rgba(255,255,255,0.18);
        border-color: rgba(212,197,160,0.95);
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 20px 45px rgba(0,0,0,0.55), 0 0 30px var(--glow, transparent);
        text-decoration: none !important;
    }
    .hero-card-link:active {
        transform: translateY(-1px) scale(0.98);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4), 0 0 20px var(--glow, transparent);
        transition: all 0.1s ease;
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
    div[data-testid="stDialog"] button[aria-label="Close"] {
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

st.markdown(
    f'<div class="progress-bar-fixed"><div class="progress-bar-fill" style="width:{progress_pct}%;"></div></div>',
    unsafe_allow_html=True
)

@st.dialog("📖 Доп. факт")
def show_extra_dialog():
    st.markdown(
        '<div style="font-size:16px;font-weight:500;color:#333;line-height:1.6;margin-bottom:12px;">У школах діяла п’ятибальна система оцінювання.</div>'
        '<div style="font-size:16px;font-weight:500;color:#333;line-height:1.6;">Формально шкала передбачала оцінки від 1 до 5, але на практиці одиницю майже не ставили.</div>',
        unsafe_allow_html=True
    )
    st.write("")
    if st.button("✖ Закрити", key="close_dialog_btn", use_container_width=True):
        st.rerun()

with st.container(key=f"scale_box_{st.session_state.step}"):

    if st.session_state.step == 0:
        st.markdown(
            '<div class="hero-full"><div class="hero-content">'
            '<div class="hero-title">ДЕНЬ ШКОЛЯРА 60-Х</div>'
            '<div class="hero-subtitle">Подорож у минуле</div>'
            '<div class="hero-cards">'
            '<a class="hero-card-link" href="?page=1" target="_self"><span class="hc-icon">📜</span><div class="hc-title">ІСТОРИЧНА ЗГАДКА</div><div class="hc-desc">Хто такі піонери та чим займались</div></a>'
            '<a class="hero-card-link" href="?page=2" target="_self"><span class="hc-icon">🌅</span><div class="hc-title">ДЕНЬ ПІОНЕРА</div><div class="hc-desc">Повний день від ранку до вечора</div></a>'
            '<a class="hero-card-link" href="?page=7" target="_self"><span class="hc-icon">⚖️</span><div class="hc-title">ПОРІВНЯННЯ</div><div class="hc-desc">Піонери та сучасна молодь</div></a>'
            '</div>'
            '<div class="hero-cards-bottom">'
            '<a class="hero-card-link" href="?page=10" target="_self"><span class="hc-icon">🎵</span><div class="hc-title">МОДА ТА КУЛЬТУРА</div><div class="hc-desc">Музика, кіно, ігри та стиль 60-х</div></a>'
            '<a class="hero-card-link" href="?page=12" target="_self"><span class="hc-icon">🎯</span><div class="hc-title">ІНТЕРАКТИВ</div><div class="hc-desc">Три тести про життя піонера</div></a>'
            '<a class="hero-card-link" href="?page=15" target="_self"><span class="hc-icon">🏁</span><div class="hc-title">ЗАВЕРШЕННЯ</div><div class="hc-desc">Подяка та фінальне слово</div></a>'
            '</div></div>'
            '<div class="hero-footer">Проект учнів 10-А класу</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("Почати подорож ➔", key="next_btn_0", use_container_width=True):
                st.session_state.step = 1
                st.rerun()

    elif st.session_state.step == 1:
        st.markdown('<div class="slide-title">ІСТОРИЧНА ЗГАДКА</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:22px;">ХТО ТАКІ ПІОНЕРИ?</div>'
            '<div style="font-size:19px;font-weight:600;color:#111;margin-bottom:8px;">📌 Хто це такі</div>'
            '<div style="font-size:19px;font-weight:500;color:#333;line-height:1.6;margin-bottom:22px;">Піонери — це радянська дитяча організація для школярів віком від 9 до 14 років.</div>'
            '<div style="font-size:19px;font-weight:600;color:#111;margin-bottom:8px;">🎒 Чим вони займалися</div>'
            '<div style="font-size:19px;font-weight:500;color:#333;line-height:1.6;margin-bottom:22px;">Піонери об’єднувалися в загони за класами. Ходили в походи, брали участь у змаганнях і концертах, відвідували гуртки.</div>'
            '<div style="font-size:19px;font-weight:600;color:#111;margin-bottom:8px;">🔴 Символіка та ритуали</div>'
            '<div style="font-size:19px;font-weight:500;color:#333;line-height:1.6;margin-bottom:22px;">Червоний галстук, урочисті лінійки та салют. Присяга на церемонії вступу.</div>'
            '<div style="font-size:19px;font-weight:600;color:#111;margin-bottom:8px;">📖 Мета організації</div>'
            '<div style="font-size:19px;font-weight:500;color:#333;line-height:1.6;margin-bottom:22px;">Піонерство було частиною радянської системи виховання.</div>',
            unsafe_allow_html=True
        )
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_1"):
                st.session_state.step = 0
                st.rerun()
        with c2:
            if st.button("🏠 На головну", key="home_btn_1"):
                st.session_state.step = 0
                st.rerun()

    elif st.session_state.step == 2:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · РАНОК</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:12px;">⏰ 07:00. Підйом та зарядка</div>'
            '<div style="font-size:18px;font-weight:500;color:#1a1a1a;line-height:1.6;margin-bottom:20px;">У 60-х роках ранок школяра починався о 7-й годині. Спочатку — ранкова гігієна, потім — обов’язкова зарядка під радіо.</div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([1, 1], gap="large")
        with cl:
            st.markdown(
                '<div class="no-anim lesson-card" style="margin-bottom:14px;min-height:auto;">'
                '<div class="lesson-title">📌 Сніданок</div>'
                '<div class="lesson-text">Каша, яйця, сир, хліб із маслом, чай або молоко.</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="no-anim lesson-card" style="min-height:auto;">'
                '<div class="lesson-title">🌅 Ранок у 60-х</div>'
                '<div class="lesson-text">Зарядка під радіо, сніданок, збори до школи — усе за розкладом.</div></div>',
                unsafe_allow_html=True
            )
        with cr:
            st.image("piner_morning.jpg", use_container_width=True)
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_2"):
                st.session_state.step = 0
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_2"):
                st.session_state.step = 3
                st.rerun()    elif st.session_state.step == 3:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ДОРОГА ДО ШКОЛИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:12px;">🎒 07:40. Вихід з дому</div>'
            '<div style="font-size:18px;font-weight:500;color:#1a1a1a;line-height:1.6;margin-bottom:20px;">Школяр 60-х виходив з дому приблизно о 07:40. Усі поспішали — попереду був день, сповнений уроків, гуртків та піонерських справ.</div>'
            '<div style="background:rgba(255,255,255,0.92);border-left:6px solid #333;padding:16px 22px;border-radius:6px;margin-bottom:20px;">'
            '<div style="font-size:17px;font-weight:700;color:#222;margin-bottom:8px;">🚶 Шлях до школи</div>'
            '<div style="font-size:16px;color:#333;line-height:1.5;">Більшість дітей ходили до школи пішки — часто по кілька кварталів. Дорогою зустрічалися з друзями.</div></div>',
            unsafe_allow_html=True
        )
        st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_3"):
                st.session_state.step = 2
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_3"):
                st.session_state.step = 4
                st.rerun()

    elif st.session_state.step == 4:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · У ШКОЛІ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:20px;font-weight:700;color:#111;margin-bottom:8px;">🔔 08:00. Уроки почалися</div>'
            '<div style="font-size:16px;font-weight:500;color:#1a1a1a;line-height:1.5;margin-bottom:15px;">Попереду — уроки, перерви, відповіді біля дошки й останній дзвоник.</div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([1, 1], gap="large")
        with cl:
            st.markdown(
                '<div class="no-anim lesson-card" style="margin-bottom:14px;"><div class="lesson-title">📚 Уроки</div>'
                '<div class="lesson-text">Одне заняття тривало 45 хвилин. Писали чорнильницями-непроливайками та ручками з металевим пером.</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="no-anim lesson-card"><div class="lesson-title">👔 Шкільна форма</div>'
                '<div class="lesson-text">Дівчата — коричнева сукня з фартухом. Хлопці — сорочка, брюки та піджак.</div></div>',
                unsafe_allow_html=True
            )
        with cr:
            st.image("school_desk.jpg", use_container_width=True)
        st.write("")
        c1, c2, c3, _ = st.columns([1, 1, 1, 3])
        with c1:
            if st.button("⬅ Назад", key="back_btn_4"):
                st.session_state.step = 3
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_4"):
                st.session_state.step = 5
                st.rerun()
        with c3:
            if st.button("📖 Доп. інфо", key="extra_btn_4"):
                show_extra_dialog()

    elif st.session_state.step == 5:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ОБІД І ГУРТКИ</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:12px;">🍽 14:00. Обід та позаурочні справи</div>'
            '<div style="font-size:18px;font-weight:500;color:#1a1a1a;line-height:1.6;margin-bottom:20px;">Після занять школярі поверталися додому на обід. Потім — короткий відпочинок, і знову до справ.</div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([2, 1], gap="large")
        with cl:
            st.markdown(
                '<div class="no-anim lesson-card"><div class="lesson-title">📌 Піонерські справи після уроків</div>'
                '<div class="lesson-text">• Збори загону та піонерські лінійки<br>• Збір макулатури та металобрухту<br>• Допомога старшим<br>• Спортивні секції<br>• Творчі гуртки</div></div>'
                '<div style="font-size:16px;font-weight:500;color:#555;line-height:1.5;margin-top:18px;">💡 У 60-х після школи дитина майже ніколи не сиділа вдома.</div>',
                unsafe_allow_html=True
            )
        with cr:
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", use_container_width=True)
        st.write("")
        c1, c2, _ = st.columns([1, 1, 4])
        with c1:
            if st.button("⬅ Назад", key="back_btn_5"):
                st.session_state.step = 4
                st.rerun()
        with c2:
            if st.button("Далі ➔", key="next_btn_5"):
                st.session_state.step = 6
                st.rerun()

    elif st.session_state.step == 6:
        st.markdown('<div class="slide-title">ДЕНЬ ПІОНЕРА · ВЕЧІР</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:12px;">🌙 19:00. Домашні завдання та відпочинок</div>'
            '<div style="font-size:18px;font-weight:500;color:#1a1a1a;line-height:1.6;margin-bottom:20px;">Увечері — час на домашнє завдання. Потім читання книжок або настільні ігри з родиною.</div>'
            '<div style="background:rgba(255,255,255,0.92);border-left:6px solid #333;padding:16px 22px;border-radius:6px;margin-bottom:20px;">'
            '<div style="font-size:17px;font-weight:700;color:#222;margin-bottom:8px;">🌙 Відбій</div>'
            '<div style="font-size:16px;color:#333;line-height:1.5;">Спати лягали рано — о 21:00–22:00.</div></div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([1, 1], gap="large")
        with cl:
            st.markdown(
                '<div class="no-anim lesson-card" style="margin-bottom:14px;min-height:auto;">'
                '<div class="lesson-title">📖 Домашнє завдання</div>'
                '<div class="lesson-text">Уроки готували за підручниками та зошитами. Писати доводилося пером — тому акуратність була дуже важливою.</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="no-anim lesson-card" style="margin-bottom:14px;min-height:auto;">'
                '<div class="lesson-title">📚 Читання книжок</div>'
                '<div class="lesson-text">У 60-х не було інтернету, а телебачення — не в кожній родині. Тому книжки були головним джерелом знань і розваг.</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="no-anim lesson-card" style="min-height:auto;">'
                '<div class="lesson-title">🎲 Настільні ігри</div>'
                '<div class="lesson-text">Шахи, шашки, доміно. Грали всією родиною — це був справжній вечірній ритуал.</div></div>',
                unsafe_allow_html=True
            )
        with cr:
            st.markdown(
                '<div class="no-anim lesson-card" style="margin-bottom:14px;min-height:auto;">'
                '<div class="lesson-title">📻 Радіо та музика</div>'
                '<div class="lesson-text">Ввечері по радіо часто транслювали концерти, радіовистави та новини. Слухали всі разом.</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="no-anim lesson-card" style="min-height:auto;">'
                '<div class="lesson-title">🛏 Підготовка до сну</div>'
                '<div class="lesson-text">Форма на завтра, портфель зібраний, одяг складений. Усе — за розпорядком, як привчали в піонерському загоні.</div></div>',
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
            '<div style="font-size:22px;font-weight:800;color:#111;margin-bottom:22px;">ПІОНЕРИ ТА СУЧАСНА МОЛОДЬ</div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([1.3, 1], gap="large")
        with cl:
            st.markdown(
                '<div style="font-size:18px;font-weight:500;color:#333;line-height:1.7;margin-bottom:20px;">Піонери 60-х та сучасна молодь жили в різних світах. Одні виховувались у колективі, де головним було спільне благо та дисципліна.</div>'
                '<div style="font-size:18px;font-weight:500;color:#333;line-height:1.7;">Інші — у світі, де цінується свобода вибору. Давайте порівняємо.</div>',
                unsafe_allow_html=True
            )
        with cr:
            st.markdown(
                '<div class="no-anim lesson-card" style="min-height:auto;padding:24px 26px;">'
                '<div class="lesson-title" style="font-size:19px;">📌 Про що поговоримо</div>'
                '<div class="lesson-text" style="font-size:16px;line-height:1.9;">✅ Що хорошого було у піонерів<br><br>🌟 Що хорошого є у сучасної молоді</div></div>',
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
                st.rerun()    elif st.session_state.step == 8:
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
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:22px;">🎵 Що слухали, дивилися та в що грали</div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([1.3, 1], gap="large")
        with cl:
            st.markdown(
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
        with cr:
            st.markdown(
                '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;">'
                '<div class="lesson-title" style="font-size:18px;">💃 Танці та дворові ігри</div>'
                '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
                '• Танці під патефон у дворі<br>'
                '• «Козаки-розбійники», «Вишибали»<br>'
                '• Вечірні гуляння під гітару<br>'
                '• Дитячі пісні та лічилки'
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
            '<div style="font-size:22px;font-weight:700;color:#111;margin-bottom:22px;">👗 Як одягалися у 60-х</div>',
            unsafe_allow_html=True
        )
        cl, cr = st.columns([1, 1], gap="large")
        with cl:
            st.markdown(
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
        with cr:
            st.markdown(
                '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;margin-bottom:14px;">'
                '<div class="lesson-title" style="font-size:18px;">✂️ Стиль епохи</div>'
                '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
                '• Яскраві принти та міні-спідниці<br>'
                '• Молодь наслідувала західних зірок<br>'
                '• Зачіски — чубчики, начоси, коси'
                '</div></div>'
                '<div class="no-anim lesson-card" style="min-height:auto;padding:20px 24px;">'
                '<div class="lesson-title" style="font-size:18px;">🧵 Аксесуари</div>'
                '<div class="lesson-text" style="font-size:15px;line-height:1.7;">'
                '• Стрічки, банти, гребінці<br>'
                '• Шкіряні портфелі та сумки<br>'
                '• Годинники та брошки як прикраси'
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
