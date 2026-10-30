import streamlit as st
import pandas as pd
import numpy as np

# 1. Tiêu đề và mô tả ứng dụng
st.title("📊 Ứng dụng Quản lý & Phân tích Dữ liệu")
st.markdown("Chào mừng bạn đến với ứng dụng Streamlit đầu tiên! Dưới đây là các thành phần giao diện cơ bản.")

# 2. Thanh bên (Sidebar) để người dùng nhập thông tin
st.sidebar.header("Cấu hình hiển thị")
user_name = st.sidebar.text_input("Nhập tên của bạn:", "Người dùng")
number_of_rows = st.sidebar.slider("Chọn số dòng dữ liệu mẫu:", 5, 50, 10)

# 3. Hiển thị lời chào cá nhân hóa
st.success(f"Xin chào **{user_name}**! Chúc bạn có một ngày làm việc hiệu quả.")

# 4. Tạo và hiển thị bảng dữ liệu mẫu (DataFrame)
st.subheader("1. Bảng dữ liệu ngẫu nhiên")
data = pd.DataFrame(
    np.random.randn(number_of_rows, 3),
    columns=['Cột A', 'Cột B', 'Cột C']
)
st.dataframe(data) # Hoặc dùng st.table(data)

# 5. Vẽ biểu đồ trực quan hóa dữ liệu
st.subheader("2. Biểu đồ đường (Line Chart)")
st.line_chart(data)

# 6. Nút bấm tương tác
if st.button("Nhấn vào đây để xem thông báo"):
    st.balloons()
    st.info("Tuyệt vời! Bạn đã tương tác thành công với ứng dụng Streamlit.")
import streamlit as st

# Dán đoạn code báo cáo xuất nhập kho vào đây
with st.container():
  st.markdown("### 📦 Báo cáo xuất nhập kho")
  st.info("Khu vực này hiển thị thông tin nhập xuất kho.")
