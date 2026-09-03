# LaTeX Paper Formatting Notes

# Tables
## Purpose

This note records a practical workaround for formatting `tabular*` environments with `latexindent` in TeXstudio.

The issue is that `latexindent` may align ordinary `tabular` environments correctly while leaving `tabular*` tables unchanged.

---

## Problem

A table written with:

```latex
\begin{tabular*}{\tblwidth}{@{}LLLLLLL@{}}
...
\end{tabular*}
```

may not have its `&` delimiters aligned by `latexindent`.

However, a regular table such as:

```latex
\begin{tabular}{ccc}
...
\end{tabular}
```

is formatted correctly.

The reason is that `latexindent` recognizes and aligns some table environments by default, but `tabular*` may not be handled in the same way in the current configuration.

---

## Working Solution

Wrap the content of `tabular*` with special `%*` comment markers that make `latexindent` treat the block like a normal `tabular` environment.

Example:

```latex
\begin{table}[width=\linewidth,cols=7,pos=h]
    \caption{Comparison on Dataset~2.}
    \label{tab:sota_d2}

    \begin{tabular*}{\tblwidth}{@{}LLLLLLL@{}}

        %* \begin{tabular}
        \toprule
        Method & Params (M) & GMACs & Precision (\%) & Recall (\%) & F1 (\%) & IoU (\%) \\
        \midrule
        U-Net & 31.38 & 177.49 & 85.78$\pm$0.83 & 87.85$\pm$0.79 & 86.80$\pm$0.22 & 76.67$\pm$0.34 \\
        Attention U-Net & 31.91 & 182.64 & 86.18$\pm$0.66 & 87.62$\pm$0.81 & 86.89$\pm$0.25 & 76.82$\pm$0.40 \\
        \bottomrule
        %* \end{tabular}

    \end{tabular*}
\end{table}
```

After running `latexindent`, the rows are aligned approximately as:

```latex
Method          & Params (M) & GMACs  & Precision (\%)  & Recall (\%)     & F1 (\%)          & IoU (\%)         \\
U-Net           & 31.38      & 177.49 & 85.78$\pm$0.83  & 87.85$\pm$0.79  & 86.80$\pm$0.22  & 76.67$\pm$0.34 \\
Attention U-Net & 31.91      & 182.64 & 86.18$\pm$0.66  & 87.62$\pm$0.81  & 86.89$\pm$0.25  & 76.82$\pm$0.40 \\
```

---

## Why This Works

The lines:

```latex
%* \begin{tabular}
...
%* \end{tabular}
```

are ordinary comments from LaTeX's point of view, so they do not affect compilation or the generated PDF.

`latexindent`, however, interprets `%*` markers as a special code block. By labeling the block as `tabular`, it applies the delimiter-alignment behavior that already works for normal `tabular` environments.

This makes the workaround useful for journal templates that use `tabular*` extensively.

---

## Recommended TeXstudio Command

A typical TeXstudio user command is:

```text
"C:\Tools\latexindent\latexindent.exe" -w ?c:ame
```

If a local `.latexindent.yaml` configuration file is also used:

```text
"C:\Tools\latexindent\latexindent.exe" -l -w ?c:ame
```

Where:

- `-w` writes the formatted result back to the current `.tex` file.
- `-l` loads local YAML settings.
- `?c:ame` refers to the current document in TeXstudio.

---

## Safety Recommendation

When trying a new `latexindent` configuration, first write the result to a separate file:

```text
latexindent.exe main.tex -o main-formatted.tex
```

Check the output before switching to in-place formatting with `-w`.

Using Git or another version-control system is also recommended before enabling automatic formatting.

---

## Practical Rule for This Paper

For tables using:

```latex
\begin{tabular*}{...}
```

add:

```latex
%* \begin{tabular}
```

before the table rows and:

```latex
%* \end{tabular}
```

after the final row.

This keeps the PDF unchanged while allowing `latexindent` to align the table source cleanly.

## Footnote
When formatting result-comparison tables in the LaTeX paper, keep the table caption concise and move the statistical-reporting explanation into a left-aligned note below the table.

Use this note exactly:

\textit{Note:} Values are reported as mean$\pm$sample SD across independent training seeds. The best result is shown in bold, and the second-best result is underlined.

Formatting requirements:
- Keep the table itself centered.
- Place the note directly below the table.
- Align the note to the left edge of the table, not centered.
- Use \footnotesize for the note.
- Prefer wrapping the note in a minipage with width \tblwidth and \raggedright so that it aligns with the table width.
- Do not include the statistical-reporting sentence in the caption.
- Use bold formatting for the best mean value and underline formatting for the second-best mean value.
example: 
\vspace{2pt}
\begin{minipage}{\tblwidth}
\raggedright
\footnotesize
\textit{Note:} Values are reported as mean$\pm$sample SD across independent training seeds.
The best result is shown in bold, and the second-best result is underlined.
\end{minipage}
