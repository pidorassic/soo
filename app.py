import streamlit as st

# Настройка страницы с выравниванием по левому краю через стили
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS: сдвигаем весь контент влево, убираем дублирующийся заголовок, делаем приветствие крупнее
st.markdown(
    """
    <style>
    /* Общий белый фон и выравнивание по левому краю */
    .stApp {
        background-color: #ffffff;
        color: #000000;
        text-align: left !important;
    }
    
    /* Сдвигаем основной контейнер влево и задаем комфортную ширину */
    div.block-container {
        background-color: #ffffff;
        max-width: 1000px !important;
        margin-left: 2rem !important;
        margin-right: auto !important;
        padding-left: 0rem !important;
    }

    /* Увеличиваем заголовок-приветствие */
    .welcome-title {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #111111 !important;
        margin-bottom: 15px !important;
        line-height: 1.3 !important;
    }

    /* Обычный текст */
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

# Шаг 0: Приветствие от 10 "А" (без верхнего дубля, крупный текст слева)
if st.session_state.step == 0:
    st.markdown('<div class="welcome-title">Приветствуем вас! Проект подготовлен учениками 10 «А» класса.</div>', unsafe_allow_html=True)
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
