# Cấu trúc kho mã nguồn

[English](../en/repository-structure.md) | [Tiếng Việt](repository-structure.md)

Đây là bản dịch tiếng Việt. Nếu có khác biệt, bản tiếng Anh là nguồn chuẩn.

`ai-research-template` sử dụng hai trục tổ chức khác nhau có chủ đích cho đầu vào và đầu ra nghiên cứu.

## Hai trục tổ chức

Đầu vào ưu tiên bộ dữ liệu:

```text
data/<dataset>/{raw,interim,processed}
```

Đầu ra ưu tiên thí nghiệm:

```text
experiments/<experiment>/<dataset>/
```

Cách này giúp dễ kiểm tra nguồn gốc từng bộ dữ liệu, đồng thời giữ toàn bộ bằng chứng cho một câu hỏi nghiên cứu ở cùng nơi. Kết quả liên bộ dữ liệu nằm trong `experiments/<experiment>/summary/`.

## Trách nhiệm của từng thư mục

### `data/`

Mỗi bộ dữ liệu là một thực thể nghiên cứu độc lập và có README riêng. `raw/` là bất biến, `interim/` chứa biến đổi chưa hoàn tất, còn `processed/` chứa dữ liệu sẵn sàng cho thí nghiệm. Git bỏ qua dữ liệu dung lượng lớn nhưng theo dõi tài liệu và tệp giữ chỗ. Thư mục gốc này chứa dữ liệu thật; `src/project/data/` chứa mã xử lý dữ liệu.

### `notebooks/`

`exploration/<dataset>/` dành cho khảo sát và giả thuyết theo bộ dữ liệu. `analysis/` dành cho phân tích liên bộ dữ liệu/thí nghiệm, thống kê, phân tích lỗi và hình cho bài báo. Notebook có thể mang tính khám phá, nhưng logic tái sử dụng hoặc ảnh hưởng tính đúng đắn của kết quả phải được chuyển vào `src/`.

### `src/project/`

Đây là package Python có thể import. Bắt đầu bằng module nhỏ và chỉ tách khi độ phức tạp thực tế yêu cầu. `project` là tên giữ chỗ và nên được đổi trong dự án thật.

### `configs/` và `experiments/`

`configs/` chứa cấu hình khởi đầu có thể chỉnh sửa và tái sử dụng, nhóm theo bộ dữ liệu, mô hình và thí nghiệm. Thư mục thí nghiệm là hồ sơ bất biến của lần chạy thật. `config.yaml` là bản chụp cấu hình đã phân giải đầy đủ, không chỉ trỏ đến cấu hình dùng chung có thể thay đổi. Kết quả từng bộ dữ liệu nằm dưới thí nghiệm; so sánh nằm trong `summary/`.

### `docs/`, `paper/`, `website/` và `.agent/`

`docs/en/` là tài liệu chuẩn và `docs/vi/` chứa bản dịch tương ứng. `paper/` là workspace LaTeX Elsevier CAS: toàn bộ bài báo nằm trong một `main.tex`, hình nằm trong `figs/`, và skill viết bài cục bộ hướng dẫn agent AI. `website/` là dashboard dự án không cần dependency, chỉ tổng hợp các bằng chứng chuẩn chứ không thay thế chúng. `.agent/` chứa ngữ cảnh vận hành hiện tại và quyết định lâu dài, không phải bản ghi hội thoại hay lịch sử thí nghiệm thứ hai. `CHANGELOG.md` ghi các phiên bản và cập nhật đáng chú ý.

## Nội dung nên đưa vào Git

Theo dõi mã nguồn, notebook đáng lưu giữ, cấu hình, metadata bộ dữ liệu, metric nhỏ, bảng, hình, ghi chú thí nghiệm và quyết định. Thông thường không theo dõi dữ liệu lớn, checkpoint, tensor sinh ra, log rất lớn, cache, môi trường và đầu ra tạm. Nếu artifact lớn là thiết yếu, hãy ghi nơi lưu trữ và checksum kiểm tra toàn vẹn.
