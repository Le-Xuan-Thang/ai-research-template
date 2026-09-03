# Mẫu dự án nghiên cứu AI

[English](README.md) | **Tiếng Việt**

> Đây là bản dịch tiếng Việt của `README.md`.
> Trong trường hợp có khác biệt, bản tiếng Anh là nguồn chuẩn.

[![Giấy phép: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](pyproject.toml)

`ai-research-template` là mẫu dự án gọn nhẹ, thân thiện với AI dành cho nghiên cứu AI và machine learning có thể tái lập trên nhiều bộ dữ liệu. Mẫu cung cấp quy ước rõ ràng để nhà nghiên cứu và agent AI tổ chức dữ liệu, notebook, mã tái sử dụng, cấu hình, bằng chứng thực nghiệm, tài liệu và bài báo.

Khác với mẫu phần mềm hoặc production ML thông thường, dự án coi khám phá và khả năng truy vết khoa học là trọng tâm. Mẫu chủ động không đưa vào triển khai, MLOps hay hạ tầng doanh nghiệp.

## Vì sao dùng mẫu này?

- Quản lý độc lập nhiều bộ dữ liệu trong cùng một câu hỏi nghiên cứu.
- Lưu cấu hình chính xác và bằng chứng phía sau từng kết quả quan trọng.
- Sử dụng notebook linh hoạt mà không giữ logic tái sử dụng chỉ trong notebook.
- Giúp nhà nghiên cứu và agent AI tiếp tục công việc từ ngữ cảnh ngắn gọn, lâu dài.
- Chuyển tự nhiên từ khám phá dữ liệu sang thí nghiệm, phân tích và bản thảo Elsevier.

## Nguyên tắc cốt lõi

Hai quy tắc thư mục quan trọng nhất:

```text
data/                              experiments/
├── dataset_a/                     └── exp001_baseline/
│   ├── raw/                           ├── config.yaml
│   ├── interim/                       ├── dataset_a/
│   └── processed/                     ├── dataset_b/
└── dataset_b/                         └── summary/

bộ dữ liệu -> giai đoạn xử lý       thí nghiệm -> bộ dữ liệu -> kết quả
```

Dữ liệu raw là bất biến. Bảng, biểu đồ và kết luận liên bộ dữ liệu nằm trong `summary/` của thí nghiệm. Logic nghiên cứu tái sử dụng nằm trong `src/`; khám phá dữ liệu và phân tích liên thí nghiệm vẫn là workflow notebook hạng nhất.

## Cấu trúc kho mã nguồn

```text
data/<dataset>/                  Dữ liệu và nguồn gốc theo giai đoạn xử lý
notebooks/exploration/<dataset>/ Khảo sát, trực quan hóa và giả thuyết
notebooks/analysis/              Phân tích liên bộ dữ liệu và thí nghiệm
src/project/                     Package Python giữ chỗ có thể tái sử dụng
configs/                         Cấu hình dữ liệu, mô hình và thí nghiệm
experiments/<experiment>/        Bản chụp cấu hình và kết quả từng bộ dữ liệu
docs/{en,vi}/                    Tài liệu tiếng Anh chuẩn và bản dịch tiếng Việt
paper/                           Bản thảo Elsevier CAS một tệp và hình bài báo
website/                         Dashboard dự án không cần dependency
.agent/                          Ngữ cảnh, bàn giao và quyết định lâu dài
```

Xem [cấu trúc kho mã nguồn chi tiết](docs/vi/repository-structure.md).

## Bắt đầu nhanh

1. Trên GitHub, chọn **Use this template**, tạo kho nghiên cứu mới và clone về máy.
2. Nếu có [`uv`](https://docs.astral.sh/uv/), chuẩn bị môi trường Python đã ghim và cài dự án:

   ```bash
   uv python install
   uv sync
   uv run python -c "import project"
   ```

   Nếu không có `uv`, dùng phương án chuẩn:

   ```bash
   python -m venv .venv
   # Kích hoạt .venv phù hợp với shell, sau đó:
   python -m pip install -e .
   ```

3. Đổi tên `src/project/` thành tên package mong muốn. Cập nhật `[project].name` trong `pyproject.toml`; việc tìm package theo bố cục `src/` đã được cấu hình.
4. Thay mô tả mẫu trong `README.md` và xác định mục tiêu hiện tại trong `.agent/state.md`.
5. Đăng ký từng bộ dữ liệu trong `data/<dataset_name>/` và thêm cấu hình runtime trong `configs/datasets/`.
6. Khám phá dữ liệu trong `notebooks/exploration/<dataset_name>/`, chuyển logic tái sử dụng sang `src/<project_package>/`.
7. Định nghĩa cấu hình mô hình/thí nghiệm, rồi lưu từng lần chạy thật trong `experiments/<experiment_id>/` cùng bản chụp `config.yaml` đã phân giải.

Package được import bằng `project`, không phải `src.project`, cho đến khi bạn đổi tên.

## Nghiên cứu đa bộ dữ liệu

Mỗi bộ dữ liệu quản lý nguồn, phiên bản, giấy phép, cách chia tập, các giai đoạn tiền xử lý và hạn chế trong `data/<dataset>/README.md`. Một thí nghiệm có thể đánh giá cùng giả thuyết trên nhiều bộ dữ liệu; metric của từng bộ dữ liệu nằm dưới thí nghiệm và `summary/` lưu bằng chứng tổng hợp có thể so sánh.

`example_a`, `example_b` và `exp001_baseline` chỉ là metadata hướng dẫn. Chúng không chứa dữ liệu giả hoặc kết quả được tuyên bố.

## Quy trình thí nghiệm

Bắt đầu từ tệp tái sử dụng trong `configs/`, phân giải mọi thiết lập quan trọng, rồi lưu bản chụp cấu hình cạnh lần chạy. Đưa metric nhỏ, ghi chú, tóm tắt và nguồn gốc vào Git; không đưa dữ liệu lớn, checkpoint, tensor và log lớn vào Git. Không ghi đè thí nghiệm đã hoàn tất—hãy tạo định danh mô tả mới như `exp004_ablation_no_augmentation`.

Xem [quy trình nghiên cứu đầy đủ](docs/vi/research-workflow.md).

## Quy trình agent AI

Agent đọc [AGENTS.md](AGENTS.md), [.agent/state.md](.agent/state.md) và [.agent/handoff.md](.agent/handoff.md) nếu có trước khi sửa artifact nghiên cứu. Quyết định khoa học hoặc cấu trúc lâu dài nằm trong `.agent/decisions/`, không phải log hội thoại. Công việc bản thảo còn phải tuân theo [`write-ai-paper` skill](paper/Skills/write-ai-paper/SKILL.md) cục bộ.

## Tài liệu

Tiếng Anh là nguồn chuẩn cho nội dung kỹ thuật và nội dung dành cho máy. Bản dịch tiếng Việt của tài liệu dành cho người đọc nằm tại đường dẫn tương ứng trong `docs/vi/`. Mã nguồn, cấu hình, định danh thí nghiệm, `AGENTS.md` và `.agent/` không được nhân đôi theo ngôn ngữ.

- [Cấu trúc kho mã nguồn](docs/vi/repository-structure.md)
- [Quy trình nghiên cứu](docs/vi/research-workflow.md)
- [Tài liệu tiếng Anh](docs/en/repository-structure.md)
- [Dashboard dự án](website/index.html)
- [Lịch sử thay đổi](CHANGELOG.md)

## Đóng góp

Các cải tiến có phạm vi rõ ràng luôn được chào đón. Vui lòng đọc [CONTRIBUTING.md](CONTRIBUTING.md) trước khi đề xuất thay đổi cấu trúc và giữ mọi đóng góp gọn nhẹ, định hướng nghiên cứu.

## Trích dẫn

Nếu mẫu này hỗ trợ workflow nghiên cứu của bạn, metadata trích dẫn nằm trong [CITATION.cff](CITATION.cff). Hãy thay metadata cấp kho mã nguồn khi tạo dự án mới từ mẫu.

## Giấy phép

Dự án này được phát hành theo giấy phép MIT. Xem [LICENSE](LICENSE) để biết chi tiết. Các tài sản mẫu Elsevier của bên thứ ba trong `paper/` giữ nguyên thông báo bản quyền và điều khoản riêng.

