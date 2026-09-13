import streamlit as st

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="centered")

# Применяем стили: белый фон, крупный текст, уменьшенный и поднятый заголовок
st.markdown(
    """
    <style>
    /* Общий белый фон приложения */
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Поднимаем и уменьшаем верхнюю строчку (заголовок) */
    h1 {
        font-size: 22px !important;
        margin-top: -30px !important;
        margin-bottom: 10px !important;
        color: #333333;
        font-weight: 600;
    }

    /* Увеличиваем размер обычного текста */
    p, label, span, .stMarkdown {
        font-size: 18px !important;
    }

    /* Делаем белый фон для контейнеров */
    div.block-container {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Инициализация состояния шагов (нужно для работы кнопки «Сделать ход»)
if "step" not in st.session_state:
    st.session_state.step = 1

# Верхняя строчка
st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)

# Логика интерактивных шагов по кнопке «Сделать ход»
if st.session_state.step == 1:
    st.write("Шаг 1: Утро школьника. Подъем, зарядка и сборы в школу.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Школьная атмосфера")

elif st.session_state.step == 2:
    st.write("Шаг 2: Уроки в классе. Письмо перьевыми ручками и чернилами.")
    # Здесь можно будет заменить картинку на другую по теме урока
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="В классе")

elif st.session_state.step == 3:
    st.write("Шаг 3: Продленка и пионерский сбор. Обсуждение успеваемости и стенгазета.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Пионерская организация")

# Кнопка «Сделать ход»
if st.button("Сделать ход"):
    # Переключаем шаг (если дошли до 3-го, возвращаемся на 1-й)
    st.session_state.step += 1
    if st.session_state.step > 3:
        st.session_state.step = 1
    st.rerun()
