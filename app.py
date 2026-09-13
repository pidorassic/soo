import streamlit as st

# Настройка страницы на всю ширину экрана (wide)
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем стили: растягиваем на весь экран, делаем огромный заголовок и приветствие
st.markdown(
    """
    <style>
    /* Общий фон */
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    
    /* Растягиваем главный контейнер на всю ширину экрана */
    div.block-container {
        background-color: #ffffff;
        max-width: 100% !important;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    /* Огромный главный заголовок */
    h1 {
        font-size: 42px !important;
        margin-top: -20px !important;
        margin-bottom: 10px !important;
        color: #111111;
        font-weight: 800;
    }

    /* Подзаголовки */
    h3 {
        font-size: 26px !important;
        color: #444444;
        font-weight: 600;
        margin-bottom: 25px !important;
    }

    /* Крупный текст */
    p, .stMarkdown {
        font-size: 22px !important;
        line-height: 1.6 !important;
        color: #222222;
    }

    /* Большой блок приветствия */
    .welcome-box {
        background-color: #f4f6f8;
        border-left: 8px solid #222222;
        padding: 25px 30px;
        border-radius: 6px;
        margin-bottom: 30px;
        font-size: 24px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Инициализация шагов
if "step" not in st.session_state:
    st.session_state.step = 0

# Шаг 0: Титульный лист (Приветствие от 10 "А")
if st.session_state.step == 0:
    st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Интерактивная презентация о буднях подростков эпохи</h3>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="welcome-box">
            <b>Приветствуем вас!</b><br><br>
            Проект подготовлен учениками <b>10 «А» класса</b>.<br>
            Приглашаем вас совершить увлекательное путешествие на несколько десятилетий назад и узнать, чем жили, о чем мечтали и как учились школьники в 1960-х годах.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop", caption="Школьная атмосфера 1960-х")

# Шаг 1: Утро школьника
elif st.session_state.step == 1:
    st.markdown("<h1>Будни школьника: Утро</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="welcome-box">
            <b>Подъем и подготовка</b><br><br>
            День подростка в 60-е начинался задолго до рассвета с обязательной утренней зарядки под радиоприемник. Строгая форма, начищенные ботинки и портфель с учебниками — всё было готово с вечера.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop", caption="Сборы на учебу")

# Шаг 2: Уроки в классе
elif st.session_state.step == 2:
    st.markdown("<h1>Будни школьника: Уроки</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="welcome-box">
            <b>Учебный процесс</b><br><br>
            Письмо перьевыми ручками и чернильницами-непроливайками требовало предельной аккуратности. Никаких гаджетов — только тетради в клетку и линейку, живое общение на перервах и стенгазеты в коридорах.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop", caption="Классная комната")

# Шаг 3: Внеклассная жизнь
elif st.session_state.step == 3:
    st.markdown("<h1>Будни школьника: После уроков</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="welcome-box">
            <b>Общественная жизнь и хобби</b><br><br>
            Пионерские и комсомольские сборы, сбор макулатуры, кружки моделирования и драматические студии. Жизнь после школы была наполнена командной работой и общими интересами.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop", caption="Внеклассные активности")

# Кнопка переключения шагов
st.write("")
if st.button("Сделать ход"):
    st.session_state.step += 1
    if st.session_state.step > 3:
        st.session_state.step = 0
    st.rerun()
