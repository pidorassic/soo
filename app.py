import streamlit as st
from PIL import Image

# Настройка страницы
st.set_page_config(page_title="День школяра 60-х", layout="wide")

# Применяем CSS: растягиваем на весь экран и выравниваем всё по центру
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        height: 100vh !important;
    }

    .stApp {
        background-color: #ffffff;
        color: #000000;
        text-align: left !important;
    }
    
    /* Растягиваем контейнер на всю ширину и центрируем */
    div.block-container {
        background-color: #ffffff;
        max-width: 100% !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 4rem !important;
        padding-right: 4rem !important;
    }

    @keyframes scaleFadeTransition {
        0% {
            opacity: 0;
            transform: scale(0.95);
            filter: blur(4px);
        }
        100% {
            opacity: 1;
            transform: scale(1);
            filter: blur(0px);
        }
    }

    .element-container, .stMarkdown, .stRadio, .stImage, .stButton {
        animation: scaleFadeTransition 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .slide-title {
        font-size: 30px !important;
        font-weight: 700 !important;
        color: #111111 !important;
        margin-bottom: 10px !important;
        line-height: 1.2 !important;
        text-align: left !important;
    }

    .question-card {
        background-color: #f8f9fa;
        border-left: 6px solid #333333;
        padding: 15px 20px;
        border-radius: 6px;
        margin-bottom: 15px;
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #111111 !important;
    }

    p, label, span, .stMarkdown {
        font-size: 18px !important;
        font-weight: 500 !important;
        line-height: 1.5 !important;
        text-align: left !important;
        color: #1a1a1a !important;
    }

    .stButton > button {
        background-color: #e4e6eb !important;
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border: 1px solid #ced4da !important;
        border-radius: 6px !important;
        padding: 0.5rem 1.5rem !important;
        transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }
    
    .stButton > button:hover {
        background-color: #d8dadf !important;
        color: #000000 !important;
        border-color: #adb5bd !important;
        transform: translateY(-2px);
    }

    .stButton > button:active {
        transform: translateY(1px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "step" not in st.session_state:
    st.session_state.step = 0

with st.container(key=f"scale_box_{st.session_state.step}"):

    if st.session_state.step == 0:
        col_left, col_right = st.columns([1, 1.4], gap="large")
        
        with col_left:
            st.markdown(
                """
                <div style="padding-right: 15px;">
                    <div style="font-size: 32px; font-weight: 800; color: #111111; margin-bottom: 10px; line-height: 1.2;">
                        Вітаємо вас!<br>Проект підготовлено учнями 10 «А» класу.
                    </div>
                    <div style="font-size: 17px; font-weight: 500; color: #444444; line-height: 1.4;">
                        Запрошуємо вас здійснити захоплюючу подорож на кілька десятиліть назад. Ми пропонуємо поринути в атмосферу минулого століття та на власні очі побачити, яким було повсякденне життя підлітків у 60-х роках.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style="margin-top: 15px; padding: 12px 18px; background-color: #f8f9fa; border-left: 5px solid #555; border-radius: 4px;">
                    <div style="font-size: 16px; font-weight: 700; color: #222; margin-bottom: 4px;">📌 Що на вас чекає у цій подорожі:</div>
                    <div style="font-size: 15px; color: #555; line-height: 1.3;">
                        • Ранкові звички та шкільна форма<br>
                        • Особливості навчання за чорнильницями<br>
                        • Інтерактивний вибір життєвої ситуації 60-х років
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_right:
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=1200&auto=format&fit=crop", use_container_width=True)
            
            st.write("")
            if st.button("Далі ➔", key="next_btn_0"):
                st.session_state.step += 1
                st.rerun()

    else:
        if st.session_state.step == 1:
            st.markdown('<div class="slide-title">Ранок</div>', unsafe_allow_html=True)
            st.write("Кожен день радянського школяра у 60-х роках розпочинався дуже рано. Ще до того, як зійде сонце або лунала шкільна дзвінка пора, у квартирах лунала радіотрансляція з обов'язковою ранковою зарядкою. Одяг — виключно випрасувана форма, білі комірці та манжети, які пришивали окремо. Портфелі з цупкої шкіри збиралися суворо з вечора, а взуття ретельно начищалося до блиску.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
            st.write("")
            if st.button("Далі ➔", key="next_btn_1"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 2:
            st.markdown('<div class="slide-title">Уроки</div>', unsafe_allow_html=True)
            st.write("У навчальному процесі панувала сувора дисципліна та порядок. Школярі писали справжніми чорнильницами-непроливайками та дерев'яними ручками з металевими пером, що вимагало неабиякої акуратності, адже за помарочку в зошиті могли знизити оцінку. Жодних гаджетів чи калькуляторів — лише таблиця множення, логарифмічні лінійки, живі дискусії на перервах та дружні розмови біля стінгазет у коридорах.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
            st.write("")
            if st.button("Далі ➔", key="next_btn_2"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 3:
            st.markdown('<div class="slide-title">Позаурочний час</div>', unsafe_allow_html=True)
            st.write("Після завершення уроків життя школярів не зупинялося. Позаурочний час був сповнений колективної праці та творчості: піонерські та комсомольські збори, збір макулатури та металобрухту цілими класами, активна участь у різноманітних гуртках (авіамоделювання, драма, спортивні секції). Підлітки 60-х щиро вірили в майбутнє, захоплювалися космосом після польоту Гагаріна та завжди трималися разом.")
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
            st.write("")
            if st.button("Далі ➔", key="next_btn_3"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 4:
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
                    st.success("✅ **07:35.** Ти влітаєш до школи майже перед дзвінком. Урок не пропущено — ти встиг, але до обіду ще дуже далеко.")
                    st.info("💡 **Наслідок:** Дисципліну дотримано, але через відсутність сніданку на уроках важко зосередитися, а живіт починає бурчати вже на середині математики.")
                elif choice.startswith("Б"):
                    st.error("❌ **08:20.** Ти приходиш уже на другий урок. Перший урок пропущено, а відсутність потрібно пояснити.")
                    st.warning("⚠️ **Наслідок (Штраф):** Просто вирішити «сьогодні не піду» у 60-х було неможливо. Класний керівник викликає батьків до школи, а тобі доведеться писати пояснювальну записку та відробляти пропущену тему після уроків.")
                elif choice.startswith("В"):
                    st.error("❌ **08:00.** Мама: «Якщо тобі справді погано — підемо до лікаря. А якщо ні — збирайся та йди до школи».")
                    st.warning("⚠️ **Наслідок (Штраф):** Мама швидко розкрила хитрощі та виміряла температуру (яка виявилася нормальною). Довелося все одно йти до школи, але тепер ще й зі соромом за спробу збрехати та допитом від батьків увечері.")
                elif choice.startswith("Г"):
                    st.error("❌ **07:40.** Ти приходиш після дзвінка.")
                    st.warning("⚠️ **Наслідок (Штраф):** Запізнення вже зафіксували в классному журналі. Вчитель робить публічне зауваження перед усім класом, а староста записує тебе у шкільну стінгазету ганьби («порушники дисципліни»).")

            st.write("")
            if st.button("Далі ➔", key="next_btn_4"):
                st.session_state.step += 1
                st.rerun()

        elif st.session_state.step == 5:
            # Используем колонки с пустыми боковыми отступами, чтобы центр всегда был по середине экрана
            col_l, col_c, col_r = st.columns([1, 2, 1])
            with col_c:
                st.markdown('<div style="text-align: center; font-size: 38px; font-weight: 800; color: #111111; margin-bottom: 20px;">Дякуємо за увагу!</div>', unsafe_allow_html=True)
                
                st.markdown(
                    """
                    <style>
                    img {
                        max-height: 40vh !important;
                        width: auto !important;
                        display: block !important;
                        margin: 0 auto !important;
                        border-radius: 12px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                try:
                    img = Image.open("end.jpg")
                    st.image(img)
                except Exception:
                    st.error("Файл 'end.jpg' не знайдено.")
                
                st.markdown('<div style="text-align: center; font-size: 24px; font-weight: 700; margin-top: 20px; color: #111111;">Презентацію підготували учні та учениці 10 «А» класу</div>', unsafe_allow_html=True)
                st.markdown('<div style="text-align: center; font-size: 17px; color: #555555; margin-top: 5px; margin-bottom: 20px;">Сподіваємося, вам сподобалася ця подорож у минуле!</div>', unsafe_allow_html=True)

                if st.button("На початок ➔", key="restart_btn"):
                    st.session_state.step = 0
                    st.rerun()
