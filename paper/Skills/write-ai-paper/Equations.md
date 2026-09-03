# Nguyên tắc trình bày phương trình và ký hiệu toán học trong bài báo LaTeX

## 1. Trình bày phương trình

Các phương trình quan trọng, đặc biệt là các phương trình được đề cập lại trong nội dung bài báo, phải được trình bày dưới dạng phương trình đánh số. Trong LaTeX, nên sử dụng môi trường

```latex
\begin{equation}
    ...
\end{equation}
```

và gán nhãn bằng lệnh `\label{}` để có thể tham chiếu về sau. Ví dụ:

```latex
\begin{equation}
    \mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b},
    \label{eq:linear}
\end{equation}
```

Đối với các phương trình gồm nhiều dòng hoặc một hệ phương trình có quan hệ với nhau, có thể sử dụng các môi trường phù hợp như `align`, `aligned`, hoặc `split`. Không nên sử dụng `$$ ... $$` trong bài báo khoa học.

---

## 2. Giải thích các ký hiệu ngay sau phương trình

Mọi ký hiệu xuất hiện lần đầu trong một phương trình phải được định nghĩa rõ ràng. Nếu ký hiệu chưa được giải thích trước đó, phần giải thích nên được đặt ngay sau phương trình.

Thông thường, phần giải thích bắt đầu bằng **where**, ví dụ:

```latex
\begin{equation}
    \mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b},
    \label{eq:linear}
\end{equation}
where $\mathbf{x} \in \mathbb{R}^{n}$ denotes the input vector,
$\mathbf{W} \in \mathbb{R}^{m \times n}$ is the weight matrix,
$\mathbf{b} \in \mathbb{R}^{m}$ is the bias vector, and
$\mathbf{y} \in \mathbb{R}^{m}$ denotes the output vector.
```

Không được đưa ra một phương trình chứa nhiều ký hiệu mới nhưng không giải thích ý nghĩa hoặc kích thước của chúng.

Khi cần thiết, ngoài ý nghĩa vật lý hoặc toán học của biến, nên chỉ rõ **dimension** của vector, matrix hoặc tensor để tránh sự mơ hồ.

---

## 3. Mọi phương trình được sử dụng lại phải được tham chiếu

Một phương trình đã được đánh số và được đề cập trong phần nội dung phải được tham chiếu rõ ràng. Không nên viết các câu mơ hồ như

> "The loss is calculated using the following equation."

mà sau đó không nhắc lại số phương trình khi phân tích hoặc sử dụng nó.

Nên sử dụng:

```latex
Eq.~\eqref{eq:loss}
```

Ví dụ:

```latex
The classification loss is calculated according to
Eq.~\eqref{eq:loss}.
```

hoặc khi nằm đầu câu:

```latex
Equation~\eqref{eq:loss} defines the objective function used
during model training.
```

Không nên nhập số phương trình thủ công, chẳng hạn:

```latex
Eq. (5)
```

vì số thứ tự có thể thay đổi khi thêm hoặc xóa phương trình. Luôn sử dụng `\label{}` và `\eqref{}`.

---

## 4. Phương trình phải có vai trò rõ ràng trong nội dung bài báo

Không nên đưa một phương trình vào bài báo nhưng sau đó không giải thích, không sử dụng hoặc không đề cập đến nó.

Mỗi phương trình quan trọng phải có ít nhất một trong các vai trò sau:

* định nghĩa một đại lượng;
* mô tả một phương pháp;
* mô tả một phép biến đổi;
* xây dựng một hàm mục tiêu;
* xác định một đặc trưng;
* hoặc làm cơ sở cho các phương trình tiếp theo.

Các phương trình phải được kết nối với phần diễn giải bằng văn bản để người đọc hiểu **tại sao phương trình đó xuất hiện** và **nó được sử dụng như thế nào trong phương pháp đề xuất**.

---

## 5. Bảo đảm tính logic và nhất quán giữa các phương trình

Toàn bộ hệ thống phương trình trong bài báo phải nhất quán về mặt toán học và ký hiệu.

Nếu một đại lượng được ký hiệu là

```latex
\mathbf{x}
```

ở một phương trình, không được tùy ý đổi thành

```latex
\mathbf{X}
```

hoặc

```latex
x
```

ở phương trình khác nếu chúng vẫn biểu diễn cùng một đối tượng.

Ví dụ, nếu đã định nghĩa

```latex
\mathbf{x} \in \mathbb{R}^{n}
```

là một vector đầu vào, thì ký hiệu `\mathbf{x}` phải được duy trì xuyên suốt bài báo.

Tương tự, nếu

```latex
\mathbf{W} \in \mathbb{R}^{m \times n}
```

là một ma trận trọng số, không nên chuyển sang sử dụng `W`, `\mathbf{w}`, hoặc một ký hiệu khác mà không có lý do hoặc định nghĩa mới.

Đặc biệt cần kiểm tra sự tương thích về kích thước trong các phép toán ma trận. Ví dụ,

```latex
\mathbf{W}\mathbf{x}
```

chỉ hợp lệ nếu

```latex
\mathbf{W} \in \mathbb{R}^{m \times n},
\qquad
\mathbf{x} \in \mathbb{R}^{n}.
```

---

## 6. Quy ước đối với đại lượng vô hướng

Các đại lượng vô hướng (*scalars*) được biểu diễn bằng chữ cái thường hoặc chữ cái Hy Lạp dạng nghiêng, ví dụ

```latex
$x$, $N$, $\mu$, $\kappa$, $\lambda$, $\eta$
```

Ví dụ:

```latex
\eta = 10^{-3}
```

trong đó `\eta` là learning rate.

Không nên sử dụng chữ in đậm cho đại lượng vô hướng.

---

## 7. Quy ước đối với vector

Vector nên được biểu diễn bằng **chữ thường in đậm**, ví dụ

```latex
\mathbf{x}, \mathbf{y}, \mathbf{w}
```

Nếu không có giải thích khác, vector nên được mặc định hiểu là **vector cột**:

```latex
\mathbf{x}
=
[x_1; x_2; \ldots; x_n]
\in \mathbb{R}^{n}.
```

Trong khi đó,

```latex
[x_1, x_2, \ldots, x_n]
```

biểu diễn một vector hàng.

Cần chú ý sự khác biệt giữa:

```latex
[x_1, x_2, \ldots, x_n]
```

và

```latex
[x_1; x_2; \ldots; x_n].
```

Dấu phẩy `,` biểu thị việc sắp xếp các phần tử theo chiều ngang, trong khi dấu chấm phẩy `;` biểu thị việc xếp chúng theo chiều dọc. Quy ước này tương đồng với cách biểu diễn trong MATLAB.

---

## 8. Quy ước đối với ma trận

Ma trận nên được biểu diễn bằng **chữ hoa in đậm**, ví dụ

```latex
\mathbf{X}, \mathbf{Y}, \mathbf{W}
```

Ví dụ:

```latex
\mathbf{X} \in \mathbb{R}^{m \times n}.
```

Một ma trận có thể được biểu diễn thông qua các vector cột:

```latex
\mathbf{X}
=
[\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_n].
```

Trong trường hợp này, các vector

```latex
\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_n
```

được xếp cạnh nhau từ trái sang phải để tạo thành ma trận `\mathbf{X}`.

Ngược lại,

```latex
\mathbf{X}
=
[\mathbf{x}_1;
 \mathbf{x}_2;
 \ldots;
 \mathbf{x}_m]
```

biểu diễn việc xếp các vector theo chiều từ trên xuống dưới. Khi sử dụng cách biểu diễn này, kích thước của các vector phải tương thích để phép ghép ma trận có ý nghĩa.

---

## 9. Ký hiệu phần tử của ma trận

Phần tử nằm tại hàng thứ (i) và cột thứ (j) của ma trận

```latex
\mathbf{X}
```

được ký hiệu là

```latex
x_{ij}.
```

Ví dụ:

```latex
x_{ij}
```

là phần tử ở hàng (i), cột (j) của `\mathbf{X}`.

Do đó cần duy trì sự tương ứng giữa chữ hoa và chữ thường:

```latex
\mathbf{X} \leftrightarrow x_{ij}.
```

Tương tự:

```latex
\mathbf{W} \leftrightarrow w_{ij}.
```

---

## 10. Ký hiệu vector cột của một ma trận

Nếu

```latex
\mathbf{W}
=
[\mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_n],
```

thì

```latex
\mathbf{w}_i
```

được hiểu là vector cột thứ (i) của ma trận `\mathbf{W}`.

Cần chú ý sự tương ứng giữa ký hiệu chữ hoa và chữ thường:

```latex
\mathbf{W}
```

biểu diễn toàn bộ ma trận, trong khi

```latex
\mathbf{w}_i
```

biểu diễn một vector cột của ma trận đó và

```latex
w_{ij}
```

biểu diễn một phần tử cụ thể của ma trận.

Có thể hiểu theo hệ thống:

```latex
\mathbf{W}
    \quad \text{: matrix},
```

```latex
\mathbf{w}_i
    \quad \text{: the $i$th column vector of } \mathbf{W},
```

```latex
w_{ij}
    \quad \text{: the element in row $i$ and column $j$}.
```

---

## 11. Phân biệt rõ scalar, vector và matrix

Một quy ước đơn giản nên được duy trì xuyên suốt bài báo là:

| Loại đại lượng        | Ký hiệu                     | Ví dụ                              |
| --------------------- | --------------------------- | ---------------------------------- |
| Scalar                | chữ nghiêng                 | (x,\alpha,\lambda,N)               |
| Vector                | chữ thường in đậm           | (\mathbf{x},\mathbf{y},\mathbf{w}) |
| Matrix                | chữ hoa in đậm              | (\mathbf{X},\mathbf{Y},\mathbf{W}) |
| Phần tử vector        | chữ thường có một chỉ số    | (x_i)                              |
| Phần tử matrix        | chữ thường có hai chỉ số    | (x_{ij})                           |
| Vector cột của matrix | chữ thường in đậm có chỉ số | (\mathbf{x}_i)                     |

Quy ước này đặc biệt quan trọng đối với các bài báo liên quan đến machine learning, signal processing, structural health monitoring, và deep learning, nơi một ký hiệu có thể xuất hiện trong nhiều phương trình liên tiếp.

---

## 12. Chỉ số phải có ý nghĩa thống nhất

Các chỉ số như (i), (j), (k), (n), (t) cần được sử dụng có hệ thống.

Ví dụ, nếu đã quy định

```latex
i = 1,2,\ldots,N
```

là chỉ số mẫu dữ liệu, thì không nên sử dụng (i) ở một phần khác để biểu diễn frequency bin nếu điều đó có thể gây nhầm lẫn.

Có thể thiết lập quy ước như:

```latex
i
```

cho sample index,

```latex
t
```

cho time index,

```latex
f
```

hoặc `k` cho frequency index,

```latex
c
```

cho class index.

Nếu cần thay đổi ý nghĩa của một index, phải định nghĩa rõ ràng trong ngữ cảnh tương ứng.

---

## 13. Thống nhất ký hiệu toán học với phần mô tả thuật toán

Các ký hiệu xuất hiện trong equation, algorithm, figure, table và phần mô tả bằng văn bản phải thống nhất.

Ví dụ, nếu loss function được định nghĩa là

```latex
\mathcal{L}
```

trong Eq.~`\eqref{eq:loss}`, thì trong Algorithm cũng nên sử dụng

```latex
\mathcal{L}
```

thay vì thay đổi thành `L`, `loss`, hoặc `\mathcal{J}` nếu chúng cùng biểu diễn một đại lượng.

Tương tự, nếu số lượng lớp được ký hiệu là (C), thì (C) nên được duy trì trong toàn bộ phần Methodology thay vì lúc dùng (C), lúc dùng (K).

---

## 14. Phương trình là một phần của câu văn

Equation không phải là một đối tượng tách biệt hoàn toàn khỏi văn bản mà là một phần của câu. Vì vậy, phương trình cũng cần có dấu câu phù hợp.

Ví dụ:

```latex
The transformed signal is defined as
\begin{equation}
    \mathbf{z} = f(\mathbf{x}),
    \label{eq:transform}
\end{equation}
where $\mathbf{x}$ denotes the input signal and
$\mathbf{z}$ denotes the transformed representation.
```

Dấu phẩy sau phương trình là cần thiết vì câu vẫn tiếp tục với từ `where`.

Nếu câu kết thúc tại equation, có thể đặt dấu chấm:

```latex
\begin{equation}
    \hat{y} = \arg\max_c p_c.
\end{equation}
```

---

## 15. Không lạm dụng equation

Các biểu thức toán học đơn giản nằm trong câu nên được viết dưới dạng inline math, ví dụ:

```latex
The input signal $\mathbf{x} \in \mathbb{R}^{N}$ contains
$N$ sampling points.
```

Không cần tạo một equation riêng chỉ để viết:

```latex
N = 1024.
```

Môi trường `equation` nên dành cho những biểu thức có ý nghĩa toán học hoặc phương pháp luận rõ ràng, đặc biệt là những công thức cần được tham chiếu.

---

## 16. Kiểm tra tính nhất quán trước khi hoàn thành manuscript

Trước khi hoàn thành bài báo, cần kiểm tra toàn bộ phần toán học theo các câu hỏi sau:

* Mọi ký hiệu có được định nghĩa tại lần xuất hiện đầu tiên hay chưa?
* Một ký hiệu có bị sử dụng cho hai đại lượng khác nhau hay không?
* Cùng một đại lượng có bị biểu diễn bằng nhiều ký hiệu khác nhau hay không?
* Scalar, vector và matrix có được phân biệt nhất quán hay không?
* Dimension của các phép toán matrix/vector có hợp lệ hay không?
* Các phương trình quan trọng có `\label{}` hay chưa?
* Các phương trình được đề cập trong nội dung có được gọi bằng `\eqref{}` hay chưa?
* Các ký hiệu trong equation, algorithm, figure và phần văn bản có thống nhất hay không?
* Index của các biến có được sử dụng nhất quán hay không?
* Equation có được giải thích về ý nghĩa và vai trò trong phương pháp hay chưa?

Nguyên tắc quan trọng nhất là: **một hệ thống ký hiệu toán học tốt phải cho phép người đọc theo dõi toàn bộ phương pháp mà không phải đoán ý nghĩa của bất kỳ biến, vector, matrix hoặc index nào.**
