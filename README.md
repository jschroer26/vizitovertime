# vizitovertime
Absolutely — here is a clean, professional **README.md** for your GitHub repository for **VizitOverTime**.
It matches the tone and style used by educational tools, is admin-friendly, and explains installation, usage, and file requirements clearly.

---

# 📊 VizitOverTime

### *A WYTOPP Multi-Year Data Visualization Tool for Schools*

**VizitOverTime** is a web-based application built with Streamlit that allows educators and administrators to visualize **multi-year WYTOPP performance trends** across subjects and grade levels.
It is designed to complement the original **Vizit** app, which focuses on single-year data snapshots.

This tool makes it easy to track how cohorts perform over time and to identify areas of improvement for instructional planning.

---

## 🚀 Features

### ✅ Multi-year performance visualization

* Generate **stacked bar charts** showing the proportion of students performing:

  * **Basic & Below**
  * **Proficient & Advanced**
* View results for **ELA**, **Math**, or **Science**
* One panel per selected grade (e.g., Grades 3–6)

### ✅ Enrollment labeling

Each bar includes an **N value** (Number of Students Tested), giving context to year-to-year fluctuations.

### ✅ Clean, easy-to-use interface

* Upload your WYTOPP file
* Choose a subject
* Select grades
* Generate and download charts instantly

### ✅ Export options

* **Download PNG** of the chart
* **Download Excel summary** (Grade × Year tables)

### 🔧 Zero coding required

Just upload your dataset — VizitOverTime handles the rest.

---

## 📁 Required Dataset Format

Your dataset must include **one row per Grade × Year × Subject**, with no subgroup rows.

A valid file must contain these exact column names:

| Required Column                   | Description                                               |
| --------------------------------- | --------------------------------------------------------- |
| `School Year`                     | The academic year (e.g., 2020–21)                         |
| `Grade`                           | Grade level (e.g., 3, 4, 5, 6)                            |
| `Subject`                         | ELA, Math, or Science                                     |
| `Percent Basic and Below`         | Percentage of students scoring Basic or Below             |
| `Percent Proficient and Advanced` | Percentage of students scoring Proficient or Advanced     |
| `Number of Students Tested`       | Student count (N) for that grade and subject in that year |

**Formats supported:** `.xlsx`, `.xls`, `.csv`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourname/VizitOverTime.git
cd VizitOverTime
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run vizitovertime_app.py
```

The app will open at:

```
http://localhost:8501
```

---

## 🌐 Deployment

VizitOverTime is fully compatible with:

* **Streamlit Community Cloud**
* **Private institutional Streamlit servers**
* Static links from school/district websites

To deploy on Streamlit Cloud:

1. Push this repository to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Select *New App* and choose this repo
4. Deploy — your app gets its own web URL instantly

---

## 🧭 Using VizitOverTime

1. Upload your WYTOPP over-time dataset
2. Select a subject (ELA, Math, Science)
3. Choose the grade levels you want
4. The app generates:

   * A summary table
   * A multi-panel stacked bar chart
5. Download the PNG or Excel summary if desired

This tool is designed to support:

* School improvement teams
* Instructional coaches
* Principals
* District assessment staff
* Research partners

---

## 🤝 Contributing

Pull requests are welcome!
If you’d like to extend the tool (e.g., add growth models, cohort tracking, or district comparisons), please open an issue.

---

## 📜 License

GNU- See attached file in the repository
---

## ✨ Created by

**Dr. Joseph Schroer**
College of Education
University of Wyoming


