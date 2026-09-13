import streamlit as st

# Настройка страницы обратно на узкую (centered), как в самом начале
st.set_page_config(page_title="День школяра 60-х", layout="centered")

# Применяем компактные стили без огромных блоков и выравнивания по центру блоков
st.markdown(
    """
    <style>
    /* Общий белый фон */
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Уменьшенный и поднятый заголовок */
    h1 {
        font-size: 22px !important;
        margin-top: -30px !important;
        margin-bottom: 5px !important;
        color: #333333;
        font-weight: 600;
    }

    /* Обычный текст */
    p, label, span, .stMarkdown {
        font-size: 18px !important;
    }

    /* Белый фон контейнера */
    div.block-container {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Инициализация шагов
if "step" not in st.session_state:
    st.session_state.step = 0

# Шаг 0: Приветствие от 10 "А" (обычный текст слева, как раньше)
if st.session_state.step == 0:
    st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)
    st.write("Приветствуем вас! Проект подготовлен учениками 10 «А» класса.")
    st.write("Приглашаем вас совершить путешествие на несколько десятилетий назад и узнать, чем жили, о чем мечтали и как учились школьники в 1960-х годах.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Школьная атмосфера 1960-х")

# Шаг 1: Утро
elif st.session_state.step == 1:
    st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)
    st.write("Утро школьника: подъем, утренняя зарядка под радио и сборы на учебу.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Сборы на учебу")

# Шаг 2: Уроки
elif st.session_state.step == 2:
    st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)
    st.write("Уроки в классе: письмо перьевыми ручками, тетради в клетку и живое общение.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="В классе")

# Шаг 3: Продленка
elif st.session_state.step == 3:
    st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)
    st.write("После уроков: пионерские сборы, кружки и стенгазеты.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Внеклассная жизнь")

# Кнопка «Сделать ход»
st.write("")
if st.button("Сделать ход"):
    st.session_state.step += 1
    if st.session_state.step > 3:
        st.session_state.step = 0
    st.rerun()
