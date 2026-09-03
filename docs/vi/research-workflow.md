# Quy trình nghiên cứu

[English](../en/research-workflow.md) | [Tiếng Việt](research-workflow.md)

Đây là bản dịch tiếng Việt. Nếu có khác biệt, bản tiếng Anh là nguồn chuẩn.

Đây là workflow mặc định cho dự án nghiên cứu được tạo từ `ai-research-template`.

## 1. Xác định câu hỏi và đăng ký bộ dữ liệu

Viết câu hỏi nghiên cứu cụ thể. Với mỗi bộ dữ liệu, tạo `data/<dataset>/README.md` ghi nguồn, trích dẫn, giấy phép, phiên bản, cách lấy dữ liệu, bố cục, chính sách chia tập, tiền xử lý và hạn chế. Không bao giờ sửa dữ liệu raw tại chỗ.

## 2. Khám phá rồi hợp nhất logic

Dùng `notebooks/exploration/<dataset>/` để khảo sát và thử nhanh giả thuyết. Giữ notebook dễ đọc và ghi rõ đầu vào. Khi logic tải dữ liệu, tiền xử lý, mô hình, metric hoặc vẽ được tái sử dụng—hoặc ảnh hưởng tính đúng đắn khoa học—hãy chuyển nó vào `src/project/` và import từ notebook.

## 3. Cấu hình thí nghiệm

Giữ các phần cấu hình tái sử dụng trong `configs/datasets/`, `configs/models/` và `configs/experiments/`. Phải khôi phục được các thiết lập quan trọng: seed, bộ dữ liệu và phiên bản, cách chia tập, mô hình, optimizer, learning rate, batch size, số epoch, augmentation và giao thức đánh giá.

Trước khi chạy, tạo `experiments/expNNN_name/` và lưu thiết lập đã phân giải đầy đủ vào `config.yaml`. Việc sửa cấu hình dùng chung về sau không được làm thay đổi ý nghĩa kết quả cũ.

Ưu tiên `uv` khi có sẵn: `.python-version` ghim dòng Python dự kiến, `pyproject.toml` khai báo dependency, và cần commit `uv.lock` khi dự án có dependency thật. Chạy lệnh nghiên cứu bằng `uv run` để dùng đúng môi trường đã phân giải.

## 4. Chạy trên nhiều bộ dữ liệu

Ghi đầu ra vào `experiments/<experiment>/<dataset>/`. Lưu metric có cấu trúc nhỏ và metadata hữu ích trong Git. Không lưu checkpoint và log lớn trong Git, nhưng phải ghi cách tìm hoặc tái tạo chúng. Ghi trung thực lần chạy lỗi hoặc một phần thay vì âm thầm thay thế.

Dùng seed xác định khi phù hợp, ghi chi tiết phần mềm/phần cứng có ảnh hưởng đáng kể, đồng thời định nghĩa cách tổng hợp metric và độ bất định. Không so sánh các bộ dữ liệu dùng giao thức không tương thích mà không chú thích khác biệt.

## 5. Tổng hợp và công bố

Đặt bảng, biểu đồ và kết luận liên bộ dữ liệu trong `experiments/<experiment>/summary/`. Dùng `notebooks/analysis/` cho so sánh, ablation, phân tích lỗi, thống kê và sinh hình. Nội dung sẵn sàng công bố có thể chuyển vào `paper/figs/` và tệp duy nhất `paper/main.tex`, đồng thời vẫn giữ liên kết đến thí nghiệm và cấu hình nguồn. Agent AI phải tuân theo `paper/Skills/write-ai-paper/SKILL.md` khi làm việc với bản thảo.

Cập nhật `website/` bằng các điểm nổi bật, kết quả và cột mốc đã được xác minh. Website chỉ là lớp trình bày; giá trị chuẩn vẫn nằm trong hồ sơ thí nghiệm và đầu ra phân tích. Ghi thay đổi đáng chú ý của kho mã nguồn trong `CHANGELOG.md`.

## 6. Duy trì tính liên tục

Cập nhật `.agent/state.md` sau công việc có ý nghĩa. Chỉ dùng `.agent/handoff.md` khi phiên khác cần chỉ dẫn tiếp tục cụ thể. Ghi lựa chọn lâu dài—như giao thức chia tập hoặc định nghĩa metric—trong `.agent/decisions/`. Ghi chú thí nghiệm và Git vẫn là lịch sử chính.
