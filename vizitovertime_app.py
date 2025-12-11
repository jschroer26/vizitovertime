import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="VizitOverTime", layout="wide")

st.title("VizitOverTime – WYTOPP Over-Time Visualizations")

st.write(
    "Upload a WYTOPP over-time dataset (one row per Grade × Year × Subject, "
    "no subgroups), then choose a subject and grades to see multi-year trends."
)

# --- File upload ---
uploaded_file = st.file_uploader(
    "Upload WYTOPP over-time data (Excel or CSV)",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Clean column names (handles your newline formatting)
    df.columns = (
        df.columns
          .astype(str)
          .str.replace("\n", " ")
          .str.replace("  ", " ")
          .str.strip()
    )

    st.subheader("Step 1: Preview your data")
    st.dataframe(df.head())

    # --- Identify key columns ---
    required_cols = [
        "School Year",
        "Grade",
        "Subject",
        "Percent Basic and Below",
        "Percent Proficient and Advanced",
        "Number of Students Tested",
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(
            "The following required columns are missing from your file: "
            + ", ".join(missing)
            + ".\n\n"
              "Please make sure your column headers match this template exactly."
        )
    else:
        st.subheader("Step 2: Choose subject and grades")

        # Subject selection
        subjects = sorted(df["Subject"].dropna().unique())
        subject = st.selectbox(
            "Subject",
            options=subjects,
            index=0 if "English" in subjects[0] else 0,
            help="Choose ELA, Math, or Science."
        )

        # Filter by subject
        df_subj = df[df["Subject"] == subject].copy()

        # Grade selection
        grades_available = sorted(df_subj["Grade"].dropna().unique())
        grades_selected = st.multiselect(
            "Grades to display",
            options=grades_available,
            default=grades_available,
        )

        if not grades_selected:
            st.warning("Please select at least one grade.")
        else:
            df_sel = df_subj[df_subj["Grade"].isin(grades_selected)].copy()

            # --- Build summary table: Grade × School Year ---
            group_cols = ["Grade", "School Year"]
            col_basic = "Percent Basic and Below"
            col_prof = "Percent Proficient and Advanced"
            col_n = "Number of Students Tested"

            summary = (
                df_sel
                .groupby(group_cols)
                .agg({
                    col_basic: "mean",
                    col_prof: "mean",
                    col_n: "sum",   # no subgroups, so sum is same as value
                })
                .reset_index()
            )

            st.subheader("Step 3: Grade × Year summary table")
            st.dataframe(summary)

            # --- Visualization: multi-panel stacked bar chart ---
            st.subheader("Step 4: Visualization")

            grades = sorted(summary["Grade"].dropna().unique())

            fig, axes = plt.subplots(
                len(grades), 1,
                figsize=(10, 3.2 * len(grades)),
                sharex=True
            )

            if len(grades) == 1:
                axes = [axes]

            basic_bar = prof_bar = None

            for ax, grade in zip(axes, grades):
                sub = summary[summary["Grade"] == grade].set_index("School Year")

                # Ensure years are ordered logically
                sub = sub.sort_index()

                # Stacked bars
                basic_bar = ax.bar(
                    sub.index.astype(str),
                    sub[col_basic],
                    color="#d4a017"
                )
                prof_bar = ax.bar(
                    sub.index.astype(str),
                    sub[col_prof],
                    bottom=sub[col_basic],
                    color="#1f77b4"
                )

                # N labels
                for i, (year, row) in enumerate(sub.iterrows()):
                    ax.text(
                        i, 102,
                        f"N={int(row[col_n])}",
                        ha="center", va="bottom", fontsize=9
                    )

                ax.set_title(f"Grade {int(grade)} – {subject} Over Time (All Students)")
                ax.set_ylabel("Percent")
                ax.set_ylim(0, 115)

            # Single legend
            fig.legend(
                handles=[basic_bar, prof_bar],
                labels=["Basic & Below", "Proficient & Advanced"],
                loc="upper center",
                ncol=2,
                bbox_to_anchor=(0.5, 1.02),
                fontsize=11
            )

            plt.xlabel("School Year")
            plt.xticks(rotation=45)
            plt.tight_layout()

            st.pyplot(fig)

            # --- Downloads ---

            # 1. Chart as PNG
            buf_png = io.BytesIO()
            fig.savefig(buf_png, format="png", bbox_inches="tight")
            buf_png.seek(0)

            st.download_button(
                label="Download chart as PNG",
                data=buf_png,
                file_name=f"VizitOverTime_{subject.replace(' ', '_')}.png",
                mime="image/png"
            )

            # 2. Summary as Excel
            excel_buf = io.BytesIO()
            with pd.ExcelWriter(excel_buf, engine="openpyxl") as writer:
                summary.to_excel(writer, sheet_name="Summary", index=False)
            excel_buf.seek(0)

            st.download_button(
                label="Download summary as Excel",
                data=excel_buf,
                file_name=f"VizitOverTime_{subject.replace(' ', '_')}_summary.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

else:
    st.info("Upload a WYTOPP over-time file to get started.")
