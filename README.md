# 🚀 AI Learning Lab

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0.3-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange.svg)

**منصة تعليمية تفاعلية لتعلّم أساسيات الذكاء الاصطناعي وتعلّم الآلة من خلال التطبيق العملي**

[المزايا](#-المزايا) •
[التثبيت](#-التثبيت-والتشغيل) •
[الاستخدام](#-طريقة-الاستخدام) •
[البنية](#-بنية-المشروع) •
[المساهمة](#-المساهمة)

</div>

---

## 📋 نظرة عامة

AI Learning Lab هي منصة ويب تفاعلية مصممة لتعليم مفاهيم الذكاء الاصطناعي وتعلّم الآلة من خلال التجربة المباشرة بدلاً من الشرح النظري فقط. تتيح المنصة للمستخدمين رفع مجموعات البيانات، تجربة خوارزميات ML مختلفة، ومقارنة النتائج بشكل بصري وسهل الفهم.

### 🎯 الهدف من المشروع

- **التعلّم بالممارسة**: تطبيق عملي مباشر على البيانات الحقيقية
- **البساطة**: واجهة سهلة الاستخدام دون الحاجة لخبرة برمجية
- **الشفافية**: عرض المعادلات والحسابات خطوة بخطوة
- **المقارنة**: إمكانية تجربة خوارزميات متعددة ومقارنة الأداء

---

## ✨ المزايا

### 🔧 إدارة البيانات
- ✅ رفع ملفات CSV مخصصة
- ✅ مجموعات بيانات جاهزة (Iris, Titanic, Student Performance)
- ✅ تحليل تلقائي للأعمدة (رقمي/فئوي، قيم مفقودة)
- ✅ معاينة البيانات قبل التدريب
- ✅ دعم السحب والإفلات (Drag & Drop)

### 🤖 التجارب والنماذج
- ✅ دعم **Classification** و **Regression**
- ✅ 4 خوارزميات أساسية:
  - Linear Regression
  - Logistic Regression
  - Decision Tree
  - K-Nearest Neighbors (KNN)
- ✅ **AutoML**: اختيار أفضل خوارزمية تلقائيًا
- ✅ تقسيم البيانات قابل للتخصيص (10%-40%)
- ✅ خيار Randomization لتقسيم البيانات

### 📊 التقييم والنتائج

#### Classification Metrics:
- Accuracy
- Precision & Recall
- F1-Score
- Confusion Matrix مع شرح مفصّل

#### Regression Metrics:
- R² Score
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

### 🎓 محتوى تعليمي
- ✅ **مركز التعلّم**: شرح نظري للمفاهيم الأساسية
- ✅ **مختبر الأكواد**: أمثلة جاهزة قابلة للتنفيذ على Google Colab
- ✅ **شرح المعادلات**: عرض الحسابات خطوة بخطوة

### ⚡ ميزات إضافية
- ✅ **Interactive Prediction**: إدخال بيانات جديدة والتنبؤ فوراً
- ✅ **تقرير AutoML**: مقارنة شاملة بين الخوارزميات
- ✅ **Feature Scaling**: تطبيع تلقائي للخوارزميات التي تحتاجه
- ✅ **One-Hot Encoding**: معالجة البيانات الفئوية
- ✅ **حفظ النماذج**: إعادة استخدام النماذج المدربة

---

## 🛠️ التقنيات المستخدمة

### Backend
- **Django 6.0.3**: إطار الويب الأساسي
- **Django REST Framework 3.16.0**: بناء API
- **pandas 2.3.0**: معالجة البيانات
- **scikit-learn 1.3.2**: خوارزميات ML والتقييم
- **numpy 1.26.4**: عمليات رياضية
- **joblib 1.5.1**: حفظ النماذج

### Frontend
- **TailwindCSS**: تصميم الواجهة
- **Vanilla JavaScript**: التفاعلات
- **Google Fonts**: IBM Plex Sans Arabic + JetBrains Mono

### Database
- **SQLite3**: قاعدة بيانات خفيفة (قابلة للتبديل بـ PostgreSQL/MySQL)

---

## 📥 التثبيت والتشغيل

### المتطلبات الأساسية
- Python 3.10 أو أحدث
- pip (مثبت مع Python)
- Git (اختياري)

### 1️⃣ نسخ المشروع

```bash
git clone https://github.com/YOUR_USERNAME/ai_learning_lab.git
cd ai_learning_lab
```

أو تحميل الملف المضغوط مباشرة.

### 2️⃣ إنشاء بيئة افتراضية

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 4️⃣ تنفيذ الترحيلات (Migrations)

```bash
python manage.py migrate
```

### 5️⃣ تشغيل السيرفر

```bash
python manage.py runserver
```

### 6️⃣ فتح المتصفح

افتح المتصفح وتوجه إلى:
- **الصفحة الرئيسية**: http://127.0.0.1:8000/
- **مركز التعلم**: http://127.0.0.1:8000/learn/
- **مختبر الأكواد**: http://127.0.0.1:8000/learn/code-lab/
- **البيانات**: http://127.0.0.1:8000/datasets/
- **التجارب**: http://127.0.0.1:8000/experiments/

---

## 🎮 طريقة الاستخدام

### خطوة 1: فهم المفاهيم
1. اذهب إلى `/learn/` لقراءة الأساسيات النظرية
2. افتح `/learn/code-lab/` للاطلاع على الأمثلة البرمجية

### خطوة 2: رفع البيانات
1. اذهب إلى `/datasets/`
2. اختر **رفع Dataset جديد** أو استخدم dataset جاهز
3. في حالة الرفع، اختر ملف CSV وحدد اسماً مناسباً
4. اضغط **رفع وتحليل**

### خطوة 3: إنشاء تجربة
1. من صفحة البيانات، اضغط **تجربة** بجانب Dataset
2. أو اذهب مباشرة إلى `/experiments/new/`
3. اتبع الخطوات الخمسة:
   - اختر Dataset
   - حدد عمود الهدف (Target)
   - اختر نوع المشكلة (Classification/Regression)
   - اختر خوارزمية (أو فعّل AutoML)
   - حدد نسبة بيانات الاختبار
4. اضغط **ابدأ التدريب**

### خطوة 4: قراءة النتائج
- **Regression**: R², MSE, RMSE + جدول المقارنة
- **Classification**: Accuracy, Precision, Recall, F1 + Confusion Matrix
- شاهد **شرح الحسابات** لفهم كيفية حساب المقاييس
- جرّب **التوقع التفاعلي** من نفس الصفحة

### خطوة 5: المقارنة والتحسين
1. جرّب خوارزميات مختلفة على نفس Dataset
2. قارن النتائج في قائمة التجارب
3. استخدم **AutoML** لمعرفة الخوارزمية الأفضل تلقائياً
4. اقرأ **تقرير AutoML** لفهم الفروقات

---

## 📁 بنية المشروع

```
ai_learning_lab/
│
├── config/                    # إعدادات Django الرئيسية
│   ├── __init__.py
│   ├── settings.py           # إعدادات المشروع
│   ├── urls.py               # مسارات URL الرئيسية
│   ├── wsgi.py
│   └── asgi.py
│
├── datasets/                  # تطبيق إدارة البيانات
│   ├── builtin_data/         # مجموعات البيانات الجاهزة
│   │   ├── iris.csv          # تصنيف أنواع الزهور
│   │   ├── student.csv       # تنبؤ درجات الطلاب
│   │   └── titanic.csv       # تنبؤ النجاة من التايتانيك
│   ├── migrations/           # ترحيلات قاعدة البيانات
│   ├── templates/datasets/   # واجهات HTML
│   │   ├── list.html         # قائمة البيانات
│   │   └── preview.html      # معاينة Dataset
│   ├── models.py             # نموذج Dataset
│   ├── views.py              # منطق العرض
│   └── urls.py               # مسارات Datasets
│
├── experiments/               # تطبيق التجارب والتدريب
│   ├── migrations/
│   ├── templates/experiments/
│   │   ├── list.html         # قائمة التجارب
│   │   ├── new.html          # إنشاء تجربة جديدة
│   │   ├── detail.html       # عرض النتائج
│   │   └── automl_report.html # تقرير AutoML
│   ├── models.py             # نموذج Experiment
│   ├── views.py              # منطق التجارب
│   └── urls.py
│
├── ml_engine/                 # محرك ML الأساسي
│   ├── __init__.py
│   ├── preprocessor.py       # تنظيف ومعالجة البيانات
│   ├── trainer.py            # تدريب النماذج
│   ├── evaluator.py          # تقييم الأداء
│   └── automl.py             # اختيار أفضل خوارزمية
│
├── templates/                 # قوالب HTML العامة
│   ├── base.html             # القالب الأساسي
│   ├── home.html             # الصفحة الرئيسية
│   └── learn/                # صفحات التعلّم
│       ├── index.html        # مركز التعلّم
│       └── code_lab.html     # مختبر الأكواد
│
├── media/                     # ملفات المستخدمين (تُنشأ تلقائياً)
│   ├── datasets/             # ملفات CSV المرفوعة
│   └── models/               # النماذج المحفوظة (.pkl)
│
├── manage.py                  # أداة إدارة Django
├── requirements.txt           # المكتبات المطلوبة
├── .gitignore                # ملفات محذوفة من Git
└── README.md                 # هذا الملف
```

### وصف المكونات الرئيسية

#### 🗂️ `datasets/`
- **models.py**: نموذج `Dataset` يحتوي على (اسم، ملف، عدد صفوف/أعمدة)
- **views.py**: منطق رفع الملفات، تحميل datasets جاهزة، معاينة البيانات
- **builtin_data/**: مجموعات بيانات جاهزة للتجربة الفورية

#### 🧪 `experiments/`
- **models.py**: نموذج `Experiment` يحتوي على (نوع المشكلة، الخوارزمية، النتائج)
- **views.py**: منطق إنشاء التجارب، التدريب، عرض النتائج، التوقع
- **automl_report.html**: صفحة مخصصة لمقارنة AutoML

#### ⚙️ `ml_engine/`
- **preprocessor.py**: تنظيف البيانات، One-Hot Encoding، تقسيم Train/Test
- **trainer.py**: إنشاء وتدريب النماذج (Linear, Logistic, Tree, KNN)
- **evaluator.py**: حساب جميع المقاييس (Accuracy, R², MSE, Confusion Matrix)
- **automl.py**: تجربة جميع الخوارزميات واختيار الأفضل

---

## 🧮 كيف تعمل الخوارزميات

### 1. Linear Regression
- **الاستخدام**: Regression (توقع قيمة رقمية)
- **المبدأ**: إيجاد خط مستقيم يقلل المسافة من جميع النقاط
- **المعادلة**: `y = mx + b`

### 2. Logistic Regression
- **الاستخدام**: Binary Classification (تصنيف ثنائي)
- **المبدأ**: استخدام دالة sigmoid لتحويل القيم إلى احتمالات (0-1)
- **المعادلة**: `P(y=1) = 1 / (1 + e^-(mx+b))`

### 3. Decision Tree
- **الاستخدام**: Classification و Regression
- **المبدأ**: بناء شجرة قرارات بناءً على شروط منطقية
- **المزايا**: سهل الفهم والتفسير

### 4. K-Nearest Neighbors (KNN)
- **الاستخدام**: Classification و Regression
- **المبدأ**: التصويت بناءً على أقرب K نقطة
- **ملاحظة**: يحتاج Feature Scaling

---

## 📊 فهم المقاييس

### Classification Metrics

#### Accuracy (الدقة)
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```
- **المعنى**: نسبة التوقعات الصحيحة من الإجمالي
- **متى تستخدمها**: عند توازن الفئات

#### Precision (الدقة الإيجابية)
```
Precision = TP / (TP + FP)
```
- **المعنى**: من كل ما توقعناه إيجابي، كم كان صحيح؟
- **متى تستخدمها**: عندما False Positive مكلف (مثل تشخيص طبي)

#### Recall (الاستدعاء)
```
Recall = TP / (TP + FN)
```
- **المعنى**: من كل الحالات الإيجابية الفعلية، كم اكتشفنا؟
- **متى تستخدمها**: عندما False Negative خطير (مثل كشف السرطان)

#### F1-Score
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```
- **المعنى**: متوسط هارموني بين Precision و Recall

### Regression Metrics

#### R² Score (معامل التحديد)
```
R² = 1 - (SS_res / SS_tot)
```
- **النطاق**: -∞ إلى 1
- **المعنى**: نسبة التباين المفسّرة بواسطة النموذج
- **القيمة المثالية**: 1 (توقع مثالي)

#### MSE (Mean Squared Error)
```
MSE = (1/n) × Σ(y_actual - y_predicted)²
```
- **المعنى**: متوسط مربع الأخطاء
- **العيب**: حساس جداً للقيم الشاذة

#### RMSE (Root Mean Squared Error)
```
RMSE = √MSE
```
- **المعنى**: جذر MSE بنفس وحدة الهدف
- **الميزة**: سهل التفسير

---

## 🔍 الـ AutoML - كيف يعمل؟

عند تفعيل AutoML، يقوم النظام بـ:

1. **تجربة جميع الخوارزميات المناسبة**:
   - Classification: Logistic Regression, Decision Tree, KNN
   - Regression: Linear Regression, Decision Tree, KNN

2. **تدريب كل خوارزمية** على نفس بيانات Train

3. **تقييم الأداء** على نفس بيانات Test

4. **المقارنة**:
   - Classification: حسب Accuracy
   - Regression: حسب R²

5. **اختيار الأفضل** تلقائياً وعرض تقرير شامل

**متى تستخدم AutoML؟**
- عندما لا تعرف أي خوارزمية مناسبة
- للحصول على baseline سريع
- لمقارنة جميع الخوارزميات مرة واحدة

---

## 🧪 أمثلة على حالات الاستخدام

### مثال 1: تصنيف الزهور (Iris)
```
Dataset: iris.csv
Target: species (setosa, versicolor, virginica)
Problem Type: Classification
Best Algorithm: KNN
Expected Accuracy: ~95%
```

### مثال 2: توقع النجاة من التايتانيك
```
Dataset: titanic.csv
Target: survived (0/1)
Problem Type: Classification
Features: pclass, sex, age, fare, etc.
Best Algorithm: Logistic Regression
Expected Accuracy: ~75-80%
```

### مثال 3: توقع درجات الطلاب
```
Dataset: student.csv
Target: grade
Problem Type: Regression
Features: age, studytime, failures, absences
Best Algorithm: Linear Regression
Expected R²: ~0.70-0.85
```

---

## 🐛 استكشاف الأخطاء

### مشكلة: "No module named 'sklearn'"
**الحل:**
```bash
pip install scikit-learn==1.3.2
```

### مشكلة: خطأ في قراءة CSV
**الأسباب المحتملة:**
- الملف ليس بصيغة CSV صحيحة
- وجود أعمدة بدون قيم
- ترميز الملف ليس UTF-8

**الحل:**
- تأكد من أن الملف CSV صحيح
- استخدم Excel/Pandas لإعادة حفظ الملف

### مشكلة: Accuracy منخفضة جداً
**الأسباب المحتملة:**
- البيانات غير متوازنة
- Features غير مناسبة
- الخوارزمية غير مناسبة لنوع البيانات

**الحل:**
- جرّب AutoML لاختيار أفضل خوارزمية
- جرّب features مختلفة
- زد حجم Dataset

### مشكلة: التوقع التفاعلي لا يعمل
**الحل:**
- تأكد من إدخال جميع الـ features
- تأكد من أن الأنواع صحيحة (رقمي/نصي)
- افتح Developer Console للتحقق من الأخطاء

---

## 🙏 شكر وتقدير

- [Django](https://www.djangoproject.com/) - إطار الويب
- [scikit-learn](https://scikit-learn.org/) - مكتبة ML
- [TailwindCSS](https://tailwindcss.com/) - إطار التصميم
- [Google Fonts](https://fonts.google.com/) - الخطوط العربية

---

## 📞 التواصل والدعم

- **GitHub Issues**: [فتح issue جديد](https://github.com/QasemQareish/ai_learning_lab/issues)
- **Email**: qasem.qareish@gmail.com

---

<div align="center">

**صُنع بـ ❤️ لتبسيط تعلّم الذكاء الاصطناعي**

⭐ اتمنى ان ينال المشروع اعجابكم 

</div>