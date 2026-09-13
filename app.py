import streamlit as st

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS: увеличиваем шрифт основного текста и делаем его крупнее/жирнее
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

    /* Увеличиваем размер и жирность основного текста */
    p, label, span, .stMarkdown {
        font-size: 21px !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
        text-align: left !important;
        color: #1a1a1a !important;
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
    st.markdown('<div align="center" style="font-size: 34px; font-weight: 700; color: #111111; margin-bottom: 20px; line-height: 1.3;">Вітаємо вас! Проект підготовлено учнями 10 «А» класу.</div>', unsafe_allow_html=True)
    st.write("Запрошуємо вас здійснити захоплюючу подорож на кілька десятиліть назад. Ми пропонуємо поринути в атмосферу минулого століття та на власні очі побачити, яким було повсякденне життя, турботи, мрії та захоплення звичайних підлітків у 1960-х роках.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 1: Утро
elif st.session_state.step == 1:
    st.markdown('<div class="slide-title">Ранок</div>', unsafe_allow_html=True)
    st.write("Кожен день радянського школяра у 60-х роках розпочинався дуже рано. Ще до того, як зійде сонце або лунала шкільна дзвінка пора, у квартирах лунала радіотрансляція з обов'язковою ранковою зарядкою. Одяг — виключно випрасувана форма, білі комірці та манжети, які пришивали окремо. Портфелі з цупкої шкіри збиралися суворо з вечора, а взуття ретельно начищалося до блиску.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 2: Уроки
elif st.session_state.step == 2:
    st.markdown('<div class="slide-title">Уроки</div>', unsafe_allow_html=True)
    st.write("У навчальному процесі панувала сувора дисципліна та порядок. Школярі писали справжніми чорнильницями-непроливайками та дерев'яними ручками з металевими пером, що вимагало неабиякої акуратності, адже за помарочку в зошиті могли знизити оцінку. Жодних гаджетів чи калькуляторів — лише таблиця Множення, логарифмічні лінійки, живі дискусії на перервах та дружні розмови біля стінгазет у коридорах.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Шаг 3: Внеклассная жизнь
elif st.session_state.step == 3:
    st.markdown('<div class="slide-title">Позаурочний час</div>', unsafe_allow_html=True)
    st.write("Після завершення уроків життя школярів не зупинялося. Позаурочний час був сповнений колективної праці та творчості: піонерські та комсомольські збори, збір макулатури та металобрухту цілими класами, активна участь у різноманітних гуртках (авіамоделювання, драма, спортивні секції). Подростки 60-х щиро вірили в майбутнє, захоплювалися космосом після польоту Гагаріна та завжди трималися разом.")
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=800&auto=format&fit=crop", width=700)

# Кнопка «Слід.»
st.write("")
if st.button("Слід."):
    st.session_state.step += 1
    if st.session_state.step > 3:
        st.session_state.step = 0
    st.rerun()
