import streamlit as st

# =========================
# ПРИНУДИТЕЛЬНЫЕ НАСТРОЙКИ СЕРВЕРА
# =========================
st.set_page_config(
    page_title="День школяра 60-х",
    page_icon="📚",
    layout="centered"
)

# =========================
# ИНИЦИАЛИЗАЦИЯ СЕССИИ
# =========================
if "page" not in st.session_state:
    st.session_state.page = "day"

if "slide" not in st.session_state:
    st.session_state.slide = 0

if "question" not in st.session_state:
    st.session_state.question = 0

if "checked" not in st.session_state:
    st.session_state.checked = False

# =========================
# ДАННЫЕ
# =========================
slides = [
    {
        "title": "1. Ранок і збори до школи",
        "text": "Підйом, умивання, сніданок. Школяр одягає шкільну форму та збирає портфель із підручниками й зошитами."
    },
    {
        "title": "2. Дорога до школи",
        "text": "Діти зазвичай ходять до школи пішки, зустрічаються з друзями у дворі та разом ідуть на уроки."
    },
    {
        "title": "3. Навчання в школі",
        "text": "Учні вивчають математику, літературу, історію, географію, фізику та інші предмети. Вони відповідають біля дошки та пишуть у зошитах."
    },
    {
        "title": "4. Після школи",
        "text": "Після уроків школярі повертаються додому, обідають та виконують домашні завдання. Деякі відвідують гуртки або спортивні секції."
    },
    {
        "title": "5. Вільний час",
        "text": "Діти грають у дворі з друзями, читають книжки, дивляться телепередачі та допомагають батькам."
    },
    {
        "title": "6. Вечір і підготовка до сну",
        "text": "Вечеря з родиною, завершення домашніх справ, підготовка портфеля та шкільної форми на наступний день, після чого — сон."
    }
]

questions = [
    {
        "question": "Як називали нелегальні музичні записи, зроблені на рентгенівських знімках?",
        "options": ["Вініл", "На костях", "Компакт-диск", "Касета"],
        "answer": "На костях",
        "explanation": "Такі записи робили на використаних рентгенівських знімках."
    },
    {
        "question": "Скільки коштувала газована вода з сиропом в автоматі?",
        "options": ["1 копійка", "3 копійки", "10 копійок", "50 копійок"],
        "answer": "3 копійки",
        "explanation": "Газована вода з сиропом коштувала 3 копійки."
    },
    {
        "question": "Яка подія стала одним із головних символів 1960-х років?",
        "options": ["Поява інтернету", "Перший політ людини в космос", "Поява смартфонів", "Створення соціальних мереж"],
        "answer": "Перший політ людини в космос",
        "explanation": "У 1961 році відбувся перший політ людини в космос."
    },
    {
        "question": "На якому пристрої часто слухали музику вдома?",
        "options": ["Смартфон", "Бобінний магнітофон", "MP3-плеєр", "Планшет"],
        "answer": "Бобінний магнітофон",
        "explanation": "Музику часто записували та слухали на магнітній стрічці."
    },
    {
        "question": "Який одяг зазвичай носили школярі?",
        "options": ["Джинси та худі", "Шкільну форму", "Спортивний костюм", "Сучасний вільний одяг"],
        "answer": "Шкільну форму",
        "explanation": "У школах використовувалася обов'язкова шкільна форма."
    },
    {
        "question": "Що часто робили діти після школи?",
        "options": ["Грали у футбол, класики та хованки", "Грали в онлайн-ігри", "Дивилися стріми", "Користувалися соціальними мережами"],
        "answer": "Грали у футбол, класики та хованки",
        "explanation": "Діти багато часу проводили у дворі та грали разом."
    }
]

# =========================
# ИНТЕРФЕЙС
# =========================
st.title("📚 День школяра 1960-х років")
st.write("Дізнайся, як проходив день школяра, а потім пройди тест.")

col1, col2 = st.columns(2)
with col1:
    if st.button("📅 День школяра"):
        st.session_state.page = "day"
        st.rerun()

with col2:
    if st.button("🧠 Тест"):
        st.session_state.page = "test"
        st.session_state.question = 0
        st.session_state.checked = False
        st.rerun()

st.divider()

if st.session_state.page == "day":
    current = slides[st.session_state.slide]
    st.progress((st.session_state.slide + 1) / len(slides))
    st.caption(f"Частина {st.session_state.slide + 1} із {len(slides)}")
    st.subheader(current["title"])
    st.write(current["text"])
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.slide > 0:
            if st.button("⬅️ Назад"):
                st.session_state.slide -= 1
                st.rerun()

    with col2:
        if st.session_state.slide < len(slides) - 1:
            if st.button("Далі ➡️"):
                st.session_state.slide += 1
                st.rerun()
        else:
            if st.button("🧠 Перейти до тесту"):
                st.session_state.page = "test"
                st.session_state.question = 0
                st.session_state.checked = False
                st.rerun()

elif st.session_state.page == "test":
    q = questions[st.session_state.question]
    st.progress((st.session_state.question + 1) / len(questions))
    st.subheader(f"🧠 Питання {st.session_state.question + 1} із {len(questions)}")
    st.write(q["question"])

    choice = st.radio(
        "Обери правильну відповідь:",
        q["options"],
        key=f"q_{st.session_state.question}"
    )

    if not st.session_state.checked:
        if st.button("Перевірити відповідь"):
            st.session_state.checked = True
            st.rerun()
    else:
        if choice == q["answer"]:
            st.success("✅ Правильно!")
        else:
            st.error(f"❌ Неправильно. Правильна відповідь: {q['answer']}")
        st.info(f"📌 {q['explanation']}")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.question > 0:
            if st.button("⬅️ Попереднє"):
                st.session_state.question -= 1
                st.session_state.checked = False
                st.rerun()

    with col2:
        if st.session_state.question < len(questions) - 1:
            if st.button("Наступне ➡️"):
                st.session_state.question += 1
                st.session_state.checked = False
                st.rerun()
        else:
            st.success("🎉 Тест завершено!")
            if st.button("🔄 Почати тест заново"):
                st.session_state.question = 0
                st.session_state.checked = False
                st.rerun()
import http.server
import socketserver
import webbrowser
import os

PORT = 8050
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Сервер запущен: http://127.0.0.1:{PORT}")
    webbrowser.open(f"http://127.0.0.1:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass