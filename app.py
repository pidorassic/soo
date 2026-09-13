import streamlit as st

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS
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

    .slide-title {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #111111 !important;
        margin-bottom: 15px !important;
        line-height: 1.3 !important;
        text-align: left !important;
    }

    p, label, span, .stMarkdown {
        font-size: 19px !important;
        text-align: left !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Инициализация шагов
if "step" not in st.session_state:
    st.session_state.step = 0

# Шаг 0: Приветствие от 10 "А" (заголовок по центру экрана)
if st.session_state.step == 0:
    st.markdown('<div align="center" style="font-size: 32px; font-weight: 700; color: #111111; margin-bottom: 15px; line-height: 1.3;">Вітаємо вас! Проект підготовлено учнями 10 «А» класу.</div>', unsafe_allow_html=True)
    st.write("Запрошуємо вас здійснити подорож на кілька десятиліть назад і дізнатися, чим жили, про що мріяли та як вчилися школярі у 1960-х роках.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop")

# Шаг 1: Утро
elif st.session_state.step == 1:
    st.markdown('<div class="slide-title">Ранок</div>', unsafe_allow_html=True)
    st.write("Ранок школяра: підйом, ранкова зарядка під радіоприймач та збори на навчання.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop")

# Шаг 2: Уроки
elif st.session_state.step == 2:
    st.markdown('<div class="slide-title">Уроки</div>', unsafe_allow_html=True)
    st.write("Уроки в класі: письмо пір'яними ручками, зошити в клітинку та живе спілкування на перервах.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop")

# Шаг 3: Внеклассная жизнь
elif st.session_state.step == 3:
    st.markdown('<div class="slide-title">Позаурочний час</div>', unsafe_allow_html=True)
    st.write("Після уроків: піонерські збори, гуртки за інтересами та випуск стінгазет.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop")

# Кнопка «Слід.»
st.write("")
if st.button("Слід."):
    st.session_state.step += 1
    if st.session_state.step > 3:
        st.session_state.step = 0
    st.rerun()
