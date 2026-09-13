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

# Верхняя строчка
st.markdown("<h1>День школяра 60-х</h1>", unsafe_allow_html=True)

# Основной контент
st.write("Добро пожаловать в проект, посвященный жизни школьников в 1960-х годах!")

# Вставляем изображение (активная картинка)
st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", caption="Школьная атмосфера")

# Кнопка коммуникации (интерактивная)
if st.button("Связаться с автором"):
    st.success("Спасибо! Вы можете отправить отзыв или вопрос на почту или в Telegram проекта.")
