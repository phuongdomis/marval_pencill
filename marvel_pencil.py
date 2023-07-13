import streamlit as st
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded_image}');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }}
        .stApp > div {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('picture/background2.jpg')


st.markdown('<center><h1>Vũ trụ Siêu Anh Hùng: Cuộc Chiến Ác - Thiện trong MCU</h1></center>', unsafe_allow_html=True)
st.markdown('<center><h2>Trái Đất: Nơi Các Siêu Anh Hùng Huyền Thoại Hội Tụ và Bảo Vệ Vũ Trụ Khỏi Sự Tàn Phá</h2></center>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify">Ngày xửa ngày xưa, trong một vũ trụ điện ảnh thần thánh được gọi là <b>MCU</b> (<a href="https://www.marvel.com/teams-and-groups" title="Marvel Cinematic Universe">Marvel Cinematic Universe</a>), nơi tạo ra những câu chuyện hấp dẫn về <b>siêu anh hùng</b>, các nhân vật huyền thoại và cuộc chiến giữa <b>ác</b> và <b>thiện</b>.</p>', unsafe_allow_html=True)
st.image('picture/OIG.jpg', width=700)
cols = st.columns(2)
with cols[0]:
    st.write("<br/><br/>", unsafe_allow_html=True)
    st.markdown('''
    <p style="text-align: justify">Tại đây, có một vùng đất được gọi là <b>Trái Đất</b>, nơi những <b>siêu anh hùng</b> tài ba và gan dạ tụ họp để bảo vệ thế giới khỏi sự tàn phá của các <b>thế lực đen tối</b>.</p>''', unsafe_allow_html=True)
with cols[1]:
    st.image('picture/marvel.jpg', width=350)
cols = st.columns(2)
with cols[0]:
    st.image('picture/iron.jpg', width=350)
with cols[1]:
    st.markdown('<p style="text-align: justify">Trái Đất đã chứng kiến sự xuất hiện của <a href="https://www.marvel.com/movies/iron-man-3" title="Marvel Studios\' Iron Man 3">Iron Man</a>, người phi thường với khả năng sáng tạo và sức mạnh công nghệ vô song. Anh ta đã đưa ra công nghệ bất tận và chiến đấu bằng bộ giáp đầy sức mạnh. Trong cuộc chiến cuối cùng, <b>Iron Man</b> đã đối mặt với kẻ thù mạnh mẽ là <b>Thanos</b>, người muốn sử dụng <b>S Infinity Stones</b> để thống trị vũ trụ. Nhưng <b>Iron Man</b> đã hy sinh bản thân để đánh bại <b>Thanos</b> và cứu cả vũ trụ.</p>', unsafe_allow_html=True)
    with st.expander('Tìm hiểu thêm...'):
        st.markdown('''1. Trang bị và khả năng đặc biệt: Iron Man có bộ giáp công nghệ cao gồm nhiều loại vũ khí và tính năng đặc biệt như chùm tia phun lửa, tia laser, tấm chắn năng lượng, phản ứng cực nhanh và khả năng bay.

2. Chiến công:
    - Iron Man đã chiến đấu và đánh bại nhiều kẻ thù nguy hiểm trong vũ trụ Marvel. Anh đã đối mặt với Whiplash, Mandarin, Ultron và Thanos. Iron Man đã cống hiến và đóng góp quan trọng trong việc ngăn chặn các kế hoạch độc ác và bảo vệ vũ trụ. 
    - Anh cũng đã đối mặt với nhiều tên tội phạm khác và chiến thắng trong các trận đấu khó khăn.''')
cols = st.columns(2)
with cols[0]:
    st.markdown('<p style="text-align: justify">Cùng lúc đó, có một người tên là <a href="marvel.com/movies/captain-america-civil-war" title="Marvel Studios\' Captain America: Civil War">Captain America</a>. Anh là một người lính từ thế kỷ 20, đã được cải tạo gen để có sức mạnh siêu phàm và tốc độ vượt trội. <b>Captain America</b> luôn đứng vững trước mọi thử thách, trở thành biểu tượng của sự dũng cảm và lòng trung thành. Anh dẫn đầu đội <b>Avengers</b> - một nhóm siêu anh hùng với mục tiêu bảo vệ Trái Đất và toàn bộ vũ trụ khỏi sự đe dọa.</p>', unsafe_allow_html=True)
    with st.expander('Tìm hiểu thêm...'):
        st.markdown('''1. Trang bị và khả năng đặc biệt: 
    - Khiến trang bằng hợp kim Vibranium có khả năng chống đạn, có thể phản chiếu năng lượng và chống lại các tấn công.
    - Siêu sức mạnh: sức mạnh vượt trội và khả năng siêu nhân, cho phép anh vượt qua giới hạn của cơ thể con người bình thường.
    
2. Chiến công:
    - Captain America đã chiến đấu và đánh bại tổ chức Hydra, Red Skull, Loki, Winter Soldier và Thanos. 
    - Anh đã tham gia vào các trận chiến quan trọng trong vũ trụ Marvel và đóng góp sự bảo vệ và chiến thắng cho các nhóm Avengers.
''')
with cols[1]:
    st.image('picture/captain.jpg', width=350)
cols = st.columns(2)
with cols[0]:
    st.image('picture/thor.jpg', width=350)
with cols[1]:
    st.markdown('<p style="text-align: justify">Trong khi đó, <a href="https://www.marvel.com/movies/thor-love-and-thunder" title="Thor: Love and Thunder">Thor</a>, vị thần sấm sét từ Asgard, đã đến Trái Đất để tìm kiếm sức mạnh cổ đại và chiến đấu chống lại những thế lực đen tối. Với cây búa mạnh mẽ Mjolnir, <b>Thor</b> đã đối mặt với những thử thách khắc nghiệt và sẵn sàng hy sinh mọi thứ để bảo vệ vũ trụ.</p>', unsafe_allow_html=True)
    with st.expander('Tìm hiểu thêm...'):
        st.markdown('''
1. Trang bị và khả năng đặc biệt:
    - Thor sử dụng Mjolnir, một cây búa thần mạnh mẽ từ kim loại Uru, mang lại cho anh khả năng bay và kiểm soát sấm sét, cùng với siêu sức mạnh và kỹ năng chiến đấu đáng kinh ngạc
2. Chiến công:
    - Thor đã chiến đấu và đánh bại Loki, Malekith, Hela, Thanos và đóng góp quan trọng trong việc ngăn chặn sự hủy diệt vũ trụ. 
    - Anh đã tham gia vào các trận chiến đầy hào hùng và đánh bại những kẻ thù nguy hiểm, bảo vệ vũ trụ Marvel cùng với đồng đội Avengers và các nhân vật khác.''')
st.markdown('<p style="text-align: justify">Nhưng không chỉ riêng các anh hùng nam mạnh mẽ, Trái Đất cũng có những nữ siêu anh hùng tài ba. <a href="https://www.marvel.com/movies/black-widow" title="Marvel Studios\' Black Widow">Black Widow</a>, một đặc vụ giỏi với khả năng chiến đấu và bí mật vượt trội. <a href="https://www.youtube.com/watch?v=boWCj0MbW1M&ab_channel=FilmRoyalty" title="SCARLET WITCH (2023) With Elizabeth Olsen & Kathryn Hahn">Scarlet Witch</a>, có khả năng điều khiển năng lượng và tạo ra thực tại ảo. Và <a href="https://www.marvel.com/movies/the-marvels" title="Captain Marvel 2">Captain Marvel</a>, một người phụ nữ với sức mạnh siêu nhiên và tốc độ ánh sáng.</p>', unsafe_allow_html=True)

cols = st.columns(3)
with cols[0]:
    st.image('picture/black.jpg')
    with st.expander('Tìm hiểu thêm...'):
        st.markdown('''
1. Trang bị và khả năng đặc biệt:
    - Black Widow sở hữu kỹ thuật võ thuật, khả năng gián điệp và sử dụng nhiều loại vũ khí phá huỷ và công cụ gián điệp.
  
2. Chiến công:
    - Black Widow đã tham gia vào cuộc chiến chống lại tổ chức Hydra, hợp tác với Iron Man và Avengers chống lại Ultron và Thanos, đấu tranh với Winter Soldier và đối mặt với Taskmaster. 
    - Cô đã đạt được nhiều chiến công quan trọng trong vai trò là một điệp viên và thành viên của Avengers.
        ''')
with cols[1]:
    st.image('picture/Witch.jpg')
    with st.expander('Tìm hiểu thêm...'):
        st.markdown('''
1. Trang bị và khả năng đặc biệt:
    - Scarlet Witch sở hữu khả năng siêu năng lượng và sức mạnh siêu nhân, cho phép cô tạo ra trận động lực ma thuật và thực hiện các hành động ngoại viện.
    
2. Chiến công:
    - Scarlet Witch đã chiến đấu và thành công trong các trận đối đầu với Ultron, Proxima Midnight, Corvus Glaive và Thanos. 
    - Cô đã đóng góp quan trọng vào trận chiến cuối cùng chống lại Thanos và đội quân của hắn.
        ''')
with cols[2]:
    st.image('picture/captain_marvel.jpg')
    with st.expander('Tìm hiểu thêm...'):
        st.markdown('''
1. Trang bị và khả năng đặc biệt:
    - Captain Marvel có sức mạnh siêu nhân và khả năng bay, được cung cấp bởi năng lượng từ Tesseract, và sử dụng tia năng lượng từ tay và trang phục bền bỉ để chiến đấu.

2. Chiến công:
    - Captain Marvel, với sức mạnh siêu nhân và trang bị đặc biệt, đã đánh bại Kree, Yon-Rogg, Skrulls và đóng góp quan trọng trong trận chiến cuối cùng chống lại Thanos và đội quân của hắn.
        ''')
cols = st.columns(2)
with cols[0]:
    st.write("<br/><br/>", unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify">Cuộc chiến giữa các siêu anh hùng và kẻ thù không chỉ diễn ra trên Trái Đất mà còn trên các hành tinh khác nhau của vũ trụ. Những cuộc gặp gỡ, liên minh và chiến đấu đầy đau thương, nhưng cũng đầy hy vọng và lòng can đảm, đã tạo nên những câu chuyện hấp dẫn và biểu tượng trong thế giới siêu anh hùng MCU.</p>', unsafe_allow_html=True)
with cols[1]:
    st.image('picture/planet.jpg', width=350)
cols = st.columns(2)
with cols[0]:
    st.image('picture/earth.jpg', width=350)
with cols[1]:
    st.write("<br/><br/>", unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify">Dưới sự lãnh đạo của những siêu anh hùng, Trái Đất đã vượt qua biết bao hiểm nguy và trở thành nơi an lành hơn. Những câu chuyện về sự hy sinh, tình yêu và lòng trung thành đã được ghi lại trong lòng người dân và truyền đi từ thế hệ này sang thế hệ khác.</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify"><b>Và cuộc hành trình của siêu anh hùng MCU vẫn tiếp tục, với những câu chuyện mới, những nguy hiểm mới và sự xuất hiện của những siêu anh hùng mới. Trong mỗi trận chiến, họ sẽ tiếp tục chiến đấu, không bao giờ từ bỏ và luôn dành chiến thắng để bảo vệ Trái Đất và vũ trụ khỏi sự tàn phá của cái ác.</b></p>', unsafe_allow_html=True)