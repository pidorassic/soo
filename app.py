if st.session_state.step == 1:
    st.markdown('<div class="slide-title">РАНОК — ПОЧАТОК ДНЯ</div>', unsafe_allow_html=True)
    
    # Время и будильник
    st.markdown(
        """
        <div style="font-size: 22px; font-weight: 700; color: #111111; margin-bottom: 12px;">
            ⏰ 07:00. дзвенить будильник
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Основной текст
    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 500; color: #1a1a1a; line-height: 1.6; margin-bottom: 20px;">
            Після пробудження — вмитися, одягнутися, поснідати й зібратися на уроки. 
            Багато школярів носили шкільну форму: хлопці — брюки та піджак, 
            дівчата — сукню з фартухом.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Отдельный факт про сніданок
    st.markdown(
        """
        <div style="background-color: #f8f9fa; border-left: 6px solid #333333; 
                    padding: 16px 22px; border-radius: 6px; margin-bottom: 20px;">
            <div style="font-size: 17px; font-weight: 700; color: #222; margin-bottom: 8px;">
                📌 Сніданок у будній день
            </div>
            <div style="font-size: 16px; color: #333; line-height: 1.5; margin-bottom: 10px;">
                Зазвичай був простим і швидким. Уранці потрібно було просто встигнути 
                поїсти до виходу, тому ніхто не накривав святковий стіл і не готував 
                складних страв.
            </div>
            <div style="font-size: 16px; color: #333; line-height: 1.5;">
                На столі могли бути: каша, яйця, сир, хліб із маслом, бутерброди, 
                чай, молоко або какао.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Совет-подсказка
    st.markdown(
        """
        <div style="font-size: 16px; font-weight: 500; color: #555; line-height: 1.5; margin-bottom: 20px;">
            💡 У різних родинах сніданок залежав від того, які продукти були вдома 
            і скільки часу залишилось до виходу.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=600&auto=format&fit=crop", width=500)
    st.write("")
    if st.button("Далі ➔", key="next_btn_1"):
        st.session_state.step += 1
        st.rerun()
