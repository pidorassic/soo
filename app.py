import streamlit as st

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="centered")

# Применяем стили: белый фон, аккуратная типографика и визуальные блоки
st.markdown(
    """
    <style>
    /* Основной фон и цвета */
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    
    /* Заголовок страницы */
    h1 {
        font-size: 26px !important;
        margin-top: -20px !important;
        margin-bottom: 5px !important;
        color: #111111;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Подзаголовки и текст */
    h3 {
        font-size: 18px !important;
        color: #555555;
        font-weight: 500;
        margin-bottom: 20px !important;
    }

    p, .stMarkdown {
        font-size: 17px !important;
        line-height: 1.5 !important;
        color: #333333;
    }

    /* Блоки с контентом для красивой структуры */
    .info-box {
        background-color: #f8f9fa;
        border-left: 4px solid #333333;
        padding: 15px 20px;
        border-radius: 4px;
        margin-bottom: 20px;
    }

    /* Белый фон контейнеров */
    div.block-container {
        background-color: #ffffff;
        max-width: 700px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Состояние шагов для интерактивного переключения
if "step" not in st.session_state:
    st.session_state.step = 0  # 0 — это титульный лист (приветствие от 10 "А")

# Шаг 0: Титульный лист (Приветствие от 10 "А")
if st.session_state.step == 0:
    st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Интерактивная презентация о буднях подростков эпохи</h3>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="info-box">
            <b>Приветствуем вас!</b><br>
            Проект подготовлен учениками <b>10 «А» класса</b>.<br>
            Приглашаем вас совершить путешествие на несколько десятилетий назад и узнать, чем жили, о чем мечтали и как учились школьники в 1960-х годах.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Школьная атмосфера 1960-х")

# Шаг 1: Утро школьника
elif st.session_state.step == 1:
    st.markdown("<h1>Будни школьника: Утро</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-box">
            <b>Подъем и подготовка</b><br>
            День подростка в 60-е начинался задолго до рассвета с обязательной утренней зарядки под радиоприемник. Строгая форма, начищенные ботинки и портфель с учебниками — всё было готово с вечера.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Сборы на учебу")

# Шаг 2: Уроки в классе
elif st.session_state.step == 2:
    st.markdown("<h1>Будни школьника: Уроки</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-box">
            <b>Учебный процесс</b><br>
            Письмо перьевыми ручками и чернильницами-непроливайками требовало предельной аккуратности. Никаких гаджетов — только тетради в клетку и линейку, живое общение на перервах и стенгазеты в коридорах.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Классная комната")

# Шаг 3: Внеклассная жизнь
elif st.session_state.step == 3:
    st.markdown("<h1>Будни школьника: После уроков</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-box">
            <b>Общественная жизнь и хобби</b><br>
            Пионерские и комсомольские сборы, сбор макулатуры, кружки моделирования и драматические студии. Жизнь после школы была наполнена командной работой и общими интересами.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Внеклассные активности")

# Кнопка переключения шагов
st.write("")
if st.button("Сделать ход"):
    st.session_state.step += 1
    if st.session_state.step > 3:
        st.session_state.step = 0  # Возврат на титульный лист
    st.rerun()
