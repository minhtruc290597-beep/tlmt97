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
import pandas as pd
import streamlit as st

st.title("📦 Tự động tạo Báo cáo Xuất - Nhập Kho")

# 1. Đọc dữ liệu từ Sheet 1 (hoặc file tải lên)
# Giả sử file excel của bạn tên là 'Nhập_Xuất_Kho_29.10_đã_tạo_Sheet3.xlsx'
file_path = "Nhập_Xuất_Kho_29.10_đã_tạo_Sheet3.xlsx"

try:
  df_sheet1 = pd.read_excel(file_path, sheet_name="Sheet1")

  # 2. Phân loại XUẤT KHO và NHẬP KHO
  # (Tùy theo logic kho của bạn: Ví dụ Bưu cục xuất là HOCHIMINH CENTER là Xuất kho, ngược lại là Nhập kho)
  df_xuat = df_sheet1[df_sheet1["Bưu cục xuất"] == "HOCHIMINH CENTER"]
  df_nhap = df_sheet1[df_sheet1["Bưu cục nhập"] == "HOCHIMINH CENTER"]

  # Hàm gom nhóm dữ liệu theo cấu trúc báo cáo
  def group_data(df):
    if df.empty:
      return pd.DataFrame(
          columns=[
              "Mã Vận Đơn",
              "Bưu cục xuất",
              "Bưu cục nhập",
              "Bưu cục đích",
              "Bưu cục gửi",
              "Tên hàng hóa",
              "Số mã đơn con",
              "Số mã vận đơn",
              "Trọng lượng tính cước (kg)",
              "Tổng số kiện",
          ]
      )

    grouped = (
        df.groupby(
            [
                "Mã vận đơn",
                "Bưu cục xuất",
                "Bưu cục nhập",
                "Bưu cục đích",
                "Bưu cục gửi",
                "Tên hàng hóa",
            ]
        )
        .agg(
            {
                "Mã đơn con": "count",  # Đếm số lượng mã đơn con
                "Trọng lượng tính cước (kg)": "sum",  # Tổng trọng lượng
                "Tổng số kiện": "sum",  # Tổng số kiện
            }
        )
        .reset_index()
    )

    # Đếm số mã vận đơn (mỗi dòng gộp là 1)
    grouped["Số mã vận đơn"] = 1

    # Đổi tên cột cho khớp yêu cầu hiển thị
    grouped.rename(columns={"Mã đơn con": "Số mã đơn con"}, inplace=True)
    return grouped

  # 3. Tạo bảng Báo cáo Tổng Xuất Kho
  st.subheader("🔴 TỔNG XUẤT KHO / 总出库")
  report_xuat = group_data(df_xuat)
  st.dataframe(report_xuat, use_container_width=True)

  # 4. Tạo bảng Báo cáo Tổng Nhập Kho
  st.subheader("🔵 TỔNG NHẬP KHO / 总入库")
  report_nhap = group_data(df_nhap)
  st.dataframe(report_nhap, use_container_width=True)

except Exception as e:
  st.error(f"Lỗi đọc file hoặc xử lý dữ liệu: {e}")
# Dán đoạn code báo cáo xuất nhập kho vào đây
with st.container():
  st.markdown("### 📦 Báo cáo xuất nhập kho")
  st.info("Khu vực này hiển thị thông tin nhập xuất kho.")
